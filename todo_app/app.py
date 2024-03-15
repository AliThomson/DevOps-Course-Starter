from flask import Flask, render_template, request, redirect, url_for

from todo_app.classes.view_model import ViewModel
from todo_app.flask_config import Config
from todo_app.data.trello_items import get_cards, add_card, move_card

app = Flask(__name__)
app.config.from_object(Config())

@app.route('/')
def index():
    cards_view_model = ViewModel(get_cards())
    return render_template('index.html', view_model=cards_view_model)

@app.post('/add-card')
def add_card_request():
    new_card = request.form.get('title')
    add_card(new_card)
    return redirect(url_for('index'))

@app.post('/complete-card')
def update_card_request():
    
    card_id = request.form.get('card_id')
    print(card_id)
    
    move_card(card_id, "done")
    return redirect(url_for('index'))