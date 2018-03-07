# Title
## Author

## Points
500
## Category
Crypto
## Description
We've found the source to the Arstotzka spies rendevous server, we must find out their new vault key.
## Flag
`We'd all be so much safer if all primes were so free and germane`
## Solution
`slurpclient solver.py`
It's a fucked up, modified implimentation of SRP that requires a user without credentials to authenticate themselves.  So this won't be done til monday, but essentially the field prime -1 is fairly smooth, in this case though it's a schnorr group.  The group is seeded with 9001, so you can use this to find a generator which generates a group of order 4502.  This means that given two different attempts to login, with a generator which i supply as the user index, there will be an easy system of equations, that allow me to derive k * v, where k is already known, once i have this value I can solve for v, then do the servers key derivation algorithm, and send an authenticator as the server, without ever knowing the actual password.
## Setup
Attached are two files, one to distribute to players, one to run, this thing is written in python so running it on a beefier machine might be good