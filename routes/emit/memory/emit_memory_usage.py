import logging

def live_memory_usage(socketio, emit):
    @socketio.on('live_memory_usage_check')
    def memory_usage(data):
        logging.error(f'memory usage: {data}')