# Keygenme
## Author

## Points
400
## Category
Reversing
## Description

## Flag
`r3vers1ng_emul4t3d_cpuz_a1n7_h4rd!`
## Solution
```
solution/keygen
solution/keygen.cpp
solution/solver.rb
```
## Setup
Distribute `keygenme32.elf`
It might be better to give a 64 bit version of the elf instead? I don't know if giving teams with hex-rays an unfair advantage is better than giving a challenge that is maybe too hard?
To build the distributable, do `g++ *.cpp -o keygenme.elf"` for running the server, ruby does all the heavy lifting, but first you need to compile the keygen `g++ keygen.cpp -o keygen` and the keygen executable must live in the same dir as the server
## Notes
hint1: guessing = despiration = never solved
hint2: work your way up from the beginning. first solve the vm, then solve the keygen