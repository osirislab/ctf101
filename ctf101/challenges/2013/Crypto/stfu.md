# stfu
## Author

## Points
100
## Category
Crypto
## Description
Oh no! How will we ever recover the flag, now that it's stored in a Secure Test File Unit?
## Flag
`STFU_THIS_CHALLENGE_WAS_TOTALLY_NOT_LAME`
## Solution
Copy the LFSR algorithm from the binary (Googling for code should get you similar code, if you can't)
* Read the seed, tap, and skip values out of flag.stfu (bytes 4-16)
* Seed your LFSR with the seed and tap values and skip N states forward (where N is the skip value)
* For each next state in the LFSR, XOR it with the next 4 bytes of the file (starting after the 16-byte header)
* Strip off the header, view in a text editor
* (Side note: This challenge should actually be solvable by patching the binary because it's an XOR)

## Setup
