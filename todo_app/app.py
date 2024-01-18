from flask import Flask, render_template, request, redirect, url_for

from todo_app.flask_config import Config
from todo_app.data.session_items import get_items, add_item

app = Flask(__name__)
app.config.from_object(Config())

@app.route('/')
def index():
    return render_template('index.html', items=get_items())

@app.post('/add-item')
def add_item_request():
    new_item = request.form.get('title')
    add_item(new_item)
    return redirect(url_for('index'))