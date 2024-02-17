import logging

def live_pid_monitoring(socketio, emit):
    @socketio.on('live_pid_monitoring_check')
    def pid_monitoring(data):
        pid = data.get('pid')
        name = data.get('name')
        uptime = data.get('uptime')

        # Log the PID information
        logging.error(f"PID: {pid}, Name: {name}, Uptime: {uptime}")