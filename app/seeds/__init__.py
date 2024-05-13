from flask.cli import AppGroup
# from app.models.db import db, environment, SCHEMA
from .cereals import seed_cereals,undo_cereals

# Creates a seed group to hold our commands
# So we can type `flask seed --help`
seed_commands = AppGroup('seed')


# Creates the `flask seed all` command
@seed_commands.command('all')
def seed():
    seed_cereals()
    return 

# Creates the `flask seed undo` command
@seed_commands.command('undo')
def undo():
    undo_cereals()
    return 
