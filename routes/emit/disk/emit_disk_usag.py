import logging

def live_disk_usage(socketio, emit):
    @socketio.on('live_disk_usage_check')
    def server_disk_usage(data):
        logging.error(f'disk usage: {data}')