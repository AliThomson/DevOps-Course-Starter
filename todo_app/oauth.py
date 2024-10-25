import os
from flask_dance.contrib.github import make_github_blueprint
from flask_dance.contrib.github import github
from flask import redirect, url_for
from functools import wraps

blueprint = make_github_blueprint(
    client_id = os.getenv('OAUTH_CLIENT_ID'),
    client_secret = os.getenv('OAUTH_CLIENT_SECRET'),
)

def login_required(func):
    @wraps(func)
    def wrapper_login_required(*args, **kwargs):
        if not github.authorized:
            return redirect(url_for("github.login"))
        
        return func(*args, **kwargs)
    
    return wrapper_login_required