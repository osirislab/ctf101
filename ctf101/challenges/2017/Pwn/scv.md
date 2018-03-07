# SCV
## Author
## Points
100
## Category
Pwn
## Description
SCV is too hungry to mine the minerals. Can you give him some food?
## Flag
`flag{sCv_0n1y_C0st_50_M!n3ra1_tr3at_h!m_we11}` 
## Solution 
See [scv.py](scv.py)
## Setup
1.`sudo docker build -t "scv" [Path to Dockerfile]`
2.`sudo docker run --name "scv" -d -p [PORT]:[PORT] [IMAGE]`