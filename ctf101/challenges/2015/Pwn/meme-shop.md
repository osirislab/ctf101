# Meme Shop

## Author
Crowell
## Points
400
## Category
Pwn
## Description
only dwn knows what the meme is!
pwn this service to find out what only he knows!
dwn: please tell us the meme....
## Flag
`flag{dwn: please tell us your meme. I'm not going to stop asking}`
## Solution

## Setup
this is a simple type confusion challenge
you have types "meme" and "mrskeletal"
the counter is an int8_t so you can overflow and f it up
first you need ruby
then you need colorize
`gem install colorize`
then you need to build the extension
```
ruby ./extconf.rb
make
```
then run the challenge with `socat` or w/e
make sure that the flag is called "flag" because there is arb file read
also delete the .c file and do not provide the debug edition of the rb file