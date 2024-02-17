import logging

def live_network_bandwidth_monitoring(socketio, emit):
    @socketio.on('live_network_bandwidth_monitoring_check')
    def network_bandwidth_monitoring(data):
        bytes_sent = data.get('bytes_sent')
        bytes_recv = data.get('bytes_recv')
        logging.error(f'bytes_sent: {bytes_sent}; bytes_recv: {bytes_recv}')