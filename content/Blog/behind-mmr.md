Title: Behind the Audio in Music Music Revolution
Date: 2012-09-06T20:53-06:00
Modified: 2015-01-29T20:34-08:00
Tags: Technology, Html5, Games, Web Audio Api, Javascript
Slug: behind-mmr
Authors: Britt Gresham

I spent a large majority of last week working on a project I called 'Music
Music Revolution' based off of the popular '[Dance Dance
Revolution](http://en.wikipedia.org/wiki/Dance_Dance_Revolution)' and inspired
by [Beats](http://en.wikipedia.org/wiki/Beats_(video_game)) for Sonys PSP. I
had always wanted to play a game similar to these two games except, it had to
be on the PC. <!--more-->My hunt for the game I had very much desired to play I
ran across many other games that incorporated music into the game play by
generating enemies with the beat of the music or moving a mouse to the beat of
the music, which is in my opinion very awkward. What I wanted needed to feel
more natural to tapping on the beats of the music. I had decided that I
couldn't find a game that quite captured what I had wanted out of it so I made
my own!

![Music Music Revolution Gameplay]({filename}/static/images/gameplay.png)

Music Music Revolution is a Html 5 creation that uses a few very experimental
API's together to create the experience I was looking for. Now, it is very far
from perfect, but none the less, I am very proud of where it has come. The Web
Audio API, implemented in Google Chrome, allows the developer access to the low
level data that a simple &lt;audio&gt; tag cannot grasp. It is much different
in almost every way from the &lt;audio&gt; tag as well. Instead of specifying a
.Mp3 file in a src property within the tag, you download the .Mp3 as an
'arraybuffer' using an XMLHttpRequest. An arraybuffer is just the data type
that tells the javascript that it is not downloading JSON or XML, but an actual
binary file. This arraybuffer is then passed along into a method spawned from
the Web Audio API called decodeAudioData which asynchronously decodes the audio
file into a buffer that will eventually be used to play through the speakers,
but not before we get what we want out of it first. The buffer then attaches to
audioNodes which manipulate the audio using filters and equalizers and can also
give us the real low level data we really want. These audioNodes consist of
things such as high pass filters, low pass filters, normalizers, delays, gain,
attack, splitters, ect ect ect. Basically the building blocks of any audio
system, and we have complete access to it all! Just that fact alone makes me
giddy with the possibilities. The audio passes through a splitter to give me
one feed for the beat detection algorithm and the other for the sound that the
end user hears. The beat detection path sends the audio through both a high and
a low pass filter to help amplify the bass and treble of the song to make it
easier for beats to be detected. Then the [FFT
Spectrum](http://en.wikipedia.org/wiki/Spectrum_analyzer) is analysed to
determine where the beat is in the song. That information is relayed to the
actual game where the hit block is generated displayed to the user. The second
audio path is sent through a one second delay node so that the computer is able
to predict when the beats are before the user hears them. After the one second
delay the waveform is taken from the audio and generated in the background of
the game for a nice effect. Now because the beats are detected on the spot I
was able to allow users to play with their own .Mp3, .ogg, and .wav files which
is much better than having to time everything just perfect and store that as
a separate file for each individual song.

Here is a visual in case you'd like to have a look. [Journey of the
Audio](https://docs.google.com/open?id=0B2EyzGxnwZQuY3AxN2NTblhjck0)

Also, the game can be found here at
[http://music.brittg.com/](http://music.brittg.com/). Please let me know if you
find any bugs in the comments below or in an email found on the game's website!

I plan on writing a little more about how everything comes together, including
the File IO API, Beat detection algorithms, and the challenges of using the
Canvas element for actual game.
