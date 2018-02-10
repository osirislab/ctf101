# Miteegashun
## Author

## Points
400
## Category
Pwn
## Description
Security is solved.
## Flag
`Key:{And_all_I_got_was_this_stupid_key}`
## Solution
`exploit.py`
This pwnable has a trivially obvious buffer overflow unfortuatly this program rewrites its return addresses just before returning. Too bad the implementer decided the operating systems stack is untrustworthy.
Challanger can abuse this fact to achieve remote code execution
Challenger will have to rewrite a non negligable ammount of state data on the stack to achieve RCE.
## Setup
Distribute `miteegashun`