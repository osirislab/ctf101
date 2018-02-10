# Title
## Author

## Points
100
## Category
Forensics
## Description

## Flag
`key{forensics_is_fun}`
## Solution
The image appears to be made of entirely white pixels. Upon inspection the player should realize that there are actually rgb(255, 255, 255) and rgb(254, 254, 254). This can be achieved through some image statistics or image editors or simply tilting the screen.
`parity.py`
## Setup
Distribute `chal.png`