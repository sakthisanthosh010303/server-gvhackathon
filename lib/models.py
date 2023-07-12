# Author: Sakthi Santhosh
# Created on: 22/04/2023
from lib import db_handle

class Responder(db_handle.Model):
    guid = db_handle.Column(
        db_handle.Integer,
        primary_key=True
    )
    first_name = db_handle.Column(
        db_handle.String(50),
        unique=False,
        nullable=False
    )
    last_name = db_handle.Column(
        db_handle.String(50),
        unique=False,
        nullable=True
    )
    email_id = db_handle.Column(
        db_handle.String(50),
        unique=True,
        nullable=False
    )
    phone = db_handle.Column(
        db_handle.String(15),
        unique=True,
        nullable=False
    )
    fr_type = db_handle.Column(
        db_handle.String(2),
        unique=False,
        nullable=False
    )

    def __repr__(self):
        return f"<Responder {self.first_name} {self.last_name} ({self.fr_type})>"

class Event(db_handle.Model):
    guid = db_handle.Column(
        db_handle.Integer,
        primary_key=True
    )
    datetime = db_handle.Column(
        db_handle.DateTime(timezone=True),
        unique=False,
        nullable=False
    )
    device_id = db_handle.Column(
        db_handle.String(36),
        unique=False,
        nullable=False
    )
    animal_class = db_handle.Column(
        db_handle.String(10),
        unique=False,
        nullable=False
    )
    image = db_handle.Column(
        db_handle.Text
    )

    def __repr__(self):
        return f"<Event {self.datetime} {self.device_id} ({self.animal_class})>"

class Device(db_handle.Model):
    guid = db_handle.Column(
        db_handle.Integer,
        primary_key=True
    )
    device_id = db_handle.Column(
        db_handle.String(36),
        unique=False,
        nullable=False
    )
    name = db_handle.Column(
        db_handle.String(30),
        unique=True,
        nullable=False
    )
    latitude = db_handle.Column(
        db_handle.Float,
        unique=False,
        nullable=False
    )
    longitude= db_handle.Column(
        db_handle.Float,
        unique=False,
        nullable=False
    )
    last_updated = db_handle.Column(
        db_handle.DateTime(timezone=True),
        unique=False,
        nullable=True
    )

    def __repr__(self):
        return f"<Device {self.device_id} ({self.latitude}, {self.longitude})>"
