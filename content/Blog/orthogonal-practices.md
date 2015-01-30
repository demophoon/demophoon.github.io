Title: Orthogonal Practices
Date: 2012-09-23T16:33-06:00
Tags: Technology, Self Help
Slug: orthogonal-practices
Authors: Britt Gresham

Back in middle school I had gotten a BASIC stamp board to have some nice fun
with. I learned what it took to make a very simple program work with LED's,
displays, buttons, sensors, and just about everything else I could get my hands
on to. It was a lot of fun when I had simple tasks that I wanted to accomplish.
I moved on into high school to take that BASIC programming knowledge that had
learned and applied it to the programming classes I had. Learning all about the
different types of libraries I could use and how to use them, but never how to
implement my own libraries. Maybe this was something that was suppose to be
left to my college experiences but it is something that is key to developing
orthogonal programs.

An orthogonal design is one where you keep a small number of components that
have a small number of dependencies between one another so that you can add or
change functionality in a program without needing to make a ton of code
changes. It was a concept that I had read about in *The
Pragmatic Programmer* but had never actively implemented anywhere
in my code until recently. The last project I worked on was the Music Music
Revolution Html5 game and I wanted to take an orthogonal approach to it because
I find myself making a ton of changes in my code just to get one function to
work how I would want it to work. By separating out the key features in the
game like gameplay, background, the beat detection system, main menus, and the
transitions between the screens I am able to add any sort of functionality to
the game in a very small amount of code changes. Lets just say that I wanted to
take the gameplay out of the mix and only have an Html5 based music visualizer.
Well before I had learned what orthogonality was I'd have to make tons of
changes everywhere in my code just to make it all work together. I'd end up
rewriting the entire engine since I'd have the methods that would start/play
the music and calculate beats merged together. The drawing functions would be a
mess trying to figure out where each hit box would have gone. It just would
have been a complete disaster of incoherent function calls that I would have
just scrapped anyways. (I had tried this project before when I had created a
music visualizer in a non-orthogonal way.)

Yesterday I rewrote bits and pieces of the application so that if I ever wanted
to make a music visualizer out of it I could just comment out the line that
draws any gameplay. The game would not even know, nor would it care. And that
is the beauty of it! I am able to remove an entire chunk of the game and
nothing falls apart because the beat analysis algorithms do not care what is
showing up on screen. It only cares about what it needs to care about, the
music and the beats. Same goes for the scoring system or the menus. They don't
care about what is going on with any other part of the program. Same with if I
wanted to scrap the beat detection functions. If I had removed it the worst
that would happen is there would be no beats on the screen. The game would
function exactly as I'd expect it to work without getting a run-time error
because `getBeat()` was not declared.

It is 110% recommended by me to take this approach to developing programs
because you don't always know what you want to have in the end but you always
want an easy way to get there.
