+++
title = "Rotating Trac Logs"
date = 2007-12-19T16:49:00
slug = "rotating-trac-logs"
[taxonomies]
categories = ["Linux"]
tags = ["Linux", "Trac"]

[extra]
social_media_card = "imgs/social-cards/blog_rotating_trac_logs.jpg"
+++

So, you're like me and like to have [trac](http://trac.edgewall.org) constantly logging to file and you hate those files getting huge?

<!-- more -->

It is assumed that you keep all your [trac](http://trac.edgewall.org) environments on the same base directory, for example `/var/lib/trac/`

Here's a simple logrotate config file(normaly under `/etc/logrotate.d/`):

```logrotate
/var/lib/trac/*/log/trac.log {
    weekly
    rotate 7
    missingok
    create 640 www-data www-data
    compress
}
```

I hope you enjoy this simple solution.
