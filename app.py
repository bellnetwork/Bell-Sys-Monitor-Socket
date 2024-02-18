# To run, follow these steps:
# Start debug mode:
# cd /path/to/your/project && python3 -m app
# systemctl start bell_sys_monitor_socket
# systemctl restart bell_sys_monitor_socket
# systemctl stop bell_sys_monitor_socket
# systemctl status bell_sys_monitor_socket

from utils.sys.config.flask_config import create_app
from utils.imports.emit.import_routes import setup_all_socketio_events

app, socketio, emit = create_app()

# Call the function to register all event handlers
setup_all_socketio_events(socketio, emit)

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=9374)
