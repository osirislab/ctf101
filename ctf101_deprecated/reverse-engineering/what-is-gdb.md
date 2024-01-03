# The GNU Debugger (GDB)

The GNU Debugger or GDB is a powerful debugger which allows for step-by-step execution of a program. It can be used to trace program execution and is an important part of any reverse engineering toolkit.

## Vanilla GDB

GDB without any modifications is unintuitive and obscures a lot of useful information. The plug-in [pwndb](https://github.com/pwndbg/pwndbg) solves a lot of these problems and makes for a much more pleasant experience. But if you are constrained and *have* to use vanilla gdb, here are several things to make your life easier.

### Starting GDB

To execute GBD and attach it to a program simply run `gdb [program]`

### Disassembly

`(gdb) disassemble [address/symbol]` will display the disassembly for that function/frame

GDB will autocomplete functions, so saying `(gdb) disas main` suffices if you'd like to see the disassembly of main

### View Disassembly During Execution

Another handy thing to see while stepping through a program is the disassembly of nearby instructions:

`(gdb) display/[# of instructions]i $pc [± offset]`

* `display` shows data with each step
* `/[#]i` shows how much data in the format i for instruction 
* `$pc` means the pc, program counter, register
* `[± offset]` allows you to specify how you would like the data offset from the current instruction

#### Example Usage

`(gdb) display/10i $pc - 0x5`

This command will show 10 instructions on screen with an offset from the next instruction of 5, giving us this display:

```
   0x8048535 <main+6>:	lock pushl -0x4(%ecx)
   0x8048539 <main+10>:	push   %ebp
=> 0x804853a <main+11>:	mov    %esp,%ebp
   0x804853c <main+13>:	push   %ecx
   0x804853d <main+14>:	sub    $0x14,%esp
   0x8048540 <main+17>:	sub    $0xc,%esp
   0x8048543 <main+20>:	push   $0x400
   0x8048548 <main+25>:	call   0x80483a0 <malloc@plt>
   0x804854d <main+30>:	add    $0x10,%esp
   0x8048550 <main+33>:	sub    $0xc,%esp
```

#### Deleting Views

If for whatever reason, a view no long suits your needs simply call `(gdb) info display` which will give you a list of active displays:

```
Auto-display expressions now in effect:
Num Enb Expression
1:   y  /10bi $pc-0x5
```

Then simply execute `(gdb) delete display 1` and your execution will resume without the display.

### Registers

In order to view the state of registers with vanilla gdb, you need to run the command `info registers` which will display the state of all the registers:

```
eax            0xf77a6ddc	-142971428
ecx            0xffe06b10	-2069744
edx            0xffe06b34	-2069708
ebx            0x0	0
esp            0xffe06af8	0xffe06af8
ebp            0x0	0x0
esi            0xf77a5000	-142979072
edi            0xf77a5000	-142979072
eip            0x804853a	0x804853a <main+11>
eflags         0x286	[ PF SF IF ]
cs             0x23	35
ss             0x2b	43
ds             0x2b	43
es             0x2b	43
fs             0x0	0
gs             0x63	99
```

If you simply would like to see the contents of a single register, the notation `x/x $[register]` where:

* `x/x` means display the address in hex notation
* `$[register]` is the register code such as eax, rax, etc.


## Pwndbg

These commands work with vanilla gdb as well.

### Setting Breakpoints

Setting breakpoints in GDB uses the format `b*[Address/Symbol]`

#### Example Usage

- `(gdb) b*main`: Break at the start
- `(gdb) b*0x804854d`: Break at 0x804854d
- `(gdb) b*0x804854d-0x100`: Break at 0x804844d

#### Deleting Breakpoints

As before, in order to delete a view, you can list the available breakpoints using `(gdb) info breakpoints` (don't forget about GDB's autocomplete, you don't always need to type out every command!) which will display all breakpoints:

```
Num     Type           Disp Enb Address    What
1       breakpoint     keep y   0x0804852f <main>
3       breakpoint     keep y   0x0804864d <__libc_csu_init+61>
```

Then simply execute `(gdb) delete 1`

!!!note
	GDB creates breakpoints chronologically and does NOT reuse numbers.

### Stepping

What good is a debugger if you can't control where you are going? In order to begin execution of a program, use the command `r [arguments]` similar to how if you ran it with dot-slash notation you would execute it `./program [arguments]`. In this case the program will run normally and if no breakpoints are set, you will execute normally. If you have breakpoints set, you will stop at that instruction.

- `(gdb) continue [# of breakpoints]`: Resumes the execution of the program until it finishes or until another breakpoint is hit (shorthand `c`)
- `(gdb) step[# of instructions]`: Steps into an instruction the specified number of times, default is 1 (shorthand `s`)
- `(gdb) next instruction [# of instructions]`: Steps over an instruction meaning it will not delve into called functions (shorthand `ni`)
- `(gdb) finish`: Finishes a function and breaks after it gets returned (shorthand `fin`)

### Examining

Examining data in GDB is also very useful for seeing how the program is affecting data. The notation may seem complex at first, but it is flexible and provides powerful functionality.

`(gdb) x/[#][size][format] [Address/Symbol/Register][± offset]`

- `x/` means examine
- `[#]` means how much
- `[size]` means what size the data should be such as a word *w* (2 bytes), double word *d* (4 bytes), or giant word *g* (8 bytes)
- `[format]` means how the data should be interpreted such as an instruction *i*, a string *s*, hex bytes *x*
- `[Address/Symbol][± offset]` means where to start interpreting the data

#### Example Usage

- `(gdb) x/x $rax`: Displays the content of the register RAX as hex bytes
- `(gdb) x/i 0xdeadbeef`: Displays the instruction at address 0xdeadbeef
- `(gdb) x/10s 0x893e10`: Displays 10 strings at the address
- `(gdb) x/10gx 0x7fe10`: Displays 10 giant words as hex at the address

### Forking

If the program happens to be an accept-and-fork server, gdb will have issues following the child or parent processes. In order to specify how you want gdb to function you can use the command `set follow-fork-mode [on/off]`

### Setting Data

If you would like to set data at any point, it is possible using the command `set [Address/Register]=[Hex Data]`

#### Example Usage

- `set $rax=0x0`: Sets the register rax to 0
- `set 0x1e4a70=0x123`: Sets the data at 0x1e4a70 to 0x123

### Process Mapping

A handy way to find the process's mapped address spaces is to use `info proc map`:

```
Mapped address spaces:

	Start Addr   End Addr       Size     Offset objfile
	 0x8048000  0x8049000     0x1000        0x0 /directory/program
	 0x8049000  0x804a000     0x1000        0x0 /directory/program
	 0x804a000  0x804b000     0x1000     0x1000 /directory/program
	0xf75cb000 0xf75cc000     0x1000        0x0
	0xf75cc000 0xf7779000   0x1ad000        0x0 /lib32/libc-2.23.so
	0xf7779000 0xf777b000     0x2000   0x1ac000 /lib32/libc-2.23.so
	0xf777b000 0xf777c000     0x1000   0x1ae000 /lib32/libc-2.23.so
	0xf777c000 0xf7780000     0x4000        0x0
	0xf778b000 0xf778d000     0x2000        0x0 [vvar]
	0xf778d000 0xf778f000     0x2000        0x0 [vdso]
	0xf778f000 0xf77b1000    0x22000        0x0 /lib32/ld-2.23.so
	0xf77b1000 0xf77b2000     0x1000        0x0
	0xf77b2000 0xf77b3000     0x1000    0x22000 /lib32/ld-2.23.so
	0xf77b3000 0xf77b4000     0x1000    0x23000 /lib32/ld-2.23.so
	0xffc59000 0xffc7a000    0x21000        0x0 [stack]
```

This will show you where the stack, heap (if there is one), and libc are located.

### Attaching Processes

Another useful feature of GDB is to attach to processes which are already running. Simply launch gdb using `gdb`, then find the process id of the program you would like to attach to an execute `attach [pid]`. 