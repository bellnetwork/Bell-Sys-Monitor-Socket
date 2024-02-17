import logging

def live_swap_space_monitoring(socketio, emit):
    @socketio.on('live_swap_space_monitoring_check')
    def swap_space_monitoring(data):
        swap_percent = data.get('swap_percent')
        logging.error(f'swap_percent: {swap_percent}')