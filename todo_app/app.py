from flask import Flask, render_template, request, redirect, url_for

from todo_app.classes.view_model import ViewModel
from todo_app.flask_config import Config
from todo_app.data.trello_items import get_cards, move_card
from todo_app.data.mongo_items import get_items, add_item, update_item

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config())

    @app.route('/')
    def index():
        items_view_model = ViewModel(get_cards())
        return render_template('index.html', view_model=items_view_model)

    @app.post('/add-card')
    def add_card_request():
        new_item = request.form.get('title')
        add_item(new_item)
        return redirect(url_for('index'))

    @app.post('/complete-card')
    def update_card_request():
        item_id = request.form.get('card_id')
        print(item_id)
        
        move_card(item_id, "done")
        return redirect(url_for('index'))
    
    return app

create_app()