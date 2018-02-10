# A Rusty Road
## Author

## Points
200
## Category
Reversing
## Description
    - Traverse these roads, win and obtain the flag

## Flag
flag{D0wN_4nD_1eFt_WhEr3_Red_H3Rr1Ngz}
## Solution
[solver.py](solver.py)
## Premise
This is an RE challenge for CSAW 2017
- given is a compiled rust binary with symbols
- within the binary is a game that consists of 4 different grids

- a grid is a 10x10 board that has a number in each square
the numbers are generated with sieve of eratosthenes and a systematic shuffling
of these results that correspond to one of the four boards

- The goal is to traverse the board from the top left or 0,0 to 
the bottom right or 9,9

-The catch is that each grid during the traversal is changing based off the 
direction moved

EX: UP - BOARD1
    DOWN - BOARD2
    RIGHT - BOARD3
    LEFT - BOARD4

each correspond with a certain board

A magic number obtained through this means of traversal gets you the flag