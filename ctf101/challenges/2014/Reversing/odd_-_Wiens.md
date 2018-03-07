# Odd
## Author
Wiens
## Points
200
## Category
Reversing
## Description

## Flag
`flag{DynamicAnalysisForLife}`
## Solution
the elf is a modified version of the teensy elf [http://www.muppetlabs.com/~breadbox/software/tiny/teensy.html](http://www.muppetlabs.com/~breadbox/software/tiny/teensy.html) with a relatively simple self-xor-decryption loop using some floating point values. Radare has it really easy, can literally just load it up and step through it until the xor loop is done, and look at the memory pointed to by EDX. Other debuggers don't fare so well with the corrupted ELF headers. [http://dustri.org/b/screwing-elf-header-for-fun-and-profit.html](http://dustri.org/b/screwing-elf-header-for-fun-and-profit.html)
## Setup
Distribute `odd`