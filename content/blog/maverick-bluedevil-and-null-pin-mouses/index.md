+++
title = "Maverick Bluedevil and Null pin Mouse's"
date = 2011-02-18T19:58:00
slug = "maverick-bluedevil-and-null-pin-mouses"
aliases = [
  "2011/02/18/maverick-bluedevil-and-null-pin-mouse-s"
]
[taxonomies]
categories = ["Linux"]
tags = ["bluedevil", "Bluetooth", "Kubuntu"]

[extra]
social_media_card = "imgs/social-cards/blog_maverick_bluedevil_and_null_pin_mouses.jpg"
+++

So, I was trying out Kubuntu Maevrick and found out that my bluetooth mouse did not work
anymore as it previously did with Jaunty...

<!-- more -->

The search for the holy grail was not that easy, many posts said to get
the source and build it yourself...

_hmm.... this is a fresh install… I don’t want to start trashing it
already.... ;)_

Well, there’s a solution, add the backports to your `sources.list`:

```conf
deb http://archive.ubuntu.com/ubuntu maverick-backports universe
deb-src http://archive.ubuntu.com/ubuntu maverick-backport universe
```

Update your packages list:

```sh
sudo apt-get update
```

Get the new bluedevil, the one which will handle `null` pin devices like my mouse:

```sh
sudo apt-get upgrade
```

Restart bluetooth:

```sh
sudo /etc/init.d/bluetooth restart
```

Now, adding a new device will work as supposed ;)
