# MBot
## Author
Crowell
## Points
300
## Category
Pwn
## Description

## Flag
`flag{by blocking java plug-ins, mozilla hopes to reduce the risk of cool kid}`
## Solution
needs libcurl on 32 bit linux.
ASLR is on. NX is on.
This exploit works ~20% of the time, because of some randomness in the binary
and I was too lazy to fix some bug when did a stack pivot the first time ;)
To run the exploit, run `ruby ./stage1.rb > stage1` copy the stage1 file to some web server.
Then run `ruby ./hax.rb` take the output from the leaked system addr
Add the system addr to the file stage2.rb, run `ruby ./stage2.rb > stage2`
Run `ruby ./hax2.rb "cat key;"`.
This works because the server forks, so you can reconnect and every fork will have the same randomization.
Of course also provide the libc binary.
## Setup
