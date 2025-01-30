import os
from flask import Flask, render_template, request, redirect, url_for
from werkzeug.middleware.proxy_fix import ProxyFix

from todo_app.oauth import login_required, blueprint

from loggly.handlers import HTTPSHandler
from logging import Formatter

from todo_app.classes.item_service import ItemService
from todo_app.classes.view_model import ViewModel
from todo_app.flask_config import Config

def create_app():
    app = Flask(__name__)
    app.wsgi_app = ProxyFix(app.wsgi_app)
    app.config.from_object(Config())

    app.logger.setLevel(os.environ.get('LOG_LEVEL'))
    if app.config['LOGGLY_TOKEN'] is not None:
        handler = HTTPSHandler(f'https://logs-01.loggly.com/inputs/{app.config["LOGGLY_TOKEN"]}/tag/todo-app')
        handler.setFormatter(
            Formatter("[%(asctime)s] %(levelname)s in %(module)s: %(message)s")
        )
        app.logger.addHandler(handler)

    app.register_blueprint(blueprint, url_prefix="/login")
    
    item_service = ItemService()

    @app.route('/')
    @login_required
    def index():    
        items_view_model = ViewModel(item_service.get_items())
        app.logger.info("Homepage viewed")
        return render_template('index.html', view_model=items_view_model)

    @app.post('/add-item')
    @login_required
    def add_item_request():
        new_item = request.form.get('title')
        item_service.add_item(new_item)
        return redirect(url_for('index'))

    @app.post('/complete-item')
    @login_required
    def update_item_request():
        item_id = request.form.get('item_id')       
        item_service.update_item(item_id, "Done")
        return redirect(url_for('index'))
    
    return app
