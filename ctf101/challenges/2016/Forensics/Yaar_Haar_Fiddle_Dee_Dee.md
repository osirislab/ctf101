# Yaar Haar Fiddle Dee Dee
## Author

## Points
200
## Category
Forensics
## Description
DO WHAT YE WANT 'CAUSE A PIRATE IS FREE. YOU ARE A PIRATE!
## Flag
`flag{b31Ng_4_P1r4tE_1s_4lR1GHT_w1Th_M3}`
## Solution
The challenge name, "YAAR HAAR FIDDLE DEE DEE" is a reference to a viral youtube video, as well as a hint. The description is just some of the lyrics of the viral song.
The challenge is a pcap of a "conversation" created with python sockets. There 3 base 64 encoded strings, one is just a blob of 100x100 grayscale images, one is an encrypted zip file, and one is an xml file which is formatted to opencv's haar cascade format. Players must seperate out the images, load the haar cascade file with opencv and run it against the images in the file, all of this, as well as the parameters required, are alluded to in the dialog that is also in the pcap. They will also need to draw a square over the object that the haar cascade detects, so that they can successfully identify it as a "skull and crossbones", which is then the password for the encrypted zip file (without spaces, as stated in the pcap), which contains flag.txt. the dialog also helpfully states that the map (the cascade file) points to the key (the skull and crossbones) for the booty (the zip file), and also says no spaces and no capitalized letters.
1. extract base64 strings, decode into 3 different files
2. `binwalk -e` the image blob
3. use opencv python docs to write a haar cascade script
4. identify the jollyroger and use that as the password for the zip
5. `cat flag.txt`