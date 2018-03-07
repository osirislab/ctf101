# Greenhorn'd
## Author
Stortz
## Points
200
## Category
Pwn
## Description
Find the key!
## Flag
`key{He may be angry all the time, but he's the only one that understand Windows DACLs}`
## Solution
`x.py`
## Setup
Distribute `greenhornd.exe`
Configure a Windows 8.1 server and launch the AppJailLauncher. Do not distribute the App Launcher, it should be exploitable locally without it. AppJailLauncher.exe /network /key:key /port:9998 /timeout:30 greenhornd.exe