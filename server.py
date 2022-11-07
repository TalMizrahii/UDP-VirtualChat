import socket
import sys

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_port = str(sys.argv[1])

s.bind(('', int(server_port)))
data_base = {}


def valid_address(address):
    if data_base.get(address):
        return True
    return False


while True:
    data, addr = s.recvfrom(144523463)
    message = str(data)
    if message[2].isnumeric() and int(message[2]) in range(1, 6):
        print("Ok valid")
        s.sendto(str(True).encode(), addr)
        if valid_address(addr):
            print("ok name")
            s.sendto(str(True).encode(), addr)

    s.sendto(str(False).encode(), addr)
