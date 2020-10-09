import os
from pathlib import Path

from flask import Flask
from .db import init_db_context
import logging
import logging.config
from .api_v1 import api_v1
rootdir = (Path(__file__) / '../../..').resolve()


def env_bool(key, default=False):
    val = os.getenv(key, '')
    if val == '' or val.isspace():
        return default
    return val.lower() in {'yes', 'on', 'true'}


app = Flask(__name__)
app.config.from_mapping(
    DEBUG=env_bool('FLASK_DEBUG'),
    DATABASE_URL=os.getenv('FLASK_DATABASE_URL', 'dbname=gunicorn_demo'),
    LOGGING={
        'version': 1,
        'disable_existing_loggers': False,
        'formatters': {
            'verbose': {
                'format':
                '{levelname} {asctime} {module} {process:d} {thread:d} {message}',
                'style': '{',
            },
            'simple': {
                'format': '{levelname} {message}',
                'style': '{',
            },
        },
        'filters': {},
        'handlers': {
            'console': {
                'level': os.getenv('FLASK_LOGGING_LEVEL', 'INFO'),
                'filters': [],
                'class': 'logging.StreamHandler',
                'formatter': os.getenv('FLASK_LOGGING_FORMATTER', 'verbose')
            }
        },
        'loggers': {
            'root': {
                'handlers': ['console'],
                'propagate': True,
            }
        }
    })
logging.config.dictConfig({
    'version': 1,
    'formatters': {
        'default': {
            'format': '[%(asctime)s] %(levelname)s in %(module)s: %(message)s',
        }
    },
    'handlers': {
        'wsgi': {
            'class': 'logging.StreamHandler',
            'stream': 'ext://flask.logging.wsgi_errors_stream',
            'formatter': 'default'
        }
    },
    'root': {
        'level': 'INFO',
        'handlers': ['wsgi']
    }
})
logger = logging.getLogger(__name__)
app.register_blueprint(api_v1)
