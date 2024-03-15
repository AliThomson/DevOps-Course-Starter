from flask import Flask, render_template, request, redirect, url_for

from todo_app.classes.view_model import ViewModel
from todo_app.flask_config import Config
from todo_app.data.trello_items import get_items, add_item, move_item

app = Flask(__name__)
app.config.from_object(Config())

@app.route('/')
def index():
    items_view_model = ViewModel(get_items())
    return render_template('index.html', view_model=items_view_model)

@app.post('/add-item')
def add_item_request():
    new_item = request.form.get('title')
    add_item(new_item)
    return redirect(url_for('index'))

@app.post('/complete-item')
def update_item_request():
    
    item_id = request.form.get('item_id')
    print(item_id)
    
    move_item(item_id, "done")
    return redirect(url_for('index'))