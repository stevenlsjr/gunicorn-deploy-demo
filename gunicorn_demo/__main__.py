from argparse import ArgumentParser
from .quart.asgi import app

parser = ArgumentParser()
parser.add_argument('--port', '-p', type=int, help='dev server port', default=5000)
parser.add_argument('--host', '-h', type=str, help='dev server host', default='localhost')
args = parser.parse_args()

app.run(host=args.host, port=args.port)