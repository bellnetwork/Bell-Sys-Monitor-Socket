import logging

def live_network_usage(socketio, emit):
    @socketio.on('live_network_usage_check')
    def network_usage(data):
        network_usage_megabytes = data.get('network_usage_megabytes')
        logging.error(f'network_usage_megabytes: {network_usage_megabytes}')