import socket
import sys

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_port = str(sys.argv[1])
s.bind(('', int(server_port)))

# data_base = {address : (name, [messages list])}
data_base = {}
# listed_members = [(address, [name]), (address, [name])]
listed_members = []


def in_data_base(address):
    if data_base.get(address):
        return True
    return False


# Sending to a new user message about all current members in the group.
def send_names(address):
    name_msg = ''
    for person in listed_members[::-1]:
        name_msg += person[1][0] + "\n"
    name_msg = name_msg[:-1]
    # Sending the message to the user.
    s.sendto(name_msg.encode(), address)


def add_to_database(name, address):
    # Checking if the dictionary is empty or not.
    if data_base:
        # If the database is not empty, add the notification about a new group member to all users.
        for key in data_base:
            data_base[key][1].append(name + " has joined")
        # Sending the new member a message about all current listed members.
        send_names(address)
    else:
        s.sendto(''.encode(), address)
    # Adding the new user to the database.
    data_base[address] = ([name], [])
    listed_members.append((address, [name]))


# Sending to all group members a message from a user.
def send_message_user(sorted_message, address):
    # Getting The sender's name.
    sender_name = data_base[address][0][0]
    # appending to all group member the new message to the messages list.
    for key in data_base:
        # all user's, except the ine who sent the message.
        if key != address:
            data_base[key][1].append(sender_name + ": " + sorted_message)


# Changing the name of the user and updating all other group members.
def change_name(new_name, address):
    # Saving the old name of the user.
    old_name = data_base[address][0][0]
    # Updating all users about the change.
    for key in data_base:
        # Add the message to all group members except the user.
        if key != address:
            data_base[key][1].append(old_name + " changed his name to " + new_name)
    # Changing the user's name.
    for person in listed_members:
        if person[0] == address:
            person[1][0] = new_name
    data_base[address][0][0] = new_name


# Removing a user from the database and updating all current group members.
def leave_group(address):
    # Saving the user's name.
    leaving_user_name = data_base[address][0][0]
    # Deleting the user.
    data_base.pop(address)
    # Updating all current group members.
    for key in data_base:
        data_base[key][1].append(leaving_user_name + " has left the group")
    # Removing the person from the member's list
    for person in listed_members:
        if person[0] == address:
            listed_members.remove(person)
            break


# Update a specific client with all the saved message he missed.
def update_me(address):
    # Init an empty message.
    all_msg = ''

    # Appending all the saved message to one string.
    for msg in data_base[address][1]:
        # Add the message with \n.
        all_msg = all_msg + msg + "\n"

    # Remove the last \n from the complete message.
    all_msg = all_msg[:-1]
    # Sending the complete message to the client.
    s.sendto(all_msg.encode(), address)
    data_base[address][1].clear()


# Indicate the client request and execute his request.
def switch(full_msg, address):
    command_num = int(full_msg[2])
    sorted_message = full_msg[4:-1]
    # "Switch case"
    match command_num:
        # Fulfill the client request to join the group.
        case 1:
            add_to_database(sorted_message, address)
            return True
        # Fulfill the client request to send a message to the group.
        case 2:
            update_me(address)
            send_message_user(sorted_message, address)
            return True
        # Fulfill the client request to change is name
        case 3:
            update_me(address)
            change_name(sorted_message, address)
            return True
        # Fulfill the client request to leave the group.
        case 4:
            update_me(address)
            leave_group(address)
            return True
        case 5:
            update_me(address)
            return True
        # The default case when is request is not legal.
        case _:
            return False


while True:
    # DEleteeeee
    print(data_base)

    # Receive data from everyone.
    data, addr = s.recvfrom(1024)
    # Store the data in a new string.
    message = str(data)
    # If the request is not by format or not in the manu range, return an error message.
    if not message[2].isnumeric() or not int(message[2]) in range(1, 6):
        s.sendto(str(False).encode(), addr)
        continue
    # if the request is to join the group, but the user is already in it, return error.
    if int(message[2]) == 1 and in_data_base(addr):
        s.sendto(str(False).encode(), addr)
        continue
    # If the request is to preform an action by a nonmember of the group (except joining the group), return error.
    if not in_data_base(addr) and int(message[2]) != 1:
        s.sendto(str(False).encode(), addr)
        continue
    # If the request is valid, preform an action.
    if not switch(message, addr):
        s.sendto(str(False).encode(), addr)
        continue
