# Author: Sakthi Santhosh
# Created on: 25/04/2023
from base64 import b64decode
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from os import getenv
from smtplib import SMTP
from threading import Thread
from twilio.rest import Client

from lib.constants import (
    FROM_EMAIL_ID,
    MAPS_LINK,
    EMAIL_BODY,
    SMS_BODY,
    SMTP_SERVER,
    SMTP_PORT
)

class NotificationDispatcher:
    def __init__(self, first_responders: dict, metadata: dict) -> None:
        self.secrets = {}
        self.first_responders = first_responders
        self.metadata = metadata

        self._load_secrets()

    def _load_secrets(self) -> None:
        self.secrets["smtp_key"] = getenv("FLASK_SMTP_KEY")
        self.secrets["twilio_sid"] = getenv("FLASK_TWILIO_SID")
        self.secrets["twilio_auth_token"] = getenv("FLASK_TWILIO_AUTH_TOKEN")
        self.secrets["twilio_phone"] = getenv("FLASK_TWILIO_PHONE")

    def _send_sms(self) -> None:
        twilio_handle = Client(self.secrets["twilio_sid"], self.secrets["twilio_auth_token"])

        for phone in self.first_responders["phones"]:
            twilio_handle.messages.create(
                body=SMS_BODY%(
                    self.metadata["animal_class"],
                    self.metadata["datetime"].split('.')[0],
                    MAPS_LINK + self.metadata["location"]
                ),
                from_=self.secrets["twilio_phone"],
                to=phone.replace(' ', '')
            )

    def _send_email(self) -> None:
        message = MIMEMultipart()
        message["From"] = FROM_EMAIL_ID
        message["To"] = ", ".join(self.first_responders["email_ids"])
        message["Subject"] = "Danger: Wildlife Intrusion Detected"
        message.attach(
            MIMEText(EMAIL_BODY%(
                self.metadata["animal_class"],
                self.metadata["datetime"].split('.')[0],
                MAPS_LINK + self.metadata["location"]
            ), "html")
        )

        image = MIMEImage(b64decode(self.metadata["image"]), name="Image.jpg")
        image.add_header("Content-Disposition", "attachment", filename="Image.jpg")
        message.attach(image)

        with SMTP(SMTP_SERVER, SMTP_PORT) as smtp_handle:
            smtp_handle.starttls()
            smtp_handle.login(FROM_EMAIL_ID, self.secrets["smtp_key"])

            smtp_handle.sendmail(
                FROM_EMAIL_ID,
                self.first_responders["email_ids"],
                message.as_string()
            )

    def notify(self):
        Thread(target=self._send_email).start()
        Thread(target=self._send_sms).start()
