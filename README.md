# Virtual Chat
<h4 align="center">This github repository is for the assignments given in Computer Networks course, Bar Ilan University.


<p align="center">
  <a href="#description">Description</a> •
  <a href="#implementation">Implementation</a> •
  <a href="#dependencies">Dependencies</a> •
  <a href="#installing-and-executing">Installing And Executing</a> •
  <a href="#authors">Authors</a> 
</p>

## Description

This program represents a chat group users can join, write messages and change their names. 
No parallelism performed in the program, so only when a user interacts with the Server, he receives all updates sent to him since he joined the group.

The Server's purpose is to manage the group's data, store current group members and their names, store pending messages, and be responsible for checking if the client sent a message in the correct format.

The Client receives the Server's port number and IP, and the Server the port number as system arguments.

commends:
* To join the group: 1 [name]
* To send a message: 2 [message]
* To change my name: 3 [new name]
* to 
## Implementation

### The Client module
The Client receives the Server's port and id numbers as system arguments.

He connects to the server via "sendto()" method, and sends him a message.
If the Client wants to exit the program (command 4)

## Dependencies

* The program tested for linux machines.
* Compiled with g++.

## Installing And Executing

To clone and run this application, you'll need [Git](https://git-scm.com) installed on your computer. From your command line:

```bash
# Clone this repository.
$ git clone https://github.com/TalMizrahii/AP1Project

# Go into the repository.
$ cd AP1Project

# Compile using makefile.
$ make
```

```bash
# Run the program on Linux:
$ ./a.out
```

```bash
# Run the program on Windows:
$ a.out
```

```bash
# After running, clean all unnecessary files.
$ make clean
```

## Authors
* [@Yuval Arbel](https://github.com/YuvalArbel1)
* [@Tal Mizrahi](https://github.com/TalMizrahii)


