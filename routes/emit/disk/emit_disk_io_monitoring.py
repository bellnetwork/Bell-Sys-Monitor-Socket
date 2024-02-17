import logging

def live_disk_io_monitoring(socketio, emit):
    @socketio.on('live_disk_io_monitoring_check')
    def server_disk_io_monitoring(data):
        read_bytes = data.get('read_bytes')
        write_bytes = data.get('write_bytes')
        logging.error(f'read: {read_bytes}, write: {write_bytes}')