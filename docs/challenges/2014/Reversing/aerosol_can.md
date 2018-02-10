# Aerosol Can
## Author
Dinaburg
## Points
500
## Category
Reversing
## Description

## Flag
`flag{18ea6024aba10c2777703151f5bd1f58}`
## Solution

## Setup

## Notes
The original program (csaw.c) is a simple "crackme" style key checker.
The original has been compiled to x86 using GCC. The x86 was converted to LLVM via mcsema [https://github.com/trailofbits/mcsema](https://github.com/trailofbits/mcsema). Then the LLVM was emited back as x86 code. The challenge is to reverse this translated and re-emitted binary.
Writing the challenge took a bit longer than expected since it triggered a few bugs in mcsema :). The binary is called aersol_can because I was listening to [https://www.youtube.com/watch?v=pzZK4al4dvA](https://www.youtube.com/watch?v=pzZK4al4dvA) for a lot of its creation.