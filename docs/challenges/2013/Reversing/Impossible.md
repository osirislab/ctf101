# Impossible
## Author

## Points
500
## Category
Reversing
## Description
WTF, his hp is over 9000! Beat the game to get your key. 
## Flag
`ou6UbzM8fgEjZQcRrcXKVN`
## Solution
We're provided with an NDS file and the instructions to "Beat the game to get your key!". By running the binary on an emulator, we can see that it appears to be a *slightly* unfair space shooter. We're going to determine where the hp for the boss is, and set it to a more reasonable value (like 0).
Some more investigation reveals that the game is logging information to `stderr`
```
INIT MAINMENUSTATE
BEGIN RUN LOOP
INIT GAMESTATE
ADD ENT
...
```
`ADD ENT` sounds promising. Searching for this string uncovers a function at `0x2002820`, which we'll call `funct_add`. Next, we look for xrefs to this function. `0x2002188` has exactly two calls to `funct_add`. There's a high likelyhood that it's responsible for constructing the player and boss objects. We'll call it `funct_init`.
If we scroll up a bit, we see the following calls:
```
bl      201fa80
...
bl      2002bb0
...
bl      201fa80
...
bl      2002de0
```
Via Challenge Writer Logic (tm), we can say that `0x201fa80` is allocating data. `0x2002bb0` and `0x2002de0` contain the actual constructor logic.
If we look in `0x2002de0`, we see a rather interesting local.
```
.word   0x000f4240;
```
This is used at `0x2002df6`
```
ldr     r0, [pc, #168]
```
Hmm, what happens if we replace this with a 0?
[screen_01](screen_01.png)
Hmm, doesn't that key look a bit short? The CSAW website doesn't accept it, either. Why don't we do a memory search for 'key is'? That should turn up this string and tell us what's up with the text on screen.
[screen_02](screen_02.png)
Aha, some of the characters weren't being printed! Entering this into the key submission page confirms that this is the key and nets us XXX points.
## Setup
Distribute `impossible.nds`