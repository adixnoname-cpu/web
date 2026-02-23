
from flask import Flask
import os
from flask_socketio import SocketIO
from datetime import timedelta

NOWPAYMENTS_BASE_URL = "https://api.nowpayments.io/v1"

app = Flask(__name__, template_folder='../templates', static_folder='../static')

app.secret_key = os.urandom(24)
app.config['SOCKETIO_ASYNC_MODE'] = 'threading'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['UPLOADS_FOLDER'] = 'static/uploads'
app.config['SOURCES_FOLDER'] = 'static/sources'
app.config['MAX_CONTENT_LENGTH'] = 100 * 1024 * 1024
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = timedelta(minutes=1)
app.config['HTML_VERSION'] = 2.2

socketio = SocketIO(app, cors_allowed_origins="*")