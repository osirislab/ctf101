# QuizApp
## Author
Oberheide
## Points
250
## Category
Web
## Description
[https://csaw-2014.appspot.com/](https://csaw-2014.appspot.com/)
## Flag
`96ef46cacf3f832f0e43f7f9e265a3ac3ca0ca2b`
## Solution
So, it's a web app that just gives you a user/pass login prompt.

If you poke around at `robots.txt` or `sitemap.xml`, you'll notice a /backup URI:
```
<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
  <url>
    <loc>https://csaw-2014.appspot.com/</loc>
    <lastmod>2014-01-01</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.5</priority>
  </url>
  <url>
    <loc>https://csaw-2014.appspot.com/auth1</loc>
    <lastmod>2014-01-01</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.5</priority>
  </url>
  <url>
    <loc>https://csaw-2014.appspot.com/backup</loc>
    <lastmod>2014-01-01</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.5</priority>
  </url>
</urlset>
```
The /backup URI will dump you a zlib-compressed text of a mysql session:
```
csaw2014 ~ # mysql -u root -p
Enter password:
Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 1021899
Server version: 5.5.32-log Source distribution

Copyright (c) 2000, 2014, Oracle and/or its affiliates. All rights reserved.

Oracle is a registered trademark of Oracle Corporation and/or its
affiliates. Other names may be trademarks of their respective
owners.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

mysql> use csaw2014;
Reading table information for completion of table and column names
You can turn off this feature to get a quicker startup with -A

Database changed
mysql> show tables;
+-----------------------+
| Tables_in_csaw2014    |
+-----------------------+
| csaw_auth             |
| csaw_data             |
| csaw_flag             |
+-----------------------+
3 rows in set (0.00 sec)

mysql> select * from csaw_auth;
+----+---------------+---------------------+--------------------------+-------------------+
| ID | auth_username | auth_password_crypt | auth_securid_seed        | auth_email        |
+----+---------------+---------------------+--------------------------+-------------------+
|  1 | jono          | ..0WZygs1WB7.       | dxeTnBVT1aEQWaUlk9zYBg== | jon@oberheide.org |
+----+---------------+---------------------+--------------------------+-------------------+
1 row in set (0.00 sec)
```
Note: this is actually fake mysql output, there's no database involved in the challenge. But hopefully people will see the csaw_flag table and get fooled into trying some SQLi. ;-)

So, you can crack that DES-crypted password pretty easily. Once you've done that, you can use that in the original web app login. Then you'll get a two-factor challenge.

The auth_securid_seed value in the DB dump is for a RSA SecurID token so you need to find out how to generate a valid passcode from that seed. Once you've done that, you're past the two-factor auth in the web app.

Next, there's a quick quiz Q&A with the following questions:
- what's the longest running hacker con in murica?
- what is one of the l0pht group's lesser-known mottos?
- what tv-personality-turned-hacker wrote an article on bypassing windows dep?
- what twitter account run by dino dai zovi is known for providing solid security advice?
- what's the square root of this apartment?

After you answer those, you get the flag!
## Setup
