# Global Thermonuclar Cyberwar
## Author

## Premise
It's a Wargames-themed challenge, in 8086 real-mode assembly!
Launch CyberNukes to win... kinda

## Part 1:
### DEFCON 1
### Points
50
### Description
The year is 1981. Matthew Cyber-Broderick (You) finds a bizzare system. Understand it, and decrypt the secret ROM within.
### Category
Reverseing
### Flag
`flag{ok_you_decrypted_it_now_plz_pwn_it!}`
### Solution
Decrypt the payload, the flag is in the ROM
## Part 2:
### Global Thermonuclear Cyberwar
### Points
350
### Description
In this strange game, the only winning move is pwn.
### Category
Pwn
### Flag
`flag{c4n_4ny0n3_really_w1n_1n_cyb3rw4r?}`
### Solution
See `solve.py` for exploit

## Setup
For both parts, please distribute `cyberwar.rom`, which has the second flag scrubbed.
Run `server.rom` on QEMU with the VNC server exposed to the competitors.

The competitors should be told they can run the binary with:
    `qemu-system-i386 -drive format=raw,file=cyberwar.rom`
And a vnc server locally with:
    `qemu-system-i386 -vnc :0 -drive format=raw,file=cyberwar.rom`

To be nice to the competitors, note that the gdbstub in the latest QEMU on ubuntu has had issues for us. A known-good version of QEMU is:
    `2.10.1`## Topics Covered

