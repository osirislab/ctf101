# KWS (Part 1)
## Author
itszn, Ret2 Systems
## Points
300
## Category
Web
## Description
We developed a much better alternative to AWS. Our high-performance kernel driver gives us unparalleled speed of execution. And we're super-secure!
http://web.chal.csaw.io:6001/

NOTE: Login with your CTFd credentials.
NOTE: This might take a minute to start up the first time you login. Please be patient!
NOTE: There may be ways to poke at other teams' boxes. Don't do that, it is not part of the challenge.
NOTE: If you have issues with your instance, try logging out of the KWS interface, and logging back in.
NOTE: Sorry for all of the notes :P
## Flag
flag{why_d03s_th1s_k3rnel_sm3ll_l1ke_p1ckl3s}
## Solution
in `./solutions`
## Premise
**Cloud Object Storage With Kernel Accleration**

This is a two part challenge. The first part is a ~300 point web challenge. The second is a 500 point kernel pwning challenge.

Each team should get their own instance running the KWS back end. There is a main server that acts as the
face of the web challenge, and will allow players to reboot/reset their instance (if they fuck up the kernel part)

*Instance control is still not implmented yet*

The goal of the first part is to exploit the usage of pickle on signed objects in the backend server to get a shell on the instance.

The instance is running a custom kernel module (source in `./instance/kernel/hash.c`) which implements a hashmap
that can read and store objects json from a python userspace process.

This module can be exploited to EOP to root. The last flag is in /flag
