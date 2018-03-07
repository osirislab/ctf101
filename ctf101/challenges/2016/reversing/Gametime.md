# Gametime
## Author
brad_anton
## Points
50
## Category
Reversing
## Description
Guess what time it is! That's right! Gametime! Wowwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww!!!!!!!!!!!!
note: flag is not in flag{} format
## Flag
`(no5c30416d6cf52638460377995c6a8cf5)`
## Solution
You *could* maybe check your speed with the game, but really the solution to reverse out the leading sequence of character presses (they're static), then either reverse out the key or probably much quicker is to:

1. Attach the debugger, set the following breakpoints to overwrite register values to fast track you to the key. You'll need to adjust the image address at run time:

`bp image010c0000 + 18d8 "r edx=1;g;"`
`bp image010c0000 + 1916 "r esi=13;g;"`

2. Let the program start, paste in the following sequence, including spaces: 

" xm xmmx mmxxmx  xm"

A vuln in the program logic allows the user to add character to the key press buffer before they're prompted to. 

Finally the program will spit out:
`key is  (no5c30416d6cf52638460377995c6a8cf5)`
## Premise
A game that requires a user to type either space ('s'), 'm' or 'x' when prompted. If they are fast enough, they get the key. 
## Warnings
Everything should be statically compiled. I tested on two different  Win8.1 VMs with no problem. If someone gets DLL loading errors, they most likely need to download Microsoft's Visual C Runtime Library. 