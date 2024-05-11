from flask import Flask
from flask_migrate import Migrate
from .config import Config

from .models import db

app = Flask(__name__)

@app.route("/")
def hello():
	return "Hello World"

app.config.from_object(Config)

db.init_app(app)
Migrate(app, db)