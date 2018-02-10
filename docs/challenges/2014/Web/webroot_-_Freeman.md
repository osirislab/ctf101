# Webroot
## Author
Freeman
## Points
400
## Category
Web
## Description
hackerhaikus.com
## Flag
`flag{rise_and_shine,_mr._freeman._rise_and_shine}`
## Solution
* There are two SQL injection vulnerabilities in the "saveHaiku" call; one in the timestamp and one in the encrypted haiku. First one requires changing the AMF type from number to string (no tools available, requires hex munging), second requires enumerating the DES_ECB key and encrypting a payload that way.
* Backend DB is SQLite3. Shell will probably be gained with the "ATTACH DATABASE" method outlined here: http://atta.cked.me/home/sqlite3injectioncheatsheet
* There might also be bugs in Amfphp itself. In fact there almost certainly are. I haven't had time to test for these.

## Setup
Please find attached webroot.tgz. Some notes on setup:
* Needs mcrypt and sqlite3 PHP extensions enabled
* Apache should be configured with hackerhaikus.com as the virtual host (DNS is already pointing to the IP specified on IRC yesterday)
* test2.php is meant to be there, it discloses the webroot which is needed for exploitation.

## Notes
* Probably just dump a file readable by www-data in /opt or something.
* I have no idea how points work for this, and how this ranks in complexity compared to the other challenges, and therefore have no idea how many points to assign for the challenge ;)
