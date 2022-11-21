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

## Implementation
The input to the program is received by the user from the keyboard. After that, the input is passed to a validation check, which accept:

* Only doubles or integers.
* Negative or positive numbers.
* The vectors must be equally sized.
* No special characters allowed.

For example, (0, -1.1, 2) and (1, 2, 3) is a valid input, but (a, 3, 4) and (1., .1, 5, 3) is not (not equally sized and contain illegal characters).

Additionally, two out of the five distance function uses the Minkowski distance, because:
* taxicabDistance = minkowskiDistance(P = 1)
* euclideanDistance = minkowskiDistance(P = 2)

We used the minkowskiDistance to receive P=2.

The Distances class contains all calculations regard to the algorithms, in addition to the print function, which presents the result of each calculation according to the order specified above.

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


