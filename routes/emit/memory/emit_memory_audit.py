import logging

def live_memory_audit(socketio, emit):
    @socketio.on('live_memory_audit_check')
    def memory_audit(data):
        logging.error(f'memory audit: {data}')