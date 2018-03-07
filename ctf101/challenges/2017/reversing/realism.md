# realism
## Author

## Points
400
## Category
Reversing
## Description
Did you know that x86 is really old? I found a really old Master Boot Record that I thought was quite interesting! At least, I think it's really old...
## Flag
`flag{4r3alz_m0d3_y0}`
## Solution
[solve.py](solve.py)
## Premise
x86 MBR that uses SSE instructions >:)
## Setup
Run cmd (please give them this): 
`qemu-system-i386 -drive format=raw,file=main.bin`