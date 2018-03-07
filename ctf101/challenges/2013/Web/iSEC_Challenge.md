# iSEC Challenge
## Author

## Points

## Category
Web
## Description
ACME Co's update server has been stolen and posted on the internet. It seems like a bunch of janky python code.  See if you can perform some ownage.
Note:
Your instance is specific to your team.  Unless you want other teams messing with your instance and potentially denial-of-servicing you, keep your instance location a team secret.
## Flag
`key{32b57cd119d78b979c624a5bcb50b716}`
## Solution
The update code parses an XML POST that looks like this:
```
<?xml version="1.0" encoding="UTF-8" ?>
<config>
	<updateServer>fiascoaverted.com</updateServer>
	<currentVersion>1.3.1</currentVersion>
    <updateMethod>latest</updateMethod>
</config>
```
- updateServer controls the hostname to a DNS server that has a TXT record containing the current version of their software
- currentVersion is intended to be the client's current version
- updateMethod seems to be a legacy option, where the only valid value is `latest`

While the python server has a number of juicy targets in its code (subprocess, XML parsing) the only one that will actually lead you anywhere is a race condition. (At least, I think.  Maybe there's another bypass!)
The currentVersion can be decremented so that it serves you the latest client file.  This file is useless.
But, it allows you to expose a race condition. You have two options:
1. Easy: Spam the ever-loving shit out of the server with an updateMethod that says `../../../../../whatever`, while sending a single legitimate request for 'latest' (Burp Intruder+Repeater works great for this)
2. Harder: Change the target DNS server to a DNS server in your control, and then slow down the response to expose the race condition more easily.

Now that you have arbitrary file read on the system, start stealing files.  Stealing the source isn't useful, so you need to use your excellent linux skillz to break in.
You immediately go to /etc/shadow - which yields only one account with a password - root.
The root password is `terrific` and uses the DES algorithm - so we're really talking an easy cracking game.  It takes under a second with a full english dictionary.
Unfortunetly, no one is not allowed to login over SSH using passwords!  shadow also provides you with the list of accounts however.
Inside of the `tom` account, you'll find a SSH private key that allows you to login as tom.  Then, you can sudo using the root password, and go look for the flag, which is in `/home/ubuntu/csaw/flag.txt`
## Setup
Teams get a zip folder with 2 python files and a README.

I'll be running an EC2 instance for each team, and will supply you with N zips (tell me N) each with a different running instance name at X:00 on November Y.

I'll be monitoring irc for any problems between the hours of:
- Nov 14 9PMish - 11PMish
- Nov 15 7AMish - 8AMish
- Nov 15 10AMish- 6PMish onsite at Poly
- Nov 16 7AMish - 8AMish

## Notes
To make admin easier, all instances share the same private SSH key.  Teams are instructed not to share their server address, as it may lead to attacks from other teams.