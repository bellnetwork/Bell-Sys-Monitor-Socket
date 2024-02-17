import logging

def live_max_partition_usage(socketio, emit):
    @socketio.on('live_max_partition_usage_check')
    def max_partition_usage(data):
        max_partition_usage = data.get('max_partition_usage')
        logging.error(f'max partit. usage: {max_partition_usage}')