# ecxor
## Author
aweinstock
## Points
100
## Category
Crypto
## Description
I used some super-powerful crypto tonight
I hear that elliptic curves make it safe to use smaller key sizes. Can you break this curve25519-encrypted message?
## Flag
`flag{generalizing_vignere_to_arbitrary_groups_is_not_good}`
## Solution
[ecxor_solver.py](ecxor_solver.py)
## Setup
Challenge files: (exactly one of ecxor_handout_{100,200,300}.py), rfc8032.py, and a 
ciphertext blob generated with the the handout and the real flag. DO NOT give oracle access to a server (the handouts aren't side-channel hardened).
Intended solution: do (blob - 'flag{') to get a partial key, and crib/use ngram-style heuristics to use the english blob at the end to infer the rest of the key
## Notes
Challenge points: {100,200,300} depending on whether ecxor_handout_{100,200,300}.py is given out. These are not independent challenges: ecxor_handout_100.py basically has extra hints towards the solution.