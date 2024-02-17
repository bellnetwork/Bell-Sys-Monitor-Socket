import logging

def live_get_server_temperature(socketio, emit):
    @socketio.on('live_get_server_temperature_check')
    def get_server_temperature(data):
        total_temperature = data.get('total_temperature')
        logging.error(f'total_temperature: {total_temperature}')