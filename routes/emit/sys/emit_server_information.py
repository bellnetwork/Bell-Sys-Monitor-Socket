import logging

def fetch_server_information(socketio, emit):
    @socketio.on('server_information_check')
    def server_information(data):
        # Extract server information from the data
        server_machine = data.get('server_machine', 'Unknown')
        server_node = data.get('server_node', 'Unknown')
        server_platform = data.get('server_platform', 'Unknown')
        server_processor = data.get('server_processor', 'Unknown')
        python_version = data.get('python_version', 'Unknown')
        server_release = data.get('server_release', 'Unknown')
        server_uname = data.get('server_uname', 'Unknown')

        # Log the server information
        server_info = (
            f"Server Machine: {server_machine}; Node: {server_node}\n"
            f"Platform: {server_platform}; Processor: {server_processor}\n"
            f"Python Version: {python_version}; Release: {server_release}\n"
            f"Uname: {server_uname}"
        )
        
        logging.error("Server Information:\n" + server_info)