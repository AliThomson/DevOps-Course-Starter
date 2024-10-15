from flask import Flask, render_template, request, redirect, url_for

from todo_app.classes.item_service import ItemService
from todo_app.classes.view_model import ViewModel
from todo_app.flask_config import Config

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config())
    item_service = ItemService()

    @app.route('/')
    def index():
        items_view_model = ViewModel(item_service.get_items())
        return render_template('index.html', view_model=items_view_model)

    @app.post('/add-item')
    def add_item_request():
        new_item = request.form.get('title')
        item_service.add_item(new_item)
        return redirect(url_for('index'))

    @app.post('/complete-item')
    def update_item_request():
        item_id = request.form.get('item_id')
        print(item_id)
        
        item_service.update_item(item_id, "Done")
        return redirect(url_for('index'))
    
    return app

create_app()