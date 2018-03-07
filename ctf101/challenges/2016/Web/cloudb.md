# Something Something ClouDB
## Author

## Points
200
## Category
Web
## Description
"I'm working on this new service which allows you to store notes, TODOs, and more! And all of our data is accessible over JSONP so you can integrate it into other sites!
NOTE: The flag is NOT the mysql password.
UPDATE: Fixed an unintentional bug which made the challenge more confusing.
`http://web.chal.csaw.io:1344`"
## Flag
`flag{d0nt_Forg3t_2_San1t1ze_Y0uR_C@11back$}`
## Solution
1. Identify template.php as possible file read and use it to leak source
2. See in source references to db.sql.bak which is a DB backup
3. See admin ID=0
4. Realize that session ID=0 can be spoofed for inserts/updates by not being logged in (b/c of interval.
5. Use this to add a new tile to the admin which uses a JSONP endpoint with XSS in the callback to get cookies
6. Login with cookies. flag is in a TODO

## Notes
* Run with `docker run -e MYSQL_PASS='S0meR3@11yG00dPa$$w0rdThatY0u5hou1dntCar3@b0uT' -p {WhateverPortItShouldBe}:80 cloudb`
Also needs a phantomjs thing which logs in with `admin:Pg8ARJOVj4XUm2nIW67d` so that they can steal admin cookies.