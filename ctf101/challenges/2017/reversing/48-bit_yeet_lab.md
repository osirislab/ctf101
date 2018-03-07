# 48-bit bomb lab
## Author

## Points
300
## Category
Reversing
## Description
what, you've never seen an x86-48 bomb lab before?
Its just another bomb lab. 
NOTE: The flag in the binary is a placeholder. Please run against the remote system to get the real flag!
## Flag
`flag{turns_out_heavens_gate_works_on_linux_too_yote}`
## Solution
[solver.py](solver.py)
## Premise
This is a reversing challenge that abuses the ability to define a segment selector in certain far jmp instructions to obfuscate an otherwise fairly straightworward bomb-lab style challenge.
Teams are expected to reverse each phase of the bomb lab and provide an input that will allow them to continue to the next phase until they can reach flag printing code.
Phase 1 involves a constant global 32 byte string. the program takes user input into a buffer, then jumps to 64 bit execution and loads the whole string into rax, rbx, rcx, and rdx. it compares rax, rbx, and rdx to the proper offsets into the user to see if they input the same string, but rcx gets bswapped in 64 bit, then a compares ecx against the third chunk of the input string in 32 bit execution mode.
Phase 2
release yeetlab\_release