from flask import Flask
from flask_cors import CORS
from flask_socketio import SocketIO, emit
from flask_mail import Mail
from celery import Celery
from dotenv import load_dotenv
import redis, sys, os, logging, openai

sys.path.append('/path/to/your/project')

def create_app():
    # Load environment variables from .env file
    load_dotenv()
    
    app = Flask(__name__)
    app.config['DEBUG'] = True
    CORS(app, resources={r"/socket.io/*": {"origins": "*"}})
    socketio = SocketIO(app, cors_allowed_origins='*')
    logging.basicConfig(level=logging.DEBUG)
    app.config['SESSION_REDIS'] = redis.StrictRedis(host='localhost', port=6379, db=0, password='Your Password')

    # gunicorn_logger = logging.getLogger('gunicorn.error')
    # app.logger.handlers = gunicorn_logger.handlers
    # app.logger.setLevel(gunicorn_logger.level)
    app.secret_key = os.urandom(24).hex()
    logging.error(f"Secret key {app.secret_key} was generated.")

    redis_client = redis.StrictRedis(host='localhost', port=6379, db=0, decode_responses=True, password='Your Password')
    socketio = SocketIO(app, async_mode='threading')
    
    app.config['SESSION_PERMANENT'] = True  # Sessions are permanent, stored until explicitly cleared
    app.config['SESSION_USE_SIGNER'] = True  # Sign the session cookie for extra security
    app.config['HOSTNAME'] = os.environ.get('HOSTNAME')

    server_ip = 'Your server ip'
    server_id = 'Your server id'

    celery = Celery(app.import_name, broker=os.environ.get('CELERY_BROKER_URL'))

    return app, socketio, emit, redis_client, celery, server_ip, server_id
