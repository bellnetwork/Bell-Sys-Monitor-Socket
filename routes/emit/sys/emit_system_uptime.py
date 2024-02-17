import logging

def live_system_uptime(socketio, emit):
    @socketio.on('live_system_uptime_check')
    def system_uptime(data):
        server_uptime = data.get('server_uptime')
        logging.error(f'server_uptime: {server_uptime}')