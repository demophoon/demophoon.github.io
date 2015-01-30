Title: Vim
Date: 2013-01-13T23:22-06:00
Tags: Technology, Vim, Editors
Slug: vim-is-actually-the-literal-best
Authors: Britt Gresham

So, over this last week or so I have been going through some tutorials on how
to better myself when it comes to Vim. I decided to take myself way back to the
roots and review a lot of basics such as correctly moving the cursor around in
a buffer, tab and window management, and my almighty .vimrc file. Over several
months I have picked up some very bad habits when it comes to the text editor
of my choice such as using the arrows to navigate through a file instead of
using motions to navigate. Instead of pushing "w" to skip to the next word I
found myself moving the cursor over with <Right Arrow> as many times as there
were letters in the word. This should make any experienced Vim user cringe with
great disgust. I've almost treated it like it was just another sub par text
editor like Windows Notepad with some helpful tools that I had picked up along
the way like the features with Visual mode. I've decided this weekend that If I
am to use Vim I an going to use it like how it should have been used in the
first place which means no more arrow keys for me, there is a nice mapping you
can place in your own Vimrc file (the configuration file containing all of your
settings) that will map the arrow keys to nothing, effectively turning them off
so that I am forced to learn how to quickly navigate through a document with
the "hjkl" motions, along with others as well. I've also stepped up my game and
moved my entire `~/.vim` directory into version control. The `~/.vim` directory
contains all plugins you have added into Vim. Also in this folder is where my
`.vimrc` file exists so that can stay in version control too.  It now lives on
Github so now whenever I want my Vim config I can pull it down into my home
directory and it is always up to date and the exact configuration that I would
use at home or at work or where ever really.
