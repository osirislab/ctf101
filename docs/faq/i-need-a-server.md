# I need a server

Occasionally, certain kinds of exploits will require a server to connect back to. Some examples are connect back shellcode, cross site request forgery (CSRF), or blind cross site scripting (XSS).

## I just need a web server

If you just need a web server to host simple static websites or check access logs, we recommend using [PythonAnywhere](https://www.pythonanywhere.com/) to host a simple web application. You can program a simple web application in popular Python web frameworks (e.g. Flask) and host it there for free.

## I need MY server to be the server

A simple solution to forward your local development environment into a routable endpoint is [ngrok](https://ngrok.com/docs/guides/share-localhost/overview). You can share localhost to anyone on the internet.

!!! Note
    Obviously comes with the caveat of securing your own ecosystem. While an effective tool for developers to share their environment without having to deal with routing, it shouldn't be used for production environments.

## I need a real server

If you need a real server (perhaps to run complex calculations or for shellcode to connect back to), we recommend [DigitalOcean](https://www.digitalocean.com/). [DigitalOcean](https://www.digitalocean.com/) has a cheap $4-6/month plan for a small server that can be freely configured to do whatever you need.
