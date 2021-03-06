Title: Building My Own Google Music With Hookers And Blow
Date: 2013-12-29T22:54-06:00
Tags: Technology, Google Music, Knockout, Javascript, Pyramid, Python
Slug: google-music-party-mode
Authors: Britt Gresham


When things do not work the way I want them to work I tend to build my own
version of whatever it is that wasn't working for me. In this case, it is
Google Music. Now Google Music is a fantastic service, and i'm not moving away
from it any time soon. It's just missing some features that other services do
so well. I have really missed the ease of playlist sharing that Spotify had or
iTunes's DJ playlist which turned your entire iTunes library into a party
playlist where your friends could put songs they wanted to hear into a queue
for everyone to vote on. The higher rated songs would be played first and then
the lower rated songs next. The whole interactive part of music is what I miss
the most by switching over to Google Music, So I'm going to be remedying it by
building my own Google music with these new features. Of course doing this
opens up a whole bunch of interesting problems, like where am I going to get
access to all of my Google Music files and playlists and how am I going to
manage restricting streaming to only one computer at a time.

I did some digging around on finding a library that let me talk to Google Music
programmatically and I found an unofficial library that warns you that it is
not endorsed by Google what so ever and should be used seldomly to not raise
any eyebrows at Google. Playing around with the library let me grab the mp3 to
stream it locally, which can pretty dangerous in the wrong hands since it could
technically just be saved to your hard drive and thats the end of that. That
brought up an interesting challenge for me because there was no way that I'm
going to be saving a bunch of music that I don't even own to my hard drive. And
at the same time I need to cache some of it for incase I want to re-listen to a
song a few hundred times (which happens more often than I care to admit). So
off to building the server, written in Python using the pyramid web framework.
I checked out sending temporary files back via a regular request and I found a
builtin python module for handling temporary files called tempfile. It creates
"file-like" objects that you can manipulate as if they were any regular file
except when they are closed they are automatically destroyed. When a request
comes in for a new song to stream I hand that off to the google music api to
retrieve the song and throw the mp3 into a temporary file. I take that file and
package it inside of pyramid's "FileResponse" container and cache that for an
hour in memory. Now to lock down all of the computers that have access to the
stream I implement my own authentication within pyramid and only let one user
account in with a randomly generated auth-token stored in the form of a cookie.
When User A requests the site for the first time they are prompted with a login
page and upon successful login the server randomly generates a token and marks
that token as the one that is allowed to be streaming music. When User B tries
to request a song the token doesn't match up with the one allowed and it
rejects the request right there.

For now I don't plan on having more than one user account so I am keeping the
login associated with the Google account that is powering the server with
Google Music access. There is a lot of things I am wanting to implement on the
server side but I needed things to be polished up on the front end before
continuing on the backend. Some of the challenges I am facing on the front end
so far are problems with libraries and looks.  Knockout.js, the MVVM library
I'm using to power the frontend, seems to have a problem with lots of data if
not handled correctly. When I was retrieving a list of songs from the back end
I was pushing each new song object onto a knockout observable array filled with
all the songs that the client knew of.  Every time an observable or observable
array is updated it causes a refresh event to happen which then reevaluates
everywhere where that observable variable or observable array is referenced.
Whether that be in the DOM or in any dependant functions. This gets expensive
after you load about 500 items into the array because it reevaluates for all of
the objects in the array every time you push one object onto it. I was
experiencing the tab hanging for a good 4-5 minutes and that was not going to
work for me or anyone else for that matter. A much better way of going about
this problem was to fill a normal array with the items and then initialize the
observable array with all of the items from the original array into it.
Therefore only one refresh event is called and the DOM updates with all 5500
records in a few seconds. I have pagination written into the API but I am not
using it on the front end yet because I was focusing on other things. One of
the other interesting things that I had to deal with was how to seamlessly play
tracks together.

I'm using the web audio api to play the music in the browser and it is really
great at letting you had full control over the audio that you are manipulating
but you need to give it time to warm up. The browser has to download the 5-10mb
music file and decode it into an array buffer so that it can be attached to a
source node and played through the speakers of the computer. Keeping that
system in balance is interesting because I don't want to load songs immediately
and I also don't want to load them too late. When about half the song is
completed I start loading the next few songs that have not loaded yet, up to 2
preloaded songs. As soon as there is about 1 second left of play time on the
currently playing song I make it so that the user can no longer switch the next
playing song and I begin prestaging the decoded audio buffer of the next song
for showtime. You can setup a source node to start playing at so I set it to
where the end of the song is minus about 9/10ths of a second since i've noticed
there is a little bit of lag between when you schedule the song to play and
when the song actually starts playing. I read that the delay can be about 1/5th
a second but I add in a few extra tenths of seconds because the client is set
to crossfade between songs which largely masks the pause that you would hear
otherwise. I'm not super satisfied with picking the 9/10ths number and I have a
few ideas that i've been tossing around in my head to get a more accurate idea
of when a song should start playing, i've just been trying to get a bunch of
front end things all taken care of.

One of the design choices that I made was to have everything revolve around the
main song queue. The main song queue only consists of the songs that are going
to be played and not the song that is actually playing. When you want to play a
song you have to push it into the queue where it waits until all of the
conditions are right (It has its audio buffer downloaded and decoded and there
is no currently playing song) before it is pushed into the currently playing
slot. Doing things like pressing next or previous are all done through
modifying the queue. So when you want to skip to the next song I remove the
currently playing song and shift the first item into the currently playing
slot, that is of course after the song in the queue lets you know it is ready
to be played. Going back a song is just removing the currently playing song
from its slot and taking the previously played song and pushing it to the top
of the queue where it will wait until the song in the queue is ready to be
played. Doing things this way lets you keep an accurate history of every song
that you have played and it makes creating actions very easy. You are able to
create an infinite playlist by pushing things onto the queue when the queue
size has dropped below a certain number. One other advantage of a queue is it
can be used as your voting system automatically by simply moving things around
in the queue based on vote weight. If you are interested in seeing what I have
so far checkout the project at <a
href="https://github.com/demophoon/Google-Music-Party-Mode">https://github.com/demophoon/Google-Music-Party-Mode</a>.

There is still a lot of things that I need to add to get it to where I want it
to be like mobile so that anyone can vote on a song. Anyways, i'm going to call
it a night.
