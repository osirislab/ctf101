# Gopherz2Basic

By Kent Ma & Leon Chou



```
OSIRIS Laboratory                                                  K. Ma
Request for Comments: 42031337                                   L. Chou
Obsoletes: 1436                                      New York University
                                                            October 2107


           The Internet Gopher Protocol Version 2 (Gopher/2)

Status of This Memo

   This memo specifies an Internet standards track protocol for the
   Internet community. This document describes the protocol, lists some
   of the implementations currently available, and has an overview of
   how to implement new client and server applications.


Abstract

   This specification describes a modernized expression of the semantics
   of the Gopher Internet protocol, referred to as Gopher version 2
   (Gopher/2).

   This specification obsoletes version 1 of the Internet Gopher
   Protocol.


1. Introduction

   The Internet Gopher protocol is a wildly successful protocol.
   It is currently the primary communications mechanisms for people
   across the world. However it is missing several core mechanisms
   for guaranteeing security. Additionally, it is lacking capabilities
   for user interfaces and modern web document formatting.

   The Gopher/2 defines a key exchange protocol for safe, end-to-end
   encryption. Additionally, it defines a GopherText format for rendering
   webpages.

   The Internet Gopher/2 protocol and software follow a client-server
   model. This model assumes reliable data stream; TCP is assumed.
   Gopher/2 servers should listen on port 433. Documents reside on many
   autonomous servers on the Internet. Users run client software on
   their desktop, connecting to a server and completing a verification
   process before sending the server a selector (a line of text, which
   may not be empty) via a TCP connection at a well-known port. The server
   responds with a block of text and closes the connection.

   Servers return documents. The first line of the response contains the
   type of the document and 4-byte big endian length of the document encoded in
   hex and subsequent lines contain the contents of the document terminated by
   end of file.

   The GopherText format contains a list of Gopher/2 routes which the
   client will then recursively request.


2. The Internet Gopher/2 Model
   Gopher/2 provides an optimized transport for Gopher semantics.
   It supports all of the core features of Gopher but aims to be more
   secure in several ways.

   In essence, the Gopher protocol consists of a client connecting to a
   server and sending the server a selector (a line of text, which may not
   be empty) via a TCP connection.


3. Gopher/2 Protocol Overview

   In this simple example, the client establishes a connection and
   requests the base page of the server.

    {Client and server negotiate encryption key (See section 3.1)}
    Client: {Sends a single forward slash Meaning "List what you have"}
    /
    Server: {Sends a series of lines, each ending in CR LF}
    P17
    T Welcome to our page
    {Server closes connection}


3.1. Connection Handshake

   Connection will be established with a diffie-hellman key exchange.
   This will establish the encryption key for subsequent communication
   between client and server.

   In the diffie-hellman exchange, let p = 251 and g = 6

  Client: {Opens connection to web.chal.csaw.io at port 433 and
           sends diffie-hellman A value.}
  Server: {Accepts connection and says diffie hellman B value}
  {Communication continues with messages encrypted by coordinated key}

   The communication will be encrypted with repeated key xor using the
   shared secret established by diffie hellman.


3.2. Client Requests

   Media item requests:

  <Selector>    <Key/Values...>
  /asdffile     Token1:ade912e4912b1c ...


3.3. Server responses

   The first line in a server response will be the item type followed by
   the length of the return value encoded in hex. Subsequent lines will
   be the content of the page. The following are the server response
   types.

  P   Item is a GopherText page
  G   Item is a GIF format graphics file.
  I   Item is some kind of image file.
  S   Item is sound file (especially the WAV format).
  F   Item is a file.


   In the following example, the client requests a page on the server
   with a token as an argument. The page the server returns will have a
   Gopher2 media file in it. The client will reestablish another
   connection to get the contents from the server.

  {Client and server negotiate encryption key (See section 3.1)}
  Client: {Sends magic string and session tokens}
  /index username:uname sessionToken:eae12ade
  Server: {Sends a series of lines, each ending in CR LF}
  P41
  T Welcome to our page, uname
  I /imagename/png web.chal.csaw.io  433
  {Connection closes}

  {Client and server negotiate encryption key (See section 3.1)}
  Client: {Sends a request for the image}
  /imagename/png  username:uname sessionToken:eae12ade
  Server: {Responds with file type and contents of PNG}
  IDEAD
  .PNG....
  {Connection closes}


4. GopherText Pages

   The client software decides what items are available by looking at the
   first character of each line in a directory listing. Augmenting this
   list can extend the protocol.


4.1. GopherText Static Text Types
   A list of defined item-type characters. The client will decide how to
   handle distinctions between text types.

   Text type is formatted as follows:

  <Item Type> <Text>

   The following are the available text types:

  T   Text
  E   Error


4.2. GopherText Media Types

   Used as this:

  <Item Type> <Selector> <Hostname>       <Port> <Key/Values...>
  I           /asdf/png  web.chal.csaw.io 433    Token1:a912e4912b1c ...

  Where the Selector also defines how the client will download the file.
  E.g. /asdf/png will be downloaded as asdf.png
  The client is disallowed from downloading files above the client's directory
  for security purposes.

   These are the following media item types.

  G   Item is a GIF format graphics file. Client fetches and decides how
       to display.
  I   Item is some kind of image file. Client fetches and decides how to
       display.
  S   Item is sound file (especially the WAV format). Client will fetch
       and play.
  F   Item is a file. Client will fetch and download.
  L   Item is a link to another Gopher/2 page.
  P   Item is a nested browsing context. Client will fetch and render
      as nested client.


4.3. Session Storage Types

   GopherText pages can return session storage entries to set Session
   cookies on the client. The client will store it and append it to other
   requests to the same server.

  C  <Key>:<Value>        <Key>:<Value>       ...
  C  Token1:Token1Value   Token2:Token2Value  ...


Security Considerations

   Gopher/2 addresses security issues by defining standards for
   implementation of it's client and server with emphasis on cutting-edge
   best advancements for cyber-security such as cyber-security through
   obscurity, cyber-security through litigation, and cyber-security
   through libel.


Examples

   An example implementation of Gopher/2 is available at

      gopher://web.chal.csaw.io
```
## Topics Covered

## Additional Information

