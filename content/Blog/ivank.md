Title: IvanK Lib and Enhancing Canvas Elements With WebGl
Date: 2013-06-02T21:28-06:00
Tags: Technology, Javascript, Html 5, WebGL, Canvas, IvanK
Slug: ivank
Authors: Britt Gresham


Now a while back I was introduced to <a href="http://www.opusthegame.com"
target="_blank">Opus the Game</a> and it really sparked my interest just as
music related games do for me. The concept was something that I had seen before
in many games prior but nothing I had seen before was built to be played in the
web browser. I wondered what code could be driving this game and I
right-clicked to view the source and thats when my hopes and dreams were
shattered. It was written in Flash. This made a large part of me feel disgusted
because there was so much room for improvement as Flash is quickly being
replaced with Html5. This last month or so I have spent a decent amount of time
working with the IvanK javascript library that is built to help Actionscript
and Flash developers transition over to Html5 using the canvas element and I
was able to create my own rendition of Opus using purely Html5 Apis and tools.
Now before I show you my version of the game (which is very alpha by the way)
i'd like to first tell you about some of the great key features that I found
with IvanK.js. First of all, it is incredibly small, only 50kb! that is hardly
the size of a tiny picture which is an instant download on most phones that
don't already have a cached copy from a CDN. Next the library is very feature
rich coming with hit detection built right into the extensible sprite objects
you can create. And lastly this library makes use of WebGl to render 2D
graphics onto the canvas element. Now the traditional use of WebGl is to render
3D images onto a canvas element using the hardware so when you are using the
same technology to render 2D you  get a massive performance boost. One of the
downsides that I did run into with the library was that the documentation is a
bit lacking and in order to dive in quickly you will have to parse through some
Actionscript documentation and figure out what works and what doesn't work but
other than that everything else was a really fun experiment. Anyways, if you
would like to see what I have done with recreating Opus the Game in Html5 visit
<a href="http://brittg.com/mw" target="_blank">http://brittg.com/mw</a> and
test out the demo (Latest version of Chrome only as the Web Audio Api is only
supported in Chrome). There are still a few screens missing but it gets the
concepts down to how extensible and applicable the library is to someone who
has very minimal experience in Actionscript.
