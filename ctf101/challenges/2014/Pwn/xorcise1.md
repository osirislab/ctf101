# XORcise 1
## Author
Edwards
## Points
500
## Category
Pwn
## Description

## Flag
`flag{code_exec>=crypto_break}`
## Solution
`exploit.py`
## Setup

## Notes
- Solution information
Included with this write-up are two VMs: Official and Competitor, they are the same except the Official is for the judges/organizers to run, and has a new set of credentials and flag, where the Comepetitor is for the competitors to have an environment for VR+exploit dev.
- Information for competitors
Login locally or via ssh as root using the password: p0wer0verwhelming
The source & binary for the challenge service in: /home/xor/service
The service runs as user 'xor', and listens on TCP port 24001
The directory structure mirrors that of official production VM
The flag is in /home/xor/service/flag.txt
Happy bug hunting!
-Information for CSAW Organizers & Judges
VM root pw: `m0n3y_p0w3r_0d4y`
VM service pw: `NOPE!in:flag.txt`
Challenge flag: `code_exec>=crypto_break`
Flag should be found in /home/xor/service/flag.txt as: `flag{code_exec>=crypto_break}`
The /home/xor directory and all subcontents are owned by root, but readable/executably by user 'xor'.
The IP for both VMS is currently set to static: 192.168.57.172 
To change this involves systemctl and netctl, and modifying the file in:
`/etc/netctl/network@service`
The service is stupid. It has some terrible home-rolled crypto, but that's not really the point. Although the crypto is susceptible to a number of attacks (replay, chosen-plaintext, key-included-with-ciphertext, short-hashing, hashing collisions, everything-forever), none of the crypto attacks should be easier (or feasible) given the vectors and isolated exposure.
See source/binary in the service_source_and_binary/ included with this file.
There is a bug in the decipher() function, which allows for out-of-bounds manipulation of stack contents, and can be exploited to gain control over execution flow. Included with this write-up is exploit.py, which exploits the service VM(s) to gain a connect-back shell (requires netcat).
This is not vanilla memory corruption, and exploitation and involves specifying an invalid size, and XORing local function variables to augment a loop offset such that subsequent XOR operations manipulate the saved return address; there are multiple ways this can be exploited.
For more details or any questions, please feel free to email/IM me:drraid@gmail.com