import time, asyncio

async def main_start():
    # Send message when script starts
    server_name = subprocess.check_output("hostname", shell=True).decode().strip()
    if server_name is not None:
        await sio.emit(f"Script started on (Server: {server_name}) - users connected to the server:")
        connected_users = subprocess.check_output("who", shell=True).decode()
        await sio.emit(connected_users)
    
    while True:
        await asyncio.gather(
            check_network_status(),
            check_logs(), # Call the new function here
        )
        time.sleep(2) # Check every 2 seconds