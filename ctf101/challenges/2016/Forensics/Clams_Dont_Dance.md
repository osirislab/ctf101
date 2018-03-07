# Clams Don't Dance
## Author

## Points
100
## Category
Forensics
## Description
Find the clam and open it to find the pearl. 
## Flag
`flag{TH1NK ABOUT 1T B1LL. 1F U D13D, WOULD ANY1 CARE??}`
## Solution
A deleted file can be recovered from the image, `clam.pptx` with Autopsy.
Unzipping the clam, there is an `image0.gif` inside of `ppt/media` that is MaxiCode for the flag.
## Setup
Files: https://github.com/isislab/CSAW-CTF-2016-Quals/tree/master/Forensics/Clams_Dont_Dance