import logging

def live_network_latency_packet_loss(socketio, emit):
    @socketio.on('live_network_latency_packet_loss_check')
    def network_latency_packet_loss(data):
        packet_loss = data.get('packet_loss')
        logging.error(f'packet_loss: {packet_loss}')