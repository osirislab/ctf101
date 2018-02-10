# ethersnoob
## Author
quend
## Points 
300
## Category
Misc
## Description
baby's first contract
## Flag
Judges need to manually verify scores. From a judge computer, log into the CSAW17-ETH-1 VM. Run screen -ls and attach to the one instance running. This is a geth terminal. Attach to a teams contract by running:
```
var contractInfo = JSON.parse(ABI_BLOB);
var test = eth.contract(contractInfo).at("CONTRACT_ADDR");
test.get_flag.call()
```
ABI_BLOB and CONTRACT_ADDR are the last 2 entries in the account#.txt file distributed to the team.
If the call() returns the CONGRATS string award points. 
You may need to re-unlock the admin account, to do so run (admin is account #11 as is the account which deployed all contracts):
```
personal.unlockAccount("2a8f32fac2f2911aad09940b33884d2c51661464");
Enter Password:
sHtXJoHPlxGrNMa2
```
## Setup
Each team should get 1 of the files in the accounts.ZIP, these are accounts and contracts on the network setup on CSAW17-ETH-1. Sources should be distributed if people are stuck. The source filename number is associated with the account filename number (there are only 10 sources. each team per region has a unique .sol file, but teams from different regions may share .sol files).  
There are ten for each region. i.e.:
REGION 1
accounts1.txt => ethersnoob1.sol
accounts2.txt 
accounts3.txt
...
REGION 2
accounts01.txt => ethersnoob1.sol
accounts02.txt
accounts03.txt
...

and so on. accounts_admin.txt is for the judges.
## Solution
Its solidity bytecode. So players must:
1) figure out how to reverse it 
2) figure out how to talk to it over the netwowrk
3) find the bug in the solidity bytecode (its a simple integer overflow error)
4) realize that integer widths are different in solidity than in C (32 bytes instead of 4 bytes)
5) find a way to trigger it through sending up a contract or transaction commands
6) use the overflow to set the win state flag
6) call get_flag()
