# PPS
## Author
Wiens
## Points
200
## Category
Misc
## Description

## Flag
`flag{ConsiderThisPUNishmentEnough}`
## Solution
1. Leak source
```
nc localhost 5665
4
pps.php
2
```
2. Leak flag
With the source, find the hidden password, evade the string matching via PHP's awesome forced coersion:
```
nc localhost 5665
5
0xabadfad
flag
2
```

## Setup
Just move the files from deploy somewhere on a filesystem. Preferrably give whatever runs the php no permissions to write anything anywhere. Then launch via xinetd on port 5665 (or whatever).