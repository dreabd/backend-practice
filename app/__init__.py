import os
from flask import Flask
from flask_migrate import Migrate

from flask_wtf.csrf import CSRFProtect, generate_csrf

from .seeds import seed_commands
from .config import Config

from .models import db

# API ROUTES

from .api.cereal_routes import cereal_routes

app = Flask(__name__)

app.cli.add_command(seed_commands)

app.config.from_object(Config)
app.register_blueprint(cereal_routes, url_prefix="/api/cereals")

db.init_app(app)
Migrate(app, db)

@app.route("/")
def hello():
	return "Hello World"


@app.after_request
def inject_csrf_token(response):
    response.set_cookie(
        'csrf_token',
        generate_csrf(),
        secure=True if os.environ.get('FLASK_ENV') == 'production' else False,
        samesite='Strict' if os.environ.get(
            'FLASK_ENV') == 'production' else None,
        httponly=True)
    return response