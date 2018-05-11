# Memory Forensics

There are plenty of traces of someone's activity on a computer, but perhaps some of the most valuble information can be found within memory dumps, that is images taken of RAM. These dumps of data are often very large, but can be analyzed using a tool called [Volatility](http://www.volatilityfoundation.org/)

## Volatility Basics

Memory forensics isn't all that complicated, the hardest part would be using your toolset correctly. A good workflow is as follows:

0. Run `strings` for clues
1. Identify the image profile (which OS, version, etc.)
2. Dump processes and look for suspicious processes
3. Dump data related interesting processes
4. View data in a format relating to the process (Word: docx, Notepad: txt, Photoshop: psd, etc.)

### Profile Identification

In order to properly use Volatility you must supply a profile with `--profile=PROFILE`, therefore before any sleuthing, you need to determine the profile using imageinfo:

```bash
$ python vol.py -f ~/image.raw imageinfo
Volatility Foundation Volatility Framework 2.4
Determining profile based on KDBG search...

          Suggested Profile(s) : Win7SP0x64, Win7SP1x64, Win2008R2SP0x64, Win2008R2SP1x64
                     AS Layer1 : AMD64PagedMemory (Kernel AS)
                     AS Layer2 : FileAddressSpace (/Users/Michael/Desktop/win7_trial_64bit.raw)
                      PAE type : PAE
                           DTB : 0x187000L
                          KDBG : 0xf80002803070
          Number of Processors : 1
     Image Type (Service Pack) : 0
                KPCR for CPU 0 : 0xfffff80002804d00L
             KUSER_SHARED_DATA : 0xfffff78000000000L
           Image date and time : 2012-02-22 11:29:02 UTC+0000
     Image local date and time : 2012-02-22 03:29:02 -0800
```

### Dump Processes

In order to view processes, the `pslist` or `pstree` or `psscan` command can be used.

```bash
$ python vol.py -f ~/image.raw pslist --profile=Win7SP0x64 pstree
Volatility Foundation Volatility Framework 2.5
Offset(V)          Name                    PID   PPID   Thds     Hnds   Sess  Wow64 Start                          Exit
------------------ -------------------- ------ ------ ------ -------- ------ ------ ------------------------------ ------------------------------
0xffffa0ee12532180 System                    4      0    108        0 ------      0 2018-04-22 20:02:33 UTC+0000
0xffffa0ee1389d040 smss.exe                232      4      3        0 ------      0 2018-04-22 20:02:33 UTC+0000
...
0xffffa0ee128c6780 VBoxTray.exe           3324   1123     10        0      1      0 2018-04-22 20:02:55 UTC+0000
0xffffa0ee14108780 OneDrive.exe           1422   1123     10        0      1      1 2018-04-22 20:02:55 UTC+0000
0xffffa0ee14ade080 svchost.exe             228    121      1        0      1      0 2018-04-22 20:14:43 UTC+0000
0xffffa0ee1122b080 notepad.exe            2019   1123      1        0      1      0 2018-04-22 20:14:49 UTC+0000
```

### Process Memory Dump

Dumping the memory of a process can prove to be fruitful, say we want to dump the data from notepad.exe:

```bash
$ python vol.py -f ~/image.raw --profile=Win7SP0x64 memdump -p 2019 -D dump/
Volatility Foundation Volatility Framework 2.4
************************************************************************
Writing System [     2019] to 2019.dmp

$ ls -alh dump/2019.dmp
-rw-r--r--  1 user  staff   111M Apr 22 20:47 dump/2019.dmp
```

### Other Useful Commands

[There are plenty of commands](https://github.com/volatilityfoundation/volatility/wiki/Command-Reference) that Volatility offers but some highlights include:

- `$ python vol.py -f IMAGE --profile=PROFILE connections`: view network connections
- `$ python vol.py -f IMAGE --profile=PROFILE cmdscan`: view commands that were run in cmd prompt