# Guestbook
## Author
Toews
## Points
300
## Category
Web
## Description
[https://csaw-guestbook.herokuapp.com/](https://csaw-guestbook.herokuapp.com/)
## Flag
`flag{octocat-d08b319374e5}`
## Solution
This is a DOM XSS vulnerability in a guestbook application. There is a PhantomJS script that is logged in as the admin user and visits the page once per minute to approve/deny posts. The approve/deny functionality is done over XHR. To build the URL for the XHR request, JavaScript in the page pulls a URL out of an element in the page. The response from the XHR request (success/failure) is then injected into the page.
The attacker is able to post messages to the guestbook formatted using markdown. This is then converted to HTML after being run through some HTML sanitization. The HTML sanitization allows the user to set a class attribute on HTML tags. This can be used to trick the approve/deny JavaScript into making the XHR request to an attacker controlled page. The attacker can have this page return arbitrary HTML/JS, leading to XSS.
With this XSS, the attacker needs to execute JavaScript to make the admin user post a message with their name in it.
I don't know how hard of challenges you guys are going for, but I could scale this a bit either way.
I could also change the application to give a code to the user once they solve the challenge. Would that need to be a unique code per user, or just a single code.
Let me know if I can clarify anything.
## Setup
