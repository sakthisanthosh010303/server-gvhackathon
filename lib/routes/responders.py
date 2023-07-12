# Author: Sakthi Santhosh
# Created on: 29/05/2023
from flask import (
    flash,
    redirect,
    render_template,
    url_for
)

from lib import app_handle, db_handle
from lib.forms import AddResponder
from lib.models import Responder

@app_handle.route("/add_responder", methods=["GET", "POST"])
def add_responder_handle():
    form = AddResponder()

    if form.validate_on_submit():
        db_handle.session.add(Responder(
            first_name=form.first_name.data,
            last_name=form.last_name.data,
            email_id=form.email_id.data,
            phone=form.phone.data,
            fr_type=form.fr_type.data
        ))
        db_handle.session.commit()

        flash(f"Responder \"{form.first_name.data} {form.last_name.data}\" was added successfully.")
        return redirect(url_for("responders_handle"))
    return render_template("add_responder.html", form=form)

@app_handle.route("/remove_responder/<int:guid>")
def remove_responder_handle(guid: int):
    data = Responder.query.get(guid)

    db_handle.session.delete(data)
    db_handle.session.commit()

    flash(f"Responder \"{data.first_name} {data.last_name}\" was removed successfully.")
    return redirect(url_for("responders_handle"))

@app_handle.route("/responders")
def responders_handle():
    data = Responder.query.all()
    return render_template("responders.html", responders=data)

@app_handle.route("/update_responder/<int:guid>", methods=["GET", "POST"])
def update_responder_handle(guid: int):
    data = Responder.query.get(guid)
    form = AddResponder(obj=data)

    if form.validate_on_submit():
        data.first_name = form.first_name.data
        data.last_name = form.last_name.data
        data.email_id = form.email_id.data
        data.phone = form.phone.data
        data.fr_type = form.fr_type.data

        db_handle.session.commit()
        flash(f"Responder \"{form.first_name.data} {form.last_name.data}\" was updated successfully.")
        return redirect(url_for("responders_handle"))
    return render_template("update_responder.html", form=form, responder=data)
