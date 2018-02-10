# deeeeeeaaaaaadbeeeeeeeeeef
## Author

## Points
200
## Category
Forensics
## Description

## Flag
`key{TheISISPasswordIs}`
## Solution
This PNG contains a modified IHDR chunk with modified dimensions for the image. Viewing it displays part of an ISIS whiteboard. pngcheck will notify the user that the IHDR has been modified. EXIF data will tell the user that the image was taken with an iPhone 5. Searching for the default camera image size will give the user a set of larger resolutions to change the dimensions to. Modifying the height will show the user the key written on the board.
## Setup
Distribute `IMG_0707.png`