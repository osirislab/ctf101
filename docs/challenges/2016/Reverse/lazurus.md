# Lazurus
## Author

## Points
300
## Category
Reversing
## Description
Lost but not forgotten, today we breathe new life into a peculiar world.
## Flag
`flag{exp3ct_a_w1nd0ws_p0six_pwn4ble_f0r_CSAW_2017_f1nals}`
## Solution
Simply run the executable with the correct flag as the first argument. You will need the SUA Subsystem enabled.
## Notes
This is a reversing challenge that is compiled for the old, Windows POSIX Subsystem.
To complete this challenge, it is expected that teams are going to have to have to
actually get the executable running in the SUA 4.0 (Subsystem for Unix Applications)
environment. This subsystem was shipped as a part of Windows from NT 4.0 - Windows 8.

The challenge uses fingerprints of the SUA environment to create/check the flag. It
is unlikely that teams will be able to solve the challenge (at least relatively easily)
without enabling the SUA subsystem on a Windows machine.

The reversing / flag logic is by no means complex. It is simply a byte xor of an
'encrypted' flag and the collected environmental fingerprints. There is some basic
obfuscation and anti-hexrays, along with some confusing code chunks to slowdown the
finalists and increase the difficulty of the challenge. Once they understand that
some chunks of code are just opaque predicates, they'll probably solve it pretty quickly.

Other tidbits:
- I developed the challenge on an x86 Windows 7 Enterprise VM
- The challenge is 'environmentally keyed' to the SUA 4.0 Subsystem. It may not verify the flag properly on older versions.
- It might be a bit tricky for teams to debug (good!) because the launch process of POSIX executables is indirect