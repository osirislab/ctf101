# ethersplay
## Author
quend
## Category
Misc
## Points
400
## Description
I stole this contract from a private blockchain. Can you help me reverse its secrets?
## FLAG
`flag{ETHBTC_tothemoon}`
## Setup
Distribute .abi and .bytecode files.
## Solution
Its solidity bytecode. So players must:
1. figure out how to reverse it (the name of the challenge is a hint to tooling.
2. figure out which function is a good target function - aka which has 'flag' in it
3. find the winning path in the function - when you pass in the right username it will print out something different
4. figure out what algo is used to hash the password (its SHA1)
5. recover the flag through brute forcing 6 characters in SHA1
6. submit the flag
