import socket
import sys

server_ip = str(sys.argv[1])
server_port = int(sys.argv[2])


s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
    msg = input()
    s.sendto(msg.encode(), (server_ip, server_port))
    data, addr = s.recvfrom(1024)

    if not bool(data):
        print("Illegal request")
        continue
    print(str(data))
    if msg[0] == 4:
        break

