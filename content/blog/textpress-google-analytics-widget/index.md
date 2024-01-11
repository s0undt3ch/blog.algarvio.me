+++
title = "TextPress Google Analytics Widget"
date = 2008-02-25T16:26:00
slug = "textpress-google-analytics-widget"
[taxonomies]
tags = ["TextPress", "TextPress Plugin"]

[extra]
social_media_card = "imgs/social-cards/blog_textpress_google_analytics_widget.jpg"
+++

This was my first serious [TextPress](http://textpress.pocoo.org)
plugin.

This plugin will enable your [TextPress](http://textpress.pocoo.org)
install to be logged by [Google Analytics](http://www.google.com/analytics).

It ads the necessary javascript code to log your blog, plus, it also
logs the downloads of regular filenames which end with a specific
extension; these extensions are defined by you; and also external links.

## Configuration

The necessary configuration is:

- **UID**: Google Analytics’ UID. The UID is needed for Google Analytics to
  log your website stats. Your UID can be found by looking in the JavaScript

  Google Analytics gives you to put on your page. Look for your UID in between
  the javascript:

  ```javascript
  var pageTracker = _gat._getTracker("UA-111111-11");
  ```

  In this example you would put **`UA-11111-1`** in the UID box.

There are other, more advanced configuration options:

- **Admin Logging**: Disabling this option will prevent all logged in
  TextPress admins from showing up on your Google Analytics reports. A
  TextPress admin is defined as a user with a level 4 or higher.

- **Outbound Link Tracking**: Disabling this option will turn off the
  tracking of outbound links.
  It's recommended not to disable this option unless you're a privacy
  advocate (now why would you be using Google Analytics in the first
  place?) or it's causing some kind of weird issue.

- **Google Analytics External Path Prefix**: This will be the path
  shown on Google Analytics regarding external links. Consider the
  following link:

  ```html
  <a href="http://textpress.pocoo.org/">TextPress</a>
  ```

  The above link will be shown as(for example):

  ```
  /external/textpress.pocoo.org/
  ```

  _Outbound link tracking must be enabled for external links to be
  tracked._

- **Download Extensions To Track**: Enter any extensions of files you
  would like to be tracked as a download. For example to track all MP3s
  and PDFs enter **mp3,pdf**.
  Outbound link tracking must be enabled for downloads to be tracked.

- **Tracking Domain Name**: If you’re tracking multiple subdomains with
  the same Google Analytics profile, like what’s talked about
  [here](https://www.google.com/support/googleanalytics/bin/answer.py?answer=55524),
  enter your main domain here. For more info, please visit the previous
  link.

You can submit bugs and/or new features to [DevNull](http://devnull.ufsoft.org).
