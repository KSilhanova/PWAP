from flask import Blueprint, render_template, request, flash, jsonify #Blueprint pomůže vytvořit opakovaně použitelné instance vaší aplikace. Dělá to tak, že svůj projekt organizujete do modulů.
from flask_login import login_required, current_user
from .models import Note
from . import db
import json

views = Blueprint('views', __name__) #jak se prostě definuje blueprint


@views.route('/', methods=['GET', 'POST'])
@login_required #pokud není přihlášený tak to nesmažeš
def home(): #defineje homepage
    if request.method == 'POST':
        note = request.form.get('note')

        if len(note) < 1:
            flash('Poznámka je příliš krátká!', category='error')
        else:
            new_note = Note(data=note, user_id=current_user.id)
            db.session.add(new_note)
            db.session.commit()
            flash('Poznámka přidáná!', category='success')

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
