# Author: Sakthi Santhosh
# Created on: 29/05/2023
from datetime import datetime
from flask import (
    jsonify,
    make_response,
    render_template,
    request
)

from lib import app_handle, db_handle
from lib.actions import NotificationDispatcher
from lib.constants import EMAIL_LIMIT_PERIOD_S, VALID_ANIMAL_CLASSES
from lib.models import Device, Event, Responder

last_event = datetime(2023, 1, 1, 12, 0, 0)

@app_handle.route('/')
def index_handle():
    return render_template("index.html")

@app_handle.route("/add_event", methods=["POST"])
def add_event_handle():
    global last_event

    try:
        payload = request.get_json()
    except:
        return make_response(jsonify(
            response="bad_request", message="No request body."
        ), 400)

    if (
        "animal_class" not in payload
        or "device_id" not in payload
        or "image" not in payload
    ):
        return make_response(jsonify(
            response="bad_request", message="Missing data field(s)."
        ), 400)

    if payload["animal_class"] not in VALID_ANIMAL_CLASSES:
        return make_response(jsonify(
            response="bad_request", message="Invalid animal class provided."
        ), 400)

    device = Device.query.filter_by(device_id=payload["device_id"]).first()

    if device is None:
        return make_response(jsonify(response="auth_error"), 401)

    dt = datetime.now()
    device.last_updated = dt

    db_handle.session.add(Event(
        datetime=dt,
        device_id=payload["device_id"],
        animal_class=payload["animal_class"],
        image=payload["image"]
    ))
    db_handle.session.commit()

    if (
        payload["animal_class"] != "none"
        and (dt - last_event).total_seconds() > EMAIL_LIMIT_PERIOD_S
    ):
        responders = Responder.query.all()

        if responders:
            first_responders = {
                "email_ids": [],
                "phones": []
            }

            for responder in responders:
                first_responders["email_ids"].append(responder.email_id)
                first_responders["phones"].append(responder.phone)

            NotificationDispatcher(first_responders, {
                "animal_class": payload["animal_class"],
                "datetime": str(dt),
                "image": payload["image"],
                "location": "%f,%f"%(device.latitude, device.longitude),
            }).notify()
    last_event = dt
    return make_response(jsonify(response="success"), 200)

@app_handle.route("/get_event")
def get_event_handle():
    data = Event.query.order_by(Event.guid.desc()).first()

    if not data:
        return make_response(jsonify(response="no_content"), 204)

    device = Device.query.filter_by(device_id=data.device_id).first()
    return jsonify({
        "animal_class": data.animal_class,
        "datetime": data.datetime,
        "device_id": data.device_id,
        "image": data.image,
        "location": f"{device.latitude},{device.longitude}"
    })

@app_handle.errorhandler(404)
def error404_handle(error):
    return render_template("error404.html")
