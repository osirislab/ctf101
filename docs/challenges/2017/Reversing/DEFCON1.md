# DEFCON1
*Part 1 of Global Thermonuclear Cyberwar.*
## Author

## Category
Reversing
## Points
50
## Description
The year is 1981. Matthew Cyber-Broderick (You) finds a bizzare system. Understand it, and decrypt the secret ROM within.
Run with qemu-system-i386 -drive format=raw,file=cyberwar.rom

NOTE: The gdbstub in the latest QEMU on ubuntu gave us issues. A known-good version of QEMU is 2.10.1
## Flag
`flag{ok_you_decrypted_it_now_plz_pwn_it!}`
## Solution
Decrypt the payload, the flag is in the ROM
## Setup
Run `server.rom` on QEMU with the VNC server exposed to the competitors.

The competitors should be told they can run the binary with:
`qemu-system-i386 -drive format=raw,file=cyberwar.rom`
And a vnc server locally with:
`qemu-system-i386 -vnc :0 -drive format=raw,file=cyberwar.rom`

To be nice to the competitors, note that the gdbstub in the latest QEMU on ubuntu has had issues for us. A known-good version of QEMU is:
`2.10.1`