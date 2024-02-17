import logging

def live_cpu_audit(socketio, emit):
    @socketio.on('live_cpu_audit_check')
    def server_cpu_audit(data):
        logging.error(f'cpu audit: {data}')