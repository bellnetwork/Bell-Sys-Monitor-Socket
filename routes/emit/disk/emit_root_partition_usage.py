import logging

def live_root_partition_usage(socketio, emit):
    @socketio.on('live_root_partition_usage_check')
    def root_partition_usage(data):
        logging.error(f'root partition usage: {data}')