Title: Blue-Green Deployments
Date: 2012-10-13T12:37-06:00
Tags: Technology, Deployments, Continuous Deployment
Slug: blue-green
Authors: Britt Gresham


The first time I heard about blue-green deployments was when I was at work
reconfiguring an apache web server. I noticed that using name-based virtual
hosting I could change the port that
[http://blog.brittg.com/](http://blog.brittg.com/) had ran on from
say port 8790 to 8791 on the fly by just invoking a reload on the apache2
process. By starting up a new instance of my blog on port 8791 and diverting
all of the traffic to that port instead of the main process I would be able to
upgrade the main process with whatever updates I had. After the updates were
completed I'd just transfer the traffic back to port 8790 and shut off the
temporary server. Apache made this even easier since it has its own built-in
load balancer module. You can throw in as many virtual hosts as you want into a
load balancer and whenever you shut one down the traffic automatically migrates
over to the other instances. I didn't know it at the time but what I had
discovered was the Blue-Green deployment method which is very useful for
minimizing and eradicating downtime of an application. When you can script
everything to do this entire process automatically it becomes a push of a
button to push all of your newly written code out to the production instance. I
will tell you this, the work that you will spend writing the code for
streamlining your future deployments gives you more time to write more code and
less time worrying about planning when to put up that "Maintenance Mode" banner
which could be weeks down the road, only to find out that when the application
gets put into production there was a user error during the deployment that
caused an entire outage and code being rolled back. Been there, done that. So
you can believe me when I say Blue-Green is the way to go.
