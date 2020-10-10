
from pytest import fixture
from unittest import mock
import os
import tempfile

import pytest

from gunicorn_demo.flask import app
from gunicorn_demo.flask.db import init_db_context

@pytest.fixture(scope='session')
def client():
    app.config['TESTING'] = True

    with app.test_client() as client:
        with app.app_context():
            init_db_context(app)
        yield client
