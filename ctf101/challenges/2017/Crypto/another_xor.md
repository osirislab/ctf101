# Anothor_Xor
## Author

## Points
100
## Category
Crypto
## Description
Receiving a python script that encrypts a string using a user-chosen key, and an encrypted message- try to get the flag.

Hey, hey can you find my secret.

274c10121a0100495b502d551c557f0b0833585d1b27030b5228040d3753490a1c025415051525455118001911534a0052560a14594f0b1e490a010c4514411e070014615a181b02521b580305170002074b0a1a4c414d1f1d171d00151b1d0f480e491e0249010c150050115c505850434203421354424c1150430b5e094d144957080d4444254643
## Flag
`flag{sti11_us3_da_x0r_for_my_s3cratz}`
## Solution
plaintext:
flag                                  key                                                                hash(flag+key)
flag{sti11_us3_da_x0r_for_my_s3cratz}|A quart jar of oil mixed with zinc oxide makes a very bright paint|d5111350bbbe105121b9a9496ac08df2

The key is repeated to be able to encrypt the plaintext.
## Setup
Challengers will be given the cipher:

274c10121a0100495b502d551c557f0b0833585d1b27030b5228040d3753490a1c025415051525455118001911534a0052560a14594f0b1e490a010c4514411e070014615a181b02521b580305170002074b0a1a4c414d1f1d171d00151b1d0f480e491e0249010c150050115c505850434203421354424c1150430b5e094d144957080d4444254643