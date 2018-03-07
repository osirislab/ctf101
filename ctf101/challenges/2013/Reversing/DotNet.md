# DotNet
## Author

## Points
150
## Category
Reversing
## Description

## Flag
`flag{I'll create a GUI interface using visual basic...see if I can track an IP address.}`
## Solution
Password used to encrypt flag is 13371337255
1. I used .net reflector to take apart the executable and view the code.
2. I saw that it checks to see if the password xor with one value equals another value.
3. Xor two known values to obtain password.
4. Plug password into application and it decrypts the flag (using password as key for decrypting a base64 encrytped  AES blob)

## Setup
Distribute `DotNetReversing.exe`