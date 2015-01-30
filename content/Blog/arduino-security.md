Title: Arduino Security System
Date: 2013-01-06T23:44-06:00
Tags: Technology, Arduino, Home Security, Python, PySerial
Slug: arduino-security-system
Authors: Britt Gresham

Some of you may know that I am planning on moving out on my own and getting an
apartment with a good friend of mine. Knowing this well before I move out I
decided to put some of my programming skills to the challenge of designing and
programming my own security system with an Arduino. I had collected a few PIR
motion detectors over the years, they just needed to be hooked up.

Before I started work I had an idea, I wanted the system to be connected to the
internet so that I could arm it or disarm it from anywhere. Also I should be
able to view the status of the system af any given time. I had connected an
Arduino to a web server before as a simple weather station but it was only one
way communication to get the tempurature and barometric pressure to me, not the
two way communication that I needed to send commands to it. Also if the sensors
had been tripped then I'd need some way to alert me of the offense so that I
can act appropriately. I'd need to be able to handle events as events instead
of polling the device every so often. Using the PySerial library I am able to
send and recieve commands to the Arduino since it communicates via serial. I
did some investigation beforehand and found that whenever I ran the command
"serial.readline()" the function would block execution until a line was passed
back from the Arduino. This was immediately a problem because I could not send
the arm command to the device until after I received a line. Also If the device
malfunctioned then Python would have no idea and would most likely run without
being able to communicate to the Arduino. I debated on whether I should have a
"Ping-pong" type of communication where the web server would send a Ping
command asking for the current state of the Arduino and the Arduino would
respond with a Pong and the current state but that doesn't get rid of the
blocking problem that I had before. Knowing a little bit about how Python's
threading module works I decided to create two separate threads to handle
sending and receiving data separately. The threads run non-blocked even when a
function within the thread itself is blocking execution so the web server can
continue to run without a problem. I created a global state variable so that
the receiving thread could automatically update the state variable whenever it
needed and everyone else could peek at that variable if they needed. Also the
Arduino was setup to send the state back each and every time it's state was
changed (e.g. someone set off a sensor, the system was armed or disarmed, ect).

I created the serial initialization code and the threads inside of the
`__init__.py` file of my Arduino Pyramid project so that whenever I started the
web server the first thing that would happen before the views were initialized
would be that the web app would establish communication with the Arudino. One
more task I had to accomplish was how can I send myself an alert in a
reasonable amount of time to let me know If the system had been tripped. Luckly
for me Twilio makes an outstanding library for Python, and really every other
major language out there, that would let me send a text message directly to my
phone. Heck, I could set it up to call me If I wanted to! To top it all off I
plan on hooking up my Arduino to a wireless Raspberry Pi and running the web
server on that so that I don't need to have it hooked up to my computer all of
the time. Maybe I'll even try out Pagekite to make my Raspberry Pi public
facing so that I can send text message commands to arm or disarm the system If
I don't feel like logging into the web UI.
