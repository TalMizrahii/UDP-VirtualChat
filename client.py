import socket
import sys

server_ip = str(sys.argv[1])
server_port = int(sys.argv[2])

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
    msg = input()
    s.sendto(msg.encode(), (server_ip, server_port))
    data, addr = s.recvfrom(1024)
    server_reply = str(data)
    if msg[0] == 4:
        break
    if server_reply == str(b''):
        continue
    server_reply = server_reply[2:-1]
    server_reply = server_reply.split("\\n")

    for new_msg in server_reply:
        print(new_msg)

