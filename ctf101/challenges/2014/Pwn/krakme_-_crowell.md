# Krakme
## Author
Crowell
## Points
300
## Category
Pwn
## Description

## Flag
`flag{did you accidentally your entire kernel?}`
## Solution
File `exp.c` is a working local root exploit against it, just compile static and wget it to the vm to get root.
## Setup
It is a pwning challenge disguised as a crackme. There is an unchecked
`copy_from_user` that can be used to overwrite an index to an array of function pointers, and then trigger a call of a NULL pointer.
Launch with `./run.sh`, and qemu will listen on port 9999.
Give login information of csaw:csaw.
Root password is in run2.sh, but don't give that out!
Only distribute the .ko, not source, it should be simple enough to reverse.
Tell them that the device lives in /dev/krackme
Every user will get their own vm on every connect, so no need to worry about crashing or whatever. I give each vm 64 mb of ram, which should probably be a good amount. If it is too much or too little on the actual box, you can modify run2.sh.