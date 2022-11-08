import socket
import sys

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_port = str(sys.argv[1])

s.bind(('', int(server_port)))
data_base = {}


def in_data_base(address):
    if data_base.get(address):
        return True
    return False


while True:
    data, addr = s.recvfrom(144523463)
    message = str(data)
    if not message[2].isnumeric() or not int(message[2]) in range(1, 6):
        s.sendto(str(False).encode(), addr)
        continue
    if int(message[2]) == 1 and in_data_base(addr):
        s.sendto(str(False).encode(), addr)
        continue
    if not in_data_base(addr) and int(message[2]) != 1:
        s.sendto(str(False).encode(), addr)
        continue
