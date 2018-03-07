# CSAW Diary
## Author

## Points
300
## Category
Pwn
## Description
After ten years, it is time to record some memories...
## Flag
`key{signness_oh_what_a_world_we_live_in}`
## Solution
`PoC_c1.py`
Challenge: It is a remote exploitation challenge focusing on a sign extension vulnerability leading to a buffer overflow.
## Setup
Distribute `fil_chal`
Test environment was on Ubuntu 12.04 LTS. Challenge should (will) run on Debian. Binary characteristics: No NX and Full RELRO, Privileges are dropped for UID, but not for GID. The challenge can be completed with or without ASLR. I will leave it up to you to decide.
## Notes
Hint: Take a look at how the length is used