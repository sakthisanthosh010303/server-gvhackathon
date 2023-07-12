# Author: Sakthi Santhosh
# Created on: 23/04/2023
EMAIL_BODY = """<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Alert: Wildlife Intrusion Detected</title>
  </head>
  <body>
    <b>Dear Sir/Madam,</b><br>
    &emsp;A <b>%s</b> was detected in the vicinity. Details of the incident are mentioned below.
    You are requested to immediately seek for a safe place until further notice.<br><br>
    <b>Date & Time:</b>
    %s<br>
    <b>Location:</b>
    <a href="%s">Google Maps</a><br><br>
    <b>Regrads,</b><br>
    Team Sussy Bakas
  </body>
</html>
"""

SMS_BODY = """Danger: Wildlife Intrusion Detected

Dear Sir/Madam,
    A %s was detected in the vicinity. Details of the incident are mentioned below. \
You are requested to immediately seek for a safe place until further notice.

Date & Time: %s
Location: %s

Regards,
Team Sussy Bakas
"""

VALID_ANIMAL_CLASSES = ["leopard", "cheetah", "lion", "tiger", "none"]
MAPS_LINK = "http://www.google.com/maps/place/"

EMAIL_LIMIT_PERIOD_S = 900
FROM_EMAIL_ID = "sakthisanthosh010303@gmail.com"
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
