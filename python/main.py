from flask import Flask
from flask_cors import CORS
from dotenv import load_dotenv
import os

from server.routes import movies


# get env variables and such
env_path = os.path.join(
    os.path.dirname(__file__),
    './.env'
)
load_dotenv(env_path)

app = Flask(__name__)  # instantiate server

CORS(app)
# routes
movies.serve(app)

app.run(
    port=os.getenv('BACKEND_PORT'),
    host='0.0.0.0',
)
