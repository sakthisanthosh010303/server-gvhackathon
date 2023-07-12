# Author: Sakthi Santhosh
# Created on: 22/04/2023
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from uuid import uuid4

app_handle = Flask(__name__)

app_handle.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
app_handle.config["SECRET_KEY"] = str(uuid4())

db_handle = SQLAlchemy(app_handle)

from lib.routes import devices, main, responders
