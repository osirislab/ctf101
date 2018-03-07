# Watchword
## Author

## Points
100
## Category
Forensics
## Description
Canned epic hidden snek flavored cookies have shy gorilla.
## Flag
`flag{We are fsociety, we are finally free, we are finally awake!}`
## Solution
The description "canned" hints toward the file having more files within it. powpow.mp4 has a png appended to it. 
The description "epic hidden snek flavored" hints at the module stepic. Using stepic to write the output to a different file reveals a jpg.
powpow.mp4 's properties show that the Artist is Stefan Hetzl, the Title is `aHR0cDovL3N0ZWdoaWRlLnNvdXJjZWZvcmdlLm5ldC8=`, and the file was last modified October 09, 2003 (the last update to the steghide website). This points to steghide, since the title is base64 for [steghide's website](http://steghide.sourceforge.net/). The title of the challenge is "Watchword", which is a synonym for password. Using steghide and the password "password" on the jpg reveals a text file.
The text file is Base85 for the flag.
```
foremost powpow.mp4
stepic -i output/png/00001069.png -d > thing
steghide extract -sf thing.jpg -p password
cat base64.txt
python3
>>> import base64
>>> base64.b85decode(b'W^7?+dsk&3VRB_4W^-?2X=QYIEFgDfAYpQ4AZBT9VQg%9AZBu9Wh@|fWgua4Wgup0ZeeU}c_3kTVQXa}eE')
b'flag{We are fsociety, we are finally free, we are finally awake!}'
```