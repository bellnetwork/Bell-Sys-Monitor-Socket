import logging

def get_check_attempts_logs(socketio, emit):
    @socketio.on('check_attempts_logs')
    def get_log_attempts(data):
        logging.error(f'got get_log_attempts: {get_log_attempts}')