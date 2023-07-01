import socket

SERVER_IP_ADDRESS = 'localhost'

DOMAIN_NAME = 'www.yahoo.com'

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

client_socket.sendto(DOMAIN_NAME.encode(), (SERVER_IP_ADDRESS, 53))

response, _ = client_socket.recvfrom(1024)

ip_address = response.decode()

print(f"Alamat IP dari {DOMAIN_NAME} adalah {ip_address}")