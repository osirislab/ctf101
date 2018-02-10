# s3
## Author
Taylor
## Points
300
## Category
Pwn
## Description

## Flag
`flag{SimplyStupidStorage}`
## Solution
`sb.rb`
## Setup
Requirements:
* OS: Ubuntu 14.04
* Packages: libc, libstdc++, xinetd
* User: "amazon"
* Home Directory: "/home/amazon"

Installation:
```
mv s3.xinetd /etc/xinetd.d/s3
chown root:root /etc/xinetd.d/s3
chmod 644 /etc/xinetd.d/s3

mv s3.flag /home/amazon/flag
chown root:amazon /home/amazon/flag
chmod 640 /home/amazon/flag

mv s3 /home/amazon/s3
chown root:amazon /home/amazon/s3
chmod 750 /home/amazon/s3

chown amazon:amazon /home/amazon
chmod 750 /home/amazon
```
Testing:
`ruby s3.rb <remote host>`