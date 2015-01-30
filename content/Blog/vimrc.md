Title: The Perfect Vimrc
Date: 2013-03-10T19:54-06:00
Modified: 2015-01-29T20:07-08:00
Tags: Technology, Vim, Dotfiles, Editors
Slug: my-vimrc-is-actually-the-literal-best
Authors: Britt Gresham

I've spent this last month fine tuning my vimrc config file to the point that I
feel it is nearing completion. Now this is not to say that my configuration has
a complete state as my tastes can change and I may stumble upon something that
I like even better than what I have currently. After playing around with all of
these plugins and settings I am going to give you a list of things that I have
found super helpful in enhancing Vim past it's out of the box configuration.
For this post I will mainly be focusing on the configurations and settings
themselves as plugins are an entire book alone. Anyone who is looking at
getting into customizing their vimrc should definitely look into this post and
check out [Vimcasts.org](http://vimcasts.org/). Especially the videos about
[Updating your Vimrc on the
Fly](http://vimcasts.org/episodes/updating-your-vimrc-file-on-the-fly/) or
[Synchronizing plugins with git submodules and
pathogen](http://vimcasts.org/episodes/synchronizing-plugins-with-git-submodules-and-pathogen/),
these videos will help you speed up the process of editing and syncing your
vimrc file and .vim directory.

<h2>The Must Haves</h2>

These settings are simply to help ease everyday Vim usage. I consider these the must haves of Vim and I find myself often typing them if they are not enabled on a machine.

    :::viml
    set number
    set hls
    set backspace=2
    set scrolloff=5
    syntax enable</pre>

Set number turns on line numbering off to the side which is just a really nice
way for me to orient myself with where I am at in a file. Set hls will
highlight your pattern search to ease your substitutions. A handy trick I
learned was that when performing a substitution, if you do not pass in a
pattern into the "search" part of the substitution (e.g. `:%s//replace text/g`)
Vim will use the last searched term (or anything that is currently highlighted
by set `hls`. Set `backspace=2` is something that I don't believe I should have to
do but it is to prevent me from getting frustrated when I am not allowed to
backspace past my insert point. I realize that this is not the Vim way, but it
keeps me sane. `scrolloff` is not as necessary as the others but it is very nice
as it forces your cursor to always be x number of lines off of the edge of the
window when navigating around in normal/visual mode or modifying text in insert
mode. Finally, one that I simply cannot live without is syntax highlighting.
Vim does such a fantastic job with syntax highlighting for pretty much every
language I touch. I have added only one syntax file for scala files when I was
messing around with Gatling. Which, by the way, I'm saving that for a later
post because Gatling is pretty darn sweet.

<h2>The Neat and Helpful</h2>

These next set of settings are ones that I could live without but add a great
deal of class and character to my vimrc config.

    :::viml
    set ts=4 sts=4 sw=4 expandtab
    set autoindent
    set t_Co=256
    set colorcolumn=80
    highlight colorcolumn guibg=#000000 ctermbg=246
    nmap <Space> za

    " jj Exits Insert Mode
    imap jj <Esc>

    " Disable Arrow Keys
    nmap <Left> <Esc>
    nmap <Up> <Esc>
    nmap <Right> <Esc>
    nmap <Down> <Esc>

This next section is just a small chunk out of my personal config file as my
own file is quite large. These are the configs that I could do without but I
use them just about every single day. Starting off with the first line I have
Vim setup to use four spaces in place of a tab as that is what most Python
developers expect to see code. Auto indent is pretty self explanatory, Vim
takes the last lines indentation level and makes your line automatically the
same unless you are ending a code block or xml tree. `set t_Co=256` lets Vim know
that you want it to run with the 256 colors instead of its default pallet of 16.
It adds a nice look and lets colorschemes look just right. Note that `t_Co`
is really only for if you are using Vim in a terminal and not gVim or MacVim,
the graphical versions of Vim.  Color column tells Vim to color the nth column
of text. The next line (highlight colorcolumn) just tells Vim what color it
should use to color the color column. I have my column set at 80 to remind me
that I should not pass over that line if I want to stay within the 79 character
limit that
[PEP-8](http://www.python.org/dev/peps/pep-0008/#maximum-line-length) says. If
you are using Vim's folding feature then this
next mapping is for you. It almost feels natural to map the spacebar to open
and close folds. That is exactly what nmap <Space> za does. For anyone
new to mappings, the syntax is as follows: [n]ormal mode [map]ing {this key}
{will perform this action}. The next line, imap jj <Esc>, tells vim that
when it is in Insert Mode it should listen for when I push "j" twice in a row.
I learned this little trick from Drew Neil since there is very rarely a word
where two J's are back to back that you will ever type. Since you are in insert
mode modifying text anyways there is not too many characters you can push to
perform a simple task. J also happens to be the motion to move down so there is
no other perfect match for this mapping. Finally I disable the arrow keys so
that I am not tempted to use them to move my hand away from home row to move
the cursor. This was more of a mapping to help teach me to use Vim's motions. I
actually strongly recommend the last 4 lines for everyone who is learning Vim
because it trains you to use the hjkl keys how they were meant to be used.

I hope this gets some ideas into your head for what you want to do with your
vimrc. If you find something that you want to share regarding Vim leave a
comment below. Also I have my vimrc and configuration in its full out on Github
here: [My Personal Vim Files](https://github.com/demophoon/dotfiles). Check it
out and steal some of my configurations if you'd like, or use the entire thing
(I think it is brilliant).
