# Import the event handler imports module
from utils.imports.custom import event_handler_imports as ehi

def setup_all_socketio_events(socketio, emit):
    # Connection events
    ehi.accept_connection(socketio, emit)
    ehi.accept_disconnection(socketio, emit)
    ehi.accept_reconnection(socketio, emit)
    ehi.welcome_message(socketio, emit)
    
    # Security logs
    ehi.get_check_attempts_logs(socketio, emit)

    # CPU events
    ehi.live_cpu_audit(socketio, emit)
    ehi.live_cpu_usage(socketio, emit)

    # Disk events
    ehi.live_disk_io_monitoring(socketio, emit)
    ehi.live_disk_usage(socketio, emit)
    ehi.live_max_partition_usage(socketio, emit)
    ehi.live_root_partition_usage(socketio, emit)

    # Memory events
    ehi.live_memory_audit(socketio, emit)
    ehi.live_memory_usage(socketio, emit)

    # Network events
    ehi.check_user_network(socketio, emit)
    ehi.live_network_bandwidth_monitoring(socketio, emit)
    ehi.live_network_connections(socketio, emit)
    ehi.live_network_latency_packet_loss(socketio, emit)
    ehi.live_network_usage(socketio, emit)

    # Swap space monitoring
    ehi.live_swap_space_monitoring(socketio, emit)

    # Server status and temperature
    ehi.live_server_status(socketio, emit)
    ehi.live_get_server_temperature(socketio, emit)
    ehi.live_system_uptime(socketio, emit)

    # PID monitoring
    ehi.live_pid_monitoring(socketio, emit)

    # System information
    ehi.fetch_server_information(socketio, emit)