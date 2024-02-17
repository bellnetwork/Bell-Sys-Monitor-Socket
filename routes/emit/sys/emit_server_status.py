import logging

def live_server_status(socketio, emit):
    @socketio.on('live_server_status_check')
    def server_status(data):
        new_status = data.get('new_status')
        logging.error(f'new_status: {new_status}')