# Detective
Dear detective, my "program" got pwned again. Can you find the culprit for me? 

Mappings for running process on server:
```
	Start Addr   End Addr       Size     Offset objfile
	0x56555000 0x56558000     0x3000        0x0 /home/detective/detective
	0x56558000 0x56559000     0x1000     0x2000 /home/detective/detective
	0x56559000 0x5655a000     0x1000     0x3000 /home/detective/detective
	0x5655a000 0x56564000     0xa000        0x0 [heap]
	0xf7e21000 0xf7e22000     0x1000        0x0
	0xf7e22000 0xf7fca000   0x1a8000        0x0 /lib/i386-linux-gnu/libc-2.19.so
	0xf7fca000 0xf7fcb000     0x1000   0x1a8000 /lib/i386-linux-gnu/libc-2.19.so
	0xf7fcb000 0xf7fcd000     0x2000   0x1a8000 /lib/i386-linux-gnu/libc-2.19.so
	0xf7fcd000 0xf7fce000     0x1000   0x1aa000 /lib/i386-linux-gnu/libc-2.19.so
	0xf7fce000 0xf7fd1000     0x3000        0x0
	0xf7fd7000 0xf7fd9000     0x2000        0x0
	0xf7fd9000 0xf7fdb000     0x2000        0x0 [vvar]
	0xf7fdb000 0xf7fdc000     0x1000        0x0 [vdso]
	0xf7fdc000 0xf7ffc000    0x20000        0x0 /lib/i386-linux-gnu/ld-2.19.so
	0xf7ffc000 0xf7ffd000     0x1000    0x1f000 /lib/i386-linux-gnu/ld-2.19.so
	0xf7ffd000 0xf7ffe000     0x1000    0x20000 /lib/i386-linux-gnu/ld-2.19.so
	0xfffdd000 0xffffe000    0x21000        0x0 [stack]
```

## Topics Covered

## Additional Information

So exit does a bit of stuff before it actually exists. try walking through it, you might find something interesting...

![](https://cdn.meme.am/cache/instances/folder489/500x/73105489.jpg)
