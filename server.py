import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(('', 12345))
data_base = {}


def valid_address(address):
    if data_base.get(address):
        return True
    return False


while True:
    data, addr = s.recvfrom(144523463)
    message = str(data)
    if message[2].isnumeric() and int(message[2]) in range(1, 6) and valid_address(addr):
        print("Ok")
