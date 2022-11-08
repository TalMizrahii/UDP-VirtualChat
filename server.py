import socket
import sys

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_port = str(sys.argv[1])

s.bind(('', int(server_port)))

# data_base = {address : (name, [messages list])}
data_base = {}


def in_data_base(address):
    if data_base.get(address):
        return True
    return False


def add_to_database(name, address):
    # Checking if the dictionary is empty or not. If it is, adding the new member to it.
    if not data_base:
        data_base[address] = (name, [])
        return True

    # If the database is not empty, add the notification about a new group member to all users.
    for key in data_base:
        data_base[key].get(1).append(name + "has joined")
        # Sending the new member a message about all current listed members.
        s.sendto(data_base[key].get(0).encode(), address)


def switch(full_msg, address):
    command_num = int(message[2])
    sorted_message = message[2:]
    if command_num == 1:
        return add_to_database(sorted_message, address)
    elif command_num == 2:
        return send_message_user()
    elif command_num == 3:
        return change_name()
    elif command_num == 4:
        return leave_group()
    elif command_num == 5:
        return update_me()
    return False


def switch1(full_msg, address):
    command_num = int(message[2])
    sorted_message = message[2:]
    match command_num:
        case 1:
            return add_to_database(sorted_message, address)
        case 2:
            return send_message_user()
        case 3:
            return change_name()
        case 4:
            return leave_group()
        case 5:
            return update_me()
        case _:
            return False


while True:
    data, addr = s.recvfrom(1024)
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
    if not switch(message, addr):
        s.sendto(str(False).encode(), addr)
        continue
