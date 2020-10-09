import click
import psycopg2
import psycopg2.extras

from flask import Flask, current_app, g, Blueprint
from flask.cli import with_appcontext
from gunicorn_demo import poll_service

bp = Blueprint('db', __name__)


def get_db():
    if 'db' not in g:
        connection = psycopg2.connect(
            current_app.config['DATABASE_URL'],
            cursor_factory=psycopg2.extras.DictCursor)
        g.db = connection
    return g.db


def get_poll_service():
    if 'poll_service' not in g:
        g.poll_service = poll_service.PollService(db=get_db())
    return g.poll_service


def close_db(e=None):
    db = g.pop('db', None)

    if db is not None:
        db.close()


def init_db_context(app: Flask):
    app.teardown_appcontext(close_db)
