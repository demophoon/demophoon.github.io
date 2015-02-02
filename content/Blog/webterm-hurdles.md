Title: Tornado over Pyramid for Webvim
Date: 2015-02-01T18:52-08:00
Tags: Technology, Webvim, Vim, Terminal, Pyramid, Tornado
Slug: webvim-tornado
Authors: Britt Gresham

So I've done a lot of work getting Webvim to the state that it currently is at
right now. Along the way I ran into some very interesting problems that needed
to be solved in order to get the 1.0 release out.

Refactor
--------

This started off with a complete refactor of the back end technology to stop
using Pyramid and switch over to a lighter weight server called Tornado. I
realized that I was using Pyramid in the complete wrong way, mainly for serving
up static content with most of the functionality being taken care of in the
`termio` and `terminal` python modules as well as the front end logic being
handled by the javascript that I wrote. Pyramid was essentially a glorified
cookie/session manager that just happened to have websocket capabilities.

In comes Tornado's IOLoop Reactor
---------------------------------

When I was digging into [GateOne's](https://github.com/liftoff/GateOne) codebase
in my attempt to not have to write my own terminal emulator and multiplexor I
noticed that there was a callback mechanism that was built in to both
components. Being very familiar with callbacks knowing javascript this was
something that intrigued me and would have come in very nicely so that I don't
have to guess when the terminal was updated by the program. The only caveat was
that you needed to be using the libraries with Tornado and at the time I was
lazy and wanted to stick to something I knew, which was Pyramid.

After considering moving over to something lighter weight I installed Tornado
and began refactoring. Before what I had done to get the terminal working in a
close to realtime fashion was to have a while true loop running constantly
checking for updated to the terminal every tenth of a second. Seeing that my
reactor was very *homegrown* and slow when I moved to Tornado I saw massive
improvements in speed and performance since the absolute best latency you could
get was 100ms between pushing the key and getting a response from the server.

With Tornado being lighter weight the startup time was significantly reduced. I
also could focus less on the framework aspect of Pyramid and focus on more of
the code itself that was driving webvim. Also with way fewer dependencies,
installation takes no time. All of these wins, big and small, made me very happy
with the result.
