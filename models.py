from app import db
from datetime import datetime

class Participant(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    # Extend with additional fields
    sessions = db.relationship('Session', backref='participant', lazy='dynamic')

class Session(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    participant_id = db.Column(db.Integer, db.ForeignKey('participant.id'), nullable=False)
    session_type = db.Column(db.String(50))  # intake, middle, outtake
    start_time = db.Column(db.DateTime, default=datetime.utcnow)
    end_time = db.Column(db.DateTime)
    score = db.Column(db.Integer)
    paperwork_completed = db.Column(db.Boolean, default=False)
    paperwork_details = db.Column(db.String(200))
    session_data_file = db.Column(db.String(200))  # Path to stored file
    computed_values = db.Column(db.Text)  # JSON or similar structured data

    # Methods to handle session data here