# Nevernote
## Author

## Points
200
## Category
Web
## Description
```
from:     Nevernote Admin <nevernoteadmin@nevernote.com>
to:     challenger@ctf.isis.poly.edu
date:     Thurs, Sep 19, 2013 at 3:05 PM
subject:     Help
Friend, Evil hackers have taken control of the Nevernote server and locked me out.  While I'm working on restoring access, is there anyway you can get in to my account and save a copy of my notes?  I know the system is super secure but if anybody can do it - its you.
Thanks,
Nevernote Admin
```
## Flag
`akjdsf98LolCats234lkas0!#@%23Ferrari134545!@#250saDucati9dfL$Jdc09234lkjasf`
## Solution
There are two issues.  There are parameter tampering attacks for both the "view messages" and "view notes" functionality.  These will allow one user to view another user's messages and notes.  The issue is these parameters are encrypted so the challenger needs a way to get or construct and encrypted id for the target user.  This can be done by sending the nevernoteadmin a link using the supplied functionality.  By visiting this link, the encrypted messageid will be disclosed in the referrer header.  The challenger needs to setup a box with a listener in order to grab this link.
## Setup
