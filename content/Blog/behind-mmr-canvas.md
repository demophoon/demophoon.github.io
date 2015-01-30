Title: Behind the Canvas in Music Music Revolution
Date: 2012-09-16T20:53-06:00
Modified: 2015-01-29T21:01-08:00
Tags: Technology, Html5, Games, Web Audio Api, Javascript, Canvas
Slug: behind-mmr-canvas
Authors: Britt Gresham

Last week I wrote about how the I was able to use the Web Audio API in my game
Music Music Revolution. This week I am going to tie it all back into creating
the visuals for the game and the troubles I ran into with that.

Lets start by defining the Canvas element for anyone who has not had experience
with it. The canvas is exactly what it sounds like. It is a blank canvas that
you can paint onto with any colors, brushes, or pictures you desire. They can
be represented in either a 2D space or a 3D space with WebGL. To create the
canvas you simply create an empty canvas tag and then select it using
javascript.

    :::html <script type="text/javascript"> var canvas =
    document.getElementById("canvas"); var ctx = canvas.getContext("2d");
    </script>

    <canvas id="canvas"></canvas>

Now that we have the 2d context of the canvas element stored in the ctx
variable we can now start painting the canvas with what we want. I started off
by placing a background picture onto the canvas that I had created in
Photoshop. Then overlaying some text about the game such as version number. I
took the waveforms that were created from the second Web Audio Analyzer node
and draw the waveform onto the canvas. I place a semi-transparent black box
over the play field to separate the background animations from the actual
gameplay to make it less distracting to the player. I place the yellow hit
boxes and that is basically everything that will always be there.

The first audio analyzer sends me the beats a second before the user hears them
so I can calculate the distance I need to have each beat travel from its origin
to the final destination point at the yellow hit box. Now I had first just
calculated each movement with frames. I figured if I traveled 5 pixel downward
for each frame I drew then the beat would hit exactly 300 pixels from the
origin point if drawn at 60 frames per second. This method is horribly
ineffective because some frames may take longer to render than others and would
cause the beat to fall anywhere from 5-30 frames off and the latency is
definitely noticeable when you try to compete with the natural beat detection
that the brain is capable of. I ended up changing the method up to give me the
precise second that the beat would occur after the start of the song. I was
able to calculate where the beat needed to be at any given moment. and draw it
there whenever the draw() method was called. Other than that the visuals were
pretty easy to create, I still want to do more than just the simple waveform in
the background. I have another project that I had worked on a really long time
ago that I will probably do some code reuse and implement the visual effects I
had created for my web-based iTunes remote controller.
