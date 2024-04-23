from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from .models import Note, Event  # Assuming you have an Event model
from . import db
import json
from datetime import datetime

views = Blueprint('views', __name__)

@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    if request.method == 'POST':
        title = request.form.get('title')
        start = request.form.get('start')
        end = request.form.get('end')

        if not title or not start or not end:
            flash('Event details are required.', category='error')
        else:
            new_event = Event(title=title, start_date=datetime.fromisoformat(start), end_date=datetime.fromisoformat(end), user_id=current_user.id)
            db.session.add(new_event)
            db.session.commit()
            flash('Event added!', category='success')

    return render_template("home.html", user=current_user)

@views.route('/delete-note', methods=['POST'])
def delete_note():
    note = json.loads(request.data)
    noteId = note['noteId']
    note = Note.query.get(noteId)
    if note:
        if note.user_id == current_user.id:
            db.session.delete(note)
            db.session.commit()
    return jsonify({})

@views.route('/calendar')
@login_required
def calendar():
    events = Event.query.filter_by(user_id=current_user.id).all()
    event_data = [
        {
            'title': event.title,
            'start': event.start_date.isoformat(),
            'end': event.end_date.isoformat()
        }
        for event in events
    ]
    return jsonify(event_data)

@views.route('/random-event')
def random_event():
    return render_template('random_event.html')