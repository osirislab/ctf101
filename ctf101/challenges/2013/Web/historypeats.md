# Historypeats/FridgeCorp
## Author

## Points

## Category
Web
## Description
FridgeCorp uses Jenga Blocks as a Timesheet management solution. It would be nice to get Admin and so we are able to modify our timesheets.
## Flag
`key{Bundle_Up_And_Take_Your_Vitamins!}`
## Solution
It's common for developers to rely on encrypted tokens to store data about authenticated users. This challenge requires the contestants to take advantage of poorly implemented crypto.
The "Nickname" field in the profile and registration pages are reflected in the fuel_sess encrypted token. This token is susceptible to a chosen boundary attack. This makes it possible to decrypt the entire token (at least every byte after the user controllable bytes). Once the token is decrypted, the contestants can now see the serialized structure of the string. One of the values, accesstoadminpanel, is set to false. Taking advantage of the fact that developers often assume their serialization is confidential, it's possible to gain admin access by changing the Nickname to conform to the serialization and prepend their own accesstoadminpanel value.
## Setup
Requirements:
- PHP
- Apache
- Mysql

Installation:
- Unzip csaw.zip
- Move "csaw" to your Apache root (or preference)
- Create an empty database called "csaw"
- In "csaw\fuel\app\config\development\db.php" fill in the username and password for your DB
- Open up a terminal/cmd and go to the "csaw" directory.
- Run "php oil r migrate:current" - this will setup the database.
