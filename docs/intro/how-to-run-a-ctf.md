# How do I run a CTF?

> "Is it really a CTF if you don't solve the infrastructure problem in the 24 hours before the competition?"

## Before you start

Consider a few of the following before starting a CTF.

- How many people will play in my CTF?
- What type of challenges do I want to write?
- How do you want to host your challenges?
- What is my budget?

## Challenge Writing

## Infrastructure

Depending on the size of your competition, you're going to need different types of deployments. Generally, you'll need a [load balancer](https://en.wikipedia.org/wiki/Load_balancing_(computing)) to work concurrently with your web application.

!!! info
    When we ran CSAW'23, there were over 2500 teams of ~4 people. You can try to gauge how many users your competition might have before writing a deployment. 

## **Open Source Frameworks**

### [CTFd](https://docs.ctfd.io) 

CTFd makes it easy to spin up an instance able to support a CTF at any time. Starting a local server is as easy as:

``` bash
docker run -p 8000:8000 -it ctfd/ctfd # (1)
```



1.  For more information on Docker, read the [docs](https://docs.docker.com/)!

### [kCTF](https://google.github.io/kctf/)

kCTF is a framework written by Google built on Kubernetes. It has built in load balancing at the platform level. 


### [rCTF](https://rctf.redpwn.net/)

Written by the redPWN CTF team, rCTF has a separate CI/CD module for supporting challenge deployment as well.

```bash
curl https://get.rctf.redpwn.net | sh
```


## **Paid CTF Hosting**

### [CTFd Enterprise](https://ctfd.io/pricing/)

- Three-tiered pricing service with hosting services and on-call support. 
- Supports professional workshops generally reserved for industry security teams exercises.


### [Hack the Box CTF](https://www.hackthebox.com/business/business-ctf)
