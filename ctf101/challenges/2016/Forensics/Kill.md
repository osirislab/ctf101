# Kill
## Author

## Points
50
## Category
Forensics
## Description
Is kill can fix? Sign the autopsy file?
## Flag
`flag{roses_r_blue_violets_r_r3d_mayb3_harambae_is_not_kill}`
## Solution
`kill.pcapng` is kill. The file signature should be corrected to `0A 0D 0D 0A`... The third file's FTP-DATA starting at packet 696 contains the flag in a jpg file.