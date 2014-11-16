Wordpress Is Gone For Good
##########################
:date: 2008-02-25 16:48
:author: s0undt3ch
:slug: wordpress-is-gone-for-good
:tags: TextPress

I try to get my applications written in python, this way I'm able to tweak it as needed.

When I thought about putting a blog online, of course, I searched for a python blogging
application, but, by that time, I was unable to find one. So, like most users, I ended
up installing `WordPress <http://wordpress.org/>`__ which suited my needs until a week
ago, when `Google <http://google.com>`__ emailed me.

At first I thought, *dam, another spam email not catched by my mail
system*. But no:

.. code-block:: text

   Dear site owner or webmaster of ufsoft.org,
   We recently discovered that some of your pages can cause users to be
   infected with malicious software. We have begun showing a warning page
   to users who visit these pages by clicking a search result on Google.com.
   Below are some example URLs on your site which can cause users to be
   infected (space inserted to prevent accidental clicking in case your
   mail client auto-links URLs):

        ... etc, etc, etc ...

        Sincerely,
        Google Search Quality Team 


**This was legit email…**

I then went to my blog, watched the pages that I was getting that
warning and saw nothing until I checked the HTML source.

Somehow, someone had changed my blog post by including some
``<noscript>badware here</noscript>`` tags.

This was of course yet another security bug found for WordPress. There
was already a new WordPress release which handled this bug.

I upgraded my WordPress install and removed all badware from my posts.

With this problem initially solved, I contacted `Google <http://google.com>`__ and also
`StopBadware.org <http://www.stopbadware.org/>`__ like they told me to, in order to remove
the warning for my blog's domain.

My *quest* now was, getting rid of WordPress and switching to a python
blogging application.

I knew `pocoo <http://pocoo.org/>`__ was writing one, 
`TextPress <http://textpress.pocoo.org/>`__, but when I initially
checked it, it was in it's early days.

**It was time to check it out again and, Hurray!**

Even though it was still not yet production ready, I needed to take it
for a spin.

At first I started by running it locally and trying to import(by hand,
ie, re-typing it all over again) my blog posts to this new blog engine,
it was going to be a hard work...., **but** ``mitsuhiko`` soon told me
on `#pocoo <irc://freenode.net/pocoo>`__ that he was just finishing a
WordPress importer, this would mean way less work.

While I waited for him to finish his work, I started coding some
`plugin’s </tags/textpress-plugin>`__ for this new
blogging engine. Dam, it was extremely easy. So far I've coded:

-  `Blix Theme <{filename}/textpress-blix-theme.rst>`_
-  `ChowMe Theme <{filename}/chowme-textpress-theme.rst>`_
-  `Extended Latest Comments Widget <{filename}/textpress-extended-last-comments-widget.rst>`_
-  `Google Analytics Widget <{filename}/textpress-extended-last-comments-widget.rst>`_
-  `ImageBox Plugin <{filename}/textpress-imagebox-plugin.rst>`_

Currently, `TextPress <http://textpress.pocoo.org/>`__ already has some
nice `plugins <http://dev.pocoo.org/projects/textpress/wiki/PluginDatabase>`blix_theme_preview (not
all done by me **``:)``**), besides `those <http://dev.pocoo.org/projects/textpress/browser/textpress/plugins>`__
included in the source and it can import from other blogging engines, like `WordPress <http://wordpress.org>`__ and
`Blogger <http://www.blogger.com/>`__.


..  role:: strikethrough

:strikethrough:`You are reading this post within my` `TextPress <http://textpress.pocoo.org/>`__ :strikethrough:`install, which makes me conclude this blog post`.

**WordPress Is Gonne For Good** from my system. Make sure you `check it out <http://textpress.pocoo.org/>`__!
