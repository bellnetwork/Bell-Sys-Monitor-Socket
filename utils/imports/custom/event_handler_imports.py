# Import all event handlers

# Connection Events
from routes.emit.connection.emit_connect import accept_connection, accept_reconnection, welcome_message
from routes.emit.connection.emit_disconnect import accept_disconnection

# Security Logs
from routes.emit.security.logs.emit_check_attempt_log import get_check_attempts_logs

# CPU Events
from routes.emit.cpu.emit_check_cpu_audit import live_cpu_audit
from routes.emit.cpu.emit_check_cpu_usage import live_cpu_usage

# Disk Events
from routes.emit.disk.emit_disk_io_monitoring import live_disk_io_monitoring
from routes.emit.disk.emit_disk_usag import live_disk_usage
from routes.emit.disk.emit_max_partition_usage import live_max_partition_usage
from routes.emit.disk.emit_root_partition_usage import live_root_partition_usage

# Memory Events
from routes.emit.memory.emit_memory_audit import live_memory_audit
from routes.emit.memory.emit_memory_usage import live_memory_usage

# Network Events
from routes.emit.network.emit_user_network_status import check_user_network
from routes.emit.network.emit_network_bandwidth_monitoring import live_network_bandwidth_monitoring
from routes.emit.network.emit_network_connections import live_network_connections
from routes.emit.network.emit_network_latency_packet_loss import live_network_latency_packet_loss
from routes.emit.network.emit_network_usage import live_network_usage

# Swap Space Monitoring
from routes.emit.swap.emit_swap_space_monitoring import live_swap_space_monitoring

# System Events
from routes.emit.sys.emit_server_status import live_server_status
from routes.emit.sys.emit_get_server_temperature import live_get_server_temperature
from routes.emit.sys.emit_system_uptime import live_system_uptime

# PID Monitoring
from routes.emit.pid.emit_pid_monitoring import live_pid_monitoring

# System information
from routes.emit.sys.emit_server_information import fetch_server_information