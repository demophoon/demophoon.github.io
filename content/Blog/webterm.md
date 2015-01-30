Title: Bringing a Disposable Terminal to the Browser
Date: 2014-05-27T22:27-06:00
Modified: 2015-01-29T22:27-08:00
Tags: Technology, Webvim, Vim, Terminal, Websockets, Html 5
Slug: webvim
Authors: Britt Gresham


A few weeks ago I was playing around with some new technology in the web
browser. I had always wanted to show off my vim configurations in some sort of
fashion and I had written a lot of really sweet web applications so I figured
why not show off my vim config in the browser.

The problem that I was faced with was how to get a good user experience in the
web browser without rewriting vim in in javascript, since many have tried and
have not quite gotten it right. I moved to my next solution, bring vim to the
browser by streaming a terminal to it! This task was far more interesting to me
because it went past just streaming vim, but all terminal applications to the
web browser! So I did exactly that!

### Removed for now... Awaiting Webvim Version 1.0...

What you see above is a real, live terminal. Running a real instance of vim.
Everything works as it is suppose to work just like you were sitting in front
of a terminal. I am using a few libraries that <a
href="https://github.com/liftoff/GateOne">GateOne</a> utilize in their
application and adapting it to spin up docker containers. I then monitor the
output of the container and send any changes to the web browser in near
real-time using websockets. Each container is set to run for 30 minutes before
terminating itself, I've also disabled networking in the containers so that my
server is not used in some botnet. So what about security? Cannot people just
escape out of vim using ":!bash"? Well yes, but I'm not too worried about it
and i'll tell you why.

Docker allows me to have very lightweight linux containers that boot in a
second or two. In fact, if you are visiting the website for the first time the
container that you are currently connected to was spun as you loaded the page.
These containers are sandboxed off from each other and the host system. Only I
can specify the type of interactivity each container can have with the each
other or the host system. I'm using a program called timelimit to automatically
kill vim after 30 minutes as well so that the servers resources do not get
eaten up by your session. This keeps thing moving along quite nicely. Sure
people can go ahead and escape out of vim with ^z or :!bash but since its
sandboxed off and networking is disabled there is very little that you could do
to harm the actual host machine (which is an amazon box dedicated to this demo
and <a href="http://www.brittg.sexy/">http://www.brittg.sexy/</a>). Also when
you connect to a webvim session you get a unique identifier that connects you
to your docker container. You can share the link that the website redirects you
to with your friends and all share the same docker container or have them get
their own containers by giving them the base url (<a
href="http://www.brittg.sexy/">http://www.brittg.sexy/</a>).

I also found a really neat terminal emulator for the web browser, also used by
gateone, called <a href="https://github.com/chjj/term.js/">term.js</a>. I
discovered that I could send raw terminal data to it and it would be rendered
properly. This made the browser part super easy. All I needed to do is write in
screen resizing and an auto disconnect after 10 minutes of inactivity and I was
done with the front end.

If you would like to see this project in its final state check it out at <a
href="http://www.brittg.sexy/">http://www.brittg.sexy/</a>. The code for the
project is out on github at <a
href="https://github.com/demophoon/webvim">https://github.com/demophoon/webvim</a>.
Feel free to pull it down and make it your own! I've got my own personal webvim
server stood up that lets me share bash prompts with others so that I can show
off the rest of my configurations while everyone is on their own personal
devices.
