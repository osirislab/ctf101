# Noobs First Firmware Mod
## Author

## Points
500
## Category
Reversing
## Description
N00b firmware modder says: "My first u-boot mod, there might be errors :(
## Flag
`S-U-P-E-R-S-E-X-Y-H-O-T-A-N-D-S-P-I-C-Y`
## Solution
It's a simple u-boot following the latest checkout. The checkout version is inside the build version. It's built for versitilepb, which is the most common board for u-boot tutorials online. You can boot them easily in QEMU-ARM. The idea is to boot the image and see there's an added command to the u-boot shell called "csaw", this command is weird in that it asks for 7-bytes of input and errors if you supply less than 7, 7, or more than 7. Sounds like a programming error!? Well, if they RE the image they'll see right after the JMP logic error it will try to decode a key from a specific location in 64-bit space and prepend the string "key=". So now they have to search for where that memory location is set. You can short circuit that search by running strings on the image. Strings will show "key!=SUPERSEXTHOTANDSPICY". Well, the decode routine just adds '-'s between each letter.
## Setup
Distribute `noobs-first-firmware-mod.tgz`
## Notes
Hints: 
1. Try to boot the image, does anything appear "modded"?
2. It's a versitilepb board, use QEMU
