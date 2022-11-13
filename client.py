"""
Title: Virtual Chat project for Networks course.
Authors: Yuval Arbel, Tal Mizrahi.
Date: 09/11/2022.
Version: V1.0
"""
import socket
import sys

# Getting the ip and server's port from the "Bat Kol".
server_ip = str(sys.argv[1])
server_port = int(sys.argv[2])
# If the port is not valid, exit the program.
if server_port not in range(0, 65536):
    exit(0)
# Opening  anew socket.
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# Running the client.
while True:
    # Getting the input from the keyboard.
    msg = input()
    # Sending a request to the server.
    s.sendto(msg.encode(), (server_ip, server_port))
    # Receiving a reply from the server.
    data, addr = s.recvfrom(1024)
    # Decoding the data from the server.
    server_reply = data.decode()
    # If the client requests to leave.
    if msg[0] == '4' and len(msg) == 1:
        # Closing the socket client request to leave the group.
        s.close()
        break
    # The client must get a reply, so if it's empty (no pending updates), continue.
    if server_reply == '':
        continue
    # Sorting thr reply.
    # server_reply = server_reply[2:-1] ????????
    server_reply = server_reply.split("\\n")
    # Printing the reply.
    for new_msg in server_reply:
        print(new_msg)