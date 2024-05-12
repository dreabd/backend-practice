from flask import Flask
from flask_migrate import Migrate

from .seeds import seed_commands
from .config import Config

from .models import db

app = Flask(__name__)

app.cli.add_command(seed_commands)

app.config.from_object(Config)

db.init_app(app)
Migrate(app, db)

@app.route("/")
def hello():
	return "Hello World"

