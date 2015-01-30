Title: Web Sockets and You
Date: 2012-10-21T20:12-06:00
Tags: Technology, Javascript, Websockets, Html 5, Python, Autobahn
Slug: websockets
Authors: Britt Gresham

Over this last week I learned about what web can exactly do. We developers use
sockets to transmit or receive data over a network by listening for, or sending
to, another computer or program. As long as the socket remains open information
can flow freely. Now setting this up in a program can be fairly easy, but when
you start experimenting with the new Web Sockets protocol that has been built
into the modern web browser, *cough* Google Chrome, things can get tricky fast.
When I dove into the world of web sockets I discovered that if I wanted to
write my own web socket server I'd have to end up writing my own TCP handshake
function to establish a connection with the client, in this case Google Chrome
running locally on my laptop. I had not done any key generation to make sure
that the socket was encrypted before so I started my hunt for a module that
would allow python to act as a web socket server. I found
[Autobahn](http://autobahn.ws/) and it easily let me setup a server from which
to send and receive data from. Once the test echo server was running I quickly
wrote up a sample webpage that could send a message to the server. A connection
had been established to the server when the page had loaded which meant that
the server was listening and waiting patiently for me to send a message. I sent
the message "Hello" and instantly "Hello" was sent back to me. Without any new
requests being made to the server since I had already established a connection
from the start. This technique can be used for simply speeding up web
applications or creating a complex online multiplayer game. Unfortunately for
us, Web Sockets are still in draft and It may be years for it to become a
standard in web browsers, but for the web browsers that support it they can
take full advantage of its sheer awesome technologies.
