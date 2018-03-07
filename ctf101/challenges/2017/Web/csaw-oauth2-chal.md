# CSAW OAUTH2
## Author
itszn, Ret2 Systems
## Points
500
## Category
Web
## Description
We found this weird site that lets you send short messages of a much better length than 140 280 characters.
http://broadcastr.chal.csaw.io:4000
NOTE: The 500 on the /user/history endpoint is irrelevant.
## Flag
`flag{m4yb3_w3_n33d_oauth3_n3xt?}`
## Solution
[sol.py](sol/sol.py)
## Setup
1. Install docker
2. Modify `config.sh` to have the correct urls and settings
2. `./create.sh` to build the docker container
3. `./run.sh` to run the container
