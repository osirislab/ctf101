# Itsy
## Author

## Points

## Category
Pwn
## Description
Get the key (it's in the usual location).
## Flag
`key{StupidSpiderNeedsToGiveUp}`
## Solution
`solution.elf`
## Setup
Distribute binary and links
1. Create user itsy
2. `cp server-source/itsy; ~itsy/; cp key ~itsy/; chown root:root ~itsy ~itsy/itsy ~itsy/key; chmod 0640 ~itsy; chmod 0750 ~itsy/itsy; chmod 0640 ~itsy/key`
3. Run `~itsy/itsy` as root, should drop-privs to user itsy after connect.
4. Verify by: `(cat solution.elf; sleep 1)|nc target-ip 11586`
