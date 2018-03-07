# AUIR 
## Author

## Points
200
## Description
At long last, we stand at the threshold of destiny. For today, we will restore the glory of our legacy. Today, we will retake what we have lost and reclaim our homeworld. -Artanis-
## Flag
`flag{W4rr10rs!_A1ur_4wa1ts_y0u!_M4rch_f0rth_and_t4k3_1t!}`
## Solution 
[auir.py](auir.py)
## Setup
1.`sudo docker build -t "auir" [Path to Dockerfile]`
2.`sudo docker run --name "auir" -d -p [PORT]:[PORT] [IMAGE]`
## Note
- The binary is pre-compiled because of ollvm....
- It is compiled on Ubuntu 16.04 xenial 
- Libc: libc-2.23.so
- Probably do not have to give out libc....