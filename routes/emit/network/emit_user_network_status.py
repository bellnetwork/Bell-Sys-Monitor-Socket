import logging

def check_user_network(socketio, emit):
    @socketio.on('network_status_update')
    def main_network_status(data):
        logging.error(f'got data: {data}')