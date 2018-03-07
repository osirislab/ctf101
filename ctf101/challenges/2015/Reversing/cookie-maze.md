# cookie_maze

## Author
Bohan
## Category
Reversing
## Points
400
## Description
Ever feel like a rat trapped in a maze? There's a flag somewhere in this binary but I just can't seem to find it.
If you don't have a OS X box you can ssh here after requesting it.
ssh 0.tcp.ngrok.io -p 47136
~Update new port is 47136
Hints:
- <https://www.mikeash.com/pyblog/friday-qa-2013-01-11-mach-exception-handlers.html>
- <https://github.com/gdbinit/readmem>
- If an exception handler returns success(0) the binary continues executing even if the exception was not handled if it returns failure(5) it always exits

## Flag
`flag{Qi29a85i52aA5i5Ea15i81aM5i5Qa18i51aY5}`
## Solution

## Setup
Distribute `cookie_maze_8d8023f8f7c38181e8abd9c5c70d527b`