+++
title = "Wordpress Is Gone For Good"
date = 2008-02-25T16:48:00
slug = "wordpress-is-gone-for-good"
[taxonomies]
tags = ["TextPress"]

[extra]
social_media_card = "imgs/social-cards/blog_wordpress_is_gone_for_good.jpg"
+++

I try to get my applications written in python, this way I'm able to tweak it as needed.

When I thought about putting a blog online, of course, I searched for a python blogging
application, but, by that time, I was unable to find one. So, like most users, I ended
up installing [WordPress](http://wordpress.org) which suited my needs until a week
ago, when Google emailed me.

At first I thought, _dam, another spam email not catched by my mail
system_. But no:

> Dear site owner or webmaster of ufsoft.org,
> We recently discovered that some of your pages can cause users to be
> infected with malicious software. We have begun showing a warning page
> to users who visit these pages by clicking a search result on Google.com.
> Below are some example URLs on your site which can cause users to be
> infected (space inserted to prevent accidental clicking in case your
> mail client auto-links URLs):
>
> _... etc, etc, etc ..._
>
> Sincerely,
> Google Search Quality Team

**This was legit email…**

I then went to my blog, watched the pages that I was getting that
warning and saw nothing until I checked the HTML source.

Somehow, someone had changed my blog post by including some
`<noscript>badware here</noscript>` tags.

This was of course yet another security bug found for WordPress. There
was already a new WordPress release which handled this bug.

I upgraded my WordPress install and removed all badware from my posts.

With this problem initially solved, I contacted Google and also
[StopBadware.org](http://www.stopbadware.org) like they told me to, in order to remove
the warning for my blog's domain.

My _quest_ now was, getting rid of WordPress and switching to a python
blogging application.

I knew [pocoo](http://pocoo.org) was writing one,
[TextPress](http://textpress.pocoo.org), but when I initially
checked it, it was in it's early days.

**It was time to check it out again and, Hurray!**

Even though it was still not yet production ready, I needed to take it
for a spin.

At first I started by running it locally and trying to import(by hand,
ie, re-typing it all over again) my blog posts to this new blog engine,
it was going to be a hard work...., **but** `mitsuhiko` soon told me
on [#pocoo](irc://freenode.net/pocoo) that he was just finishing a
WordPress importer, this would mean way less work.

While I waited for him to finish his work, I started coding some
[plugins](/tags/textpress-plugin) for this new
blogging engine. Dam, it was extremely easy. So far I've coded:

- [Blix Theme](@/blog/textpress-blix-theme/index.md)
- [ChowMe Theme](@/blog/chowme-textpress-theme/index.md)
- [Extended Latest Comments Widget](@/blog/textpress-extended-last-comments-widget/index.md)
- [Google Analytics Widget](@/blog/textpress-google-analytics-widget/index.md)
- [ImageBox Plugin](@/blog/textpress-imagebox-plugin/index.md)

Currently, [TextPress](http://textpress.pocoo.org) already has some
nice [plugins](http://dev.pocoo.org/projects/textpress/wiki/PluginDatabase) (not
all done by me **`:)`**), besides [those](http://dev.pocoo.org/projects/textpress/browser/textpress/plugins)
included in the source and it can import from other blogging engines, like [WordPress](http://wordpress.org) and
[Blogger](http://www.blogger.com).

**WordPress Is Gone For Good** from my system. Make sure you [check it out](http://textpress.pocoo.org)!
