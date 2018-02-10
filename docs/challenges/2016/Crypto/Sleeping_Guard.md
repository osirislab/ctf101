# Sleeping Guard  
## Author
Sophia D'Antoine
## Points
50 
## Category
Crypto
## Description
Only true hackers can see the image in this magic PNG.... 
## Flag
(flag printed in the decrypted magic.png file)
`flag{l4zy_H4CK3rs_d0nt_g3T_MAg1C_FlaG5}`
## Solution
[solution.py](solution.py)
[solution.png](solution.png)
## Premise
This challenge is a server which sends you a base64 encoded PNG image. The hint is given in the title to solve this. First that the encoding mechanism is a Xor and the way to decrypt is use the fact that all PNG's have the same first 12 byte headers. 
## Setup
Distribute sleeping_49d06c703032f66151ae07066d509c61.py  (md5sum appended)
Distrubute the server code after REMOVING the encryption key used in the Xor.
Server side run the server with the correct key in it.
Possible hints are look at the title for clues. All files have same magic header.