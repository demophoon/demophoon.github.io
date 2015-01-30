Title: Raspberry Pi and ddclient
Date: 2013-01-27T21:51-06:00
Tags: Technology, Raspberry Pi, DNS, ddclient
Slug: rpi-ddclient
Authors: Britt Gresham

This last week my USB Wi-fi dongle came in the mail from Amazon, which I
specifically ordered for my Raspberry Pi. This was a crucial piece of my
Raspberry Pi puzzle because this little component would let me use the device
with only one cord attached to it. The power cord.

I first configured it up to connect to one of the wireless networks that I have
in the house right. Mind that I needed a display and keyboard to complete this
task because I didn't know what the IP address was of
the miniature Linux computer thus making it impossible for me to directly SSH
into it. I had planned to solve many of my problems with setting up Pagekite (a
program that allows you to tunnel traffic from one of your own public servers
to "localhost" on a private network.)

Unfortunately for me that proved to be quite difficult to setup and get going
so I looked for alternate solutions. I'm not entirely sure as to why Dynamic
DNS was not my first solution, maybe because I had never played around with it
before. I had heard about how it worked a long time ago through DynDns. So I
browsed around at where I bought my domain at and there was free dynamic dns
there and I was in.

Installing the package ddclient onto my Raspberry Pi and configuring it to send
its local IP address instead of its public IP address meant that as long as I
was on the same network as the Raspberry Pi I could always resolve
"http://www.rpi.brittg.com/" to the Raspberry Pi itself no matter what IP
address it was assigned. So when the device is rebooted and the DHCP server
assigns a different IP address from before I will still be able to change any
settings on it all because of Dynamic DNS.

Since I am planning on running FrogPi (My Arduino + Raspberry Pi home security
system) I will need a reliable way of arming and disarming it when I am coming
and going from home.

Anyways, that's what I have been playing around with this week. I'm also
nearing the completion of transferring to the dark side of Vim as I have picked
up the book "Practical Vim", I am not but 40 pages into the book and I have
just about doubled my knowledge on the basics that I thought I had a decent
grasp on. To top it all of I also picked up a very nice keyboard with Cherry MX
Blue switches and I am in love already. Hopefully I'll have this FrogPi project
of mine hammered out over this next week! I'll keep you updated.
