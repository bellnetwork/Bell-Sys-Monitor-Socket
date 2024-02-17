import logging


def accept_connection(socketio, emit):
    @socketio.on('connect')
    def handle_connect(data):
        if not data:
            emit('error', 'There was an error.')
            
        logging.error("Client connected")
        emit('success', 'You are connected')
        
        
def accept_reconnection(socketio, emit):
    @socketio.on('reconnect')
    def handle_disconnect():
  
        logging.error("Client reconnected")
        emit('success', 'You are reconnected')
        
        
def welcome_message(socketio, emit):
    @socketio.on('message')
    def handle_message(message):
        logging.error(f'Received message: {message}')
        emit('response', 'Message received on server')