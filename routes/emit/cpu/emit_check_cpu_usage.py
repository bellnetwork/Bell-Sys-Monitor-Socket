import logging

def live_cpu_usage(socketio, emit):
    @socketio.on('live_cpu_usage_check')
    def server_cpu_usage(data):
        logging.error(f'cpu usage: {data}')