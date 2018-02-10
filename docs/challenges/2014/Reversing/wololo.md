# wololo
## Author
Stortz
## Points
300
## Category
Reversing
## Description
Can you pass all the checks?
## Flag
`flag{Small Group of Helpless Villages? Call in the Trebuchets.}`
## Solution
`/solution/wololo_x.py`
`/solution/x.bin`
## Setup
Distribute `wololo.lst.xz-41f5fa412b925fda7e08ddb9bd25d5e863ac78ec`
To run:
- sudo ./wololo-server
- The server listens on TCP port 2510 and requires the user "wololo".
- It drops from root to wololo on every connection.

The server component needs to be compiled on the host system. A make file is provided. The service doesn't have any dependencies to worry about. The service needs the 'wololo' user and should be launched as root.
The question text will need to provide the ip address, port, and listing file.
## Notes
wololo is a static revserse engineering challenge. The binary is shipped as an armv7 disassembly file. The players are expected to reverse engineer it and develop a compatible binary file that passes all its tests.
Challenge submission is handled by a custom unreleased service that provides an example "exploit" script on connection.
Wololo is a custom database format compiled to armv7. The challenge is distrobuted as an IDA arm disassembly listing (.list) The goal is to create a database that matches the specification implemented in wololo to pass all the checks.
A seperate server component exists that does the checks on the network. If they all pass, then the key is printed back on the socket.