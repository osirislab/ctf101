# Title
## Author

## Points

## Category
Forensics
## Description
Said Zed,
"This new tech is hard.
I shan't be able to cope.
Someone showed me scp
and all I said was, 'nope'."
## Flag
`OldSchoolIsBestSchool`
## Solution
extract bytes via wireshark relevant to file.bz2 and:
(for file in send?; do sleep 1; cat $file; done; sleep 1)|nc jubu 38597
While listening with an rz listener on a tcp-server.
## Setup
Distribute `saidzed.pcap`
```
sb -b * --tcp-server
rb -b --tcp-client "jubu:35699"

sz file.bz2 -L 24 -l 32 -r -vvv --tcp-client "jubu:47260"
rz -vvv --resume --tcp-server
```