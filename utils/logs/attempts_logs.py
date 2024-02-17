import os

async def check_attempts_logs(sio):
    """Checks the system logs for hacking attempts and successful SSH logins."""
    log_file = '/var/log/auth.log' # Update the path to the system log file
    cmd = f"grep 'authentication failure' {log_file}"
    output = os.popen(cmd).read()
    if output:
        await sio.emit(f"Hacking attempt detected on {server_name}:\n{output}")
    
    cmd = f"grep 'sshd.*Accepted' {log_file}" # Search for successful SSH logins
    output = os.popen(cmd).read()
    if output:
        for line in output.split('\n'):
            if line:
                words = line.split()
                user = words[8] # Extract the username from the log entry
                ip = words[10].split(':')[0] # Extract the IP address from the log entry
                await sio.emit(f"Successful SSH login by user {user} ({ip})")
