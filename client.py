import socket


s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.sendto(b'Tal Mizrahi 206960890, Yuval Arbel 206945107', ('10.0.2.15', 12345))

data, addr = s.recvfrom(1024)
print(str(data), addr)

s.close()