from flask import Flask, render_template, request, redirect, url_for

from todo_app.flask_config import Config
from todo_app.data.session_items import get_item, save_item, STATUSES
from todo_app.data.trello_items import get_items, add_item

app = Flask(__name__)
app.config.from_object(Config())

@app.route('/')
def index():
    return render_template('index.html', items=get_items(), statuses=STATUSES)

@app.post('/add-item')
def add_item_request():
    new_item = request.form.get('title')
    add_item(new_item)
    return redirect(url_for('index'))

@app.post('/update-status')
def update_status_request():
    new_status = request.form.get('status')
    item_id = int(request.form.get('item_id'))
    item_to_update = get_item(item_id)
    
    updated_item = { 'id': item_id, 'title': item_to_update['title'], 'status': new_status }

    save_item(updated_item)
    return redirect(url_for('index'))