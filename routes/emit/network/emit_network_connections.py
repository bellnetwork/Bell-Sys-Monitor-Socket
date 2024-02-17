import logging

def live_network_connections(socketio, emit):
    @socketio.on('live_network_connections_check')
    def network_connections(data):
        network_connections = data.get('network_connections')
        logging.error(f'network_connections: {network_connections}')