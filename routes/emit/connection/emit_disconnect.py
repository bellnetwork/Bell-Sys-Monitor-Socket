import logging


def accept_disconnection(socketio, emit):
    @socketio.on('disconnect')
    def handle_disconnect():
  
        logging.error("Client disconnected")
        emit('success', 'You are disconnected')
