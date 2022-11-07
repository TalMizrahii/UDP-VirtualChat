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
    if message[2].isnumeric() and  isinstance(float(message[2]), int) and int(message[2]) in range(1, 6):
        print("Ok valid")
    if valid_address(addr):
        print("ok name")
