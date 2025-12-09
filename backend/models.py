# from backend import db
# from datetime import datetime
#
# class Appointment(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     client_name = db.Column(db.String(100), nullable=False)
#     phone = db.Column(db.String(20), nullable=False)
#     time = db.Column(db.DateTime, nullable=False)
#     created_at = db.Column(db.DateTime, default=datetime.utcnow)
#     massage_type = db.Column(db.String(50), nullable=False)
from backend import db
from datetime import datetime

class Appointment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    client_name = db.Column(db.String(100), nullable=False)
    phone = db.Column(db.String(20), nullable=False)
    time = db.Column(db.DateTime, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    massage_type = db.Column(db.String(50), nullable=False)
