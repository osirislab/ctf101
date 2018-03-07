# Herpderper
## Author

## Points
300
## Category
Web
## Description

## Flag
`Yo dawg I heard you leik to derp so i put a herp in your derp so you could herpderp while you derpderp`
## Solution
The challenge is an Android application that presents users with a login form. They input a set of credentials and hit login. The server will evaluate their response and send back a JSON-formatted message that the client will interpret two values out of and let the user know that their login was either a success or failure, along with a secondary message. The end goal for a user playing is to intercept communication from the client to the server. There's a basic web application logic bug in the JSON response (more on this later) that they won't be able to solve unless they're able to man-in-the-middle the client.
The application uses SSL with a custom Android TrustManager. Instead of checking the validity of a certificate based on the root certificate that signed it, the application is merely checking the issuer's DN string, the certificate's DN string, and the serial number of the certificate's serial number for hard-coded static values. Standard MITM tools will not work out of the box. One way around this would be for a user to generate their own CA and certificate using openssl, bundle it into a pkcs12 file, and use it with Burp. There are several hints within the application itself that would hint that there is something goofy about how the application is determining trust. 1) if a user hits https://webchal.isis.poly.edu, their browser will not trust it. 2) if a user pulls apart the installation package, there are no CA certificates bundled with it 3) there are DN strings embedded in the application.
To deter the user from debugging or modifying the application, there are a few anti-tampering mechanisms in place. To prevent debugging (which is possible on a rooted device or on the Android emulator), there is a call to isDebuggerConnected() embedded in a few key functions. If a debugger is connected, the application will throw an unhandled exception and crash. To prevent the user from modifying the application, one of the tokens that the client sends to the server is an "integrityid" token. This token is actually the signature of the certificate used to sign the installation package. If a user modifies and repackages the application, this token will be different and a server-side check will produce an error informing the user of a client integrity fault. It's ok for a user to go this route, and they can... there are just a lot of things to patch and it will ultimately be "the hard way" to see what the application is doing.
So, the user needs to MITM the SSL connection. Once they do, what they will see is a post message on the client side that looks something like:
```
identity=<base64-encoded username>&secret=<base64-encoded password>&integrityid=<sig>
```
The response will look something like:
```
{"response":{"status":"failure","msg":"Login failed"},"timeStamp":"<time>","tZ":"America/New_York","reqResourceId":"webchal.isis.poly.edu","clientId":{"identitySig":"<sha1 hash of their username>","role":"anonymous","accessToken":"YXNkZkBhc2RmOmFub255bW91czp3ZWJjaGFsLmlzaXMucG9seS5lZHU="}}
```
That last item, the accessToken value, is a base64'ed ASCII string that looks like:
```
<username>:anonymous:webchal.isis.poly.edu
```
A user should see that "anonymous" corresponds to the "role" value of the main body response. Users should also note that the username that they submitted was called "identity" and was a base64'ed string and is referenced in the response by "identitySig". The user should assume that the access token is something that they can manipulate, play around with this, and attempt to submit a request with a "role" value in it:
```
 curl -i -3 -k -d "identity=<base64-encoded username>&secret=<base64-encoded password>&integrityid=<sig>&role=<base64-encoded value of "admin>" https://webchal.isis.poly.edu
```
If they submit a "role" parameter with something other than admin, the JSON response will be whatever the user submitted, so they should understand that theyre going down the right path. And sure enough, if they do submit "admin", they will win:
```
{"response":{"status":"success","msg":"Key: Yo dawg I heard you leik to derp so i put a herp in your derp so you could herpderp while you derpderp"},"timeStamp":"1379170216","tZ":"America/New_York","reqResourceId":"webchal.isis.poly.edu","clientId":{"identitySig":"af7f9454383269d7e4fbddc70151a87df37ebc02","role":"admin","accessToken":"YXNkZkBhc2RmOmFkbWluOndlYmNoYWwuaXNpcy5wb2x5LmVkdQ=="}}
```
Please use the key that I include in that response as the key. I'm not sure what I would value this from a point perspective... it should be a higher value, because its a multi-step problem. It's probably not a highest level difficulty challenge either.
## Setup
Distribute `herpderper.apk`
## Notes
For people that need to get going with the SSL stuff: "Have you accessed the web server from a browser?"
If people are getting stuck trying to recompile the application: "Android debugging might be more trouble than its worth"
For people that get all the way to the end and can't get over the web bug: "Simple web bugs are simple."