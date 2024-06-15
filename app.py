from flask import Flask, render_template, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Config
from forms import ParticipantForm

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy()
db.init_app(app)  # Initialize SQLAlchemy with your Flask app
migrate = Migrate(app, db)

# Import your models after initializing the db
from models import Participant, Session

@app.route('/')
def hello():
    # Fetch all participants from the database
    participants = Participant.query.all()
    return render_template('home.html', 
                           current_phase='before', 
                           participants=participants, 
                           scheduled_participant=None, 
                           participant_confirmed=False)

@app.route('/participants')
def list_participants():
    try:
        participants = Participant.query.all()
        participants_data = []
        for participant in participants:
            total_sessions = 16  # Total expected sessions
            completed_sessions = Session.query.filter_by(participant_id=participant.id, paperwork_completed=True).count()
            participants_data.append({
                'id': participant.id,
                'name': participant.name,
                'email': participant.email,
                'completed_sessions': completed_sessions,
                'total_sessions': total_sessions
            })
        return render_template('participants.html', participants=participants_data)
    except Exception as e:
        print(f"Error: {e}")
        flash("An error occurred while fetching participants.")
        return redirect(url_for('hello'))
    

@app.route('/view_sessions/<int:participant_id>')
def view_session(participant_id):
    participant = Participant.query.get_or_404(participant_id)
    sessions = Session.query.filter_by(participant_id=participant_id).all()
    return render_template('view_sessions.html', participant=participant, sessions=sessions)

@app.route('/update_session/<int:session_id>', methods=['GET', 'POST'])
def update_session(session_id):
    session = Session.query.get_or_404(session_id)
    form = SessionForm()
    if form.validate_on_submit():
        session.paperwork_completed = form.is_completed.data
        db.session.commit()
        flash('Session updated successfully.')
        return redirect(url_for('list_participants'))
    form.is_completed.data = session.paperwork_completed
    return render_template('update_session.html', form=form, session=session)


@app.route('/participants/create', methods=['GET', 'POST'])
def create_participant():
    form = ParticipantForm()
    if form.validate_on_submit():
        participant = Participant(name=form.name.data, email=form.email.data)
        db.session.add(participant)
        db.session.commit()
        flash('Participant created successfully.')
        return redirect(url_for('list_participants'))
    return render_template('create_participant.html', form=form)

@app.route('/participants/<int:participant_id>/edit', methods=['GET', 'POST'])
def edit_participant(participant_id):
    participant = Participant.query.get_or_404(participant_id)
    form = ParticipantForm(obj=participant)
    if form.validate_on_submit():
        form.populate_obj(participant)
        db.session.commit()
        flash('Participant updated successfully.')
        return redirect(url_for('list_participants'))
    return render_template('edit_participant.html', form=form, participant=participant)

@app.route('/participants/<int:participant_id>/delete', methods=['POST'])
def delete_participant(participant_id):
    participant = Participant.query.get_or_404(participant_id)
    db.session.delete(participant)
    db.session.commit()
    flash('Participant deleted successfully.')
    return redirect(url_for('list_participants'))


@app.route('/select-participant', methods=['POST'])
def select_participant():
    # Implementation for selecting a participant
    participant_id = request.form['participant_id']
    # Logic to handle participant selection
    return redirect(url_for('list_participants'))

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)