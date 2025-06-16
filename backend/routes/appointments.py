from flask import Blueprint, render_template, request, redirect, url_for, flash
from backend.models import Appointment
from backend import db
from datetime import datetime

appointments_bp = Blueprint('appointments_bp', __name__)

@appointments_bp.route('/')
def home():
    appointments = Appointment.query.order_by(Appointment.time).all()
    return render_template('index.html', appointments=appointments)

@appointments_bp.route('/book', methods=['POST'])
def book():
    name = request.form['name']
    phone = request.form['phone']
    time = datetime.strptime(request.form['time'], '%Y-%m-%dT%H:%M')
    massage_type = request.form['massage_type']

    existing = Appointment.query.filter_by(time=time).first()
    if existing:
        flash("Веќе има закажано за тоа време. Изберете друго.")
        return redirect(url_for('appointments_bp.home'))

    new_appt = Appointment(
        client_name=name,
        phone=phone,
        time=time,
        massage_type=massage_type
    )
    db.session.add(new_appt)
    db.session.commit()

    return redirect(url_for('appointments_bp.home'))
