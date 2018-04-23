# FIREWALL
## Author

## Points
400
## Category
Pwn
## Description
After rummaging around the network for a few days, the IT department was able to
find the dust covered machine hosting the hospital's firewall. We don't have budget
to update it... so just take a quick look and tell us it's good for another year. 
## Flag
`flag{w3_f3ll_pr3tty_f4r_d0wn_th3_w1nd0ws_r4bb1t_h0le_huh}`
## Solution
[exploit.py](solution/exploit.py)
## Premise
This is an exploitation challenge that is compiled for the old, Windows POSIX Subsystem.

To complete this challenge, it is expected that teams are going to have to have to
actually get the executable running in the SUA 4.0 (Subsystem for Unix Applications)
environment. This subsystem was shipped as a part of Windows from NT 4.0 - Windows 8.

The challenge uses fingerprints of the SUA environment to generate the initial 'token'
check. This is an attempt to deter teams from solving it statically / bruteforcing
against the server and ensure that they can debug the challenge locally.

Firewall is modeled to be a memory corruption challenge, but does not (intentionally)
give the players a means to hijack control flow. There is also some light obfuscation. 

The expected solution will leak a memory address of a static string and then
overwrite said address (in a string table) with the address of the flag (which
is read into memory during initialization).

IMO as an exploitation challenge, this is not *hard*. But lots of tidbits / the weird
environment ticks it up from a 300pt challenge, to 400pt.

Other tidbits:
- I developed the challenge on an x86 Windows 7 Enterprise VM
- The expected solution (an exploit) may fail 50/50 due to the leak failing (ASLR dependent)
- There is a red herring / buffer overflow that is not intended to be exploitable :')
## Topics Covered

- [Dissassemblers](/reverse-engineering/what-are-disassemblers/)
