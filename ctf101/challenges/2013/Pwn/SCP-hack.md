# SCP Hack
## Author

## Points
500
## Category
Pwn
## Description
The [SCP organization](http://128.238.66.211:45000) wants you to join, accept and see if you can take advantage of their interns sloppy coding and outdated browser.
## Flag
`whereisthedirtysmellysauce`
## Solution
This is a two-part challenge. At the moment there is no key for the first part, just the second. It begins with [http://128.238.66.211:45000](http://128.238.66.211:45000), you are invited to join SCP using an invite code. There are a series of flags below the invite code. The first challenge is to figure out how to prove yourself to SCP. This is done by using the same invite code (which becomes a query string parameter automatically if you don't have one assigned) from various proxies around the world. This seems difficult at first, but is rather simple using IP/port combinations from hide-my-ass or similar proxy aggregates. This should take 20-30 mins of python scripting.
When you "prove" yourself you'll have access to upload CSRs to be signed by SCP. Uploading a CSR WILL be automatically "signed" by SCP. The CSR will really just go into oblivion, but there is a script that will try to parse it. The player should be focused on the SCP "interns" because that is part of the challenge description. On the SCP page the About Us: at the bottom talks about their interns and the GitHub page they use. The players should recon that github and see the ONLY python script uploaded. The players should also see the SCPs additions to CSRs, specifically that they accept a "link to a photo" in the `commonName`. The python script on the github will download the content within these URLs.
Adding a link to a player-controlled HTTP/HTTPS server will reveal the "interns" OS and web browser, specifically IE7. The challenge is to recognize that the "link" in common name also support the `file://` protocol. This was a huge problem in the past, and it has resurfaced in the bit coin miners as an information leakage vulnerability. Once recognized, if the players set a file:// protocol link in their common name, the "interns" IE7 browser will try to log in with their current username and password. The username is the key for the challenge, the username is `key=whereisthedirtysmellysauce`, so that should be obvious.
## Setup

## Notes
Hints:
1. What recon can you do on the SCP interns?
2. Are the SCP interns vulnerable to information leakage?
