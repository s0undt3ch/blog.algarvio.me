Long Live Open-Source
#####################
:date: 2009-04-25 00:50
:author: s0undt3ch
:slug: long-live-open-source
:category: Linux
:tags: ATI, Kubuntu
:url: 2009/4/25/long-live-open-source
:save_as: 2009/4/25/long-live-open-source/index.html

As you can read on a `previous post of mine <{filename}/ati-for-linux.rst>`_,
I was, and still am quite pissed at ATI.

However, being forced to choose from upgrading my favourite linux distribution,
`Kubuntu <http://www.kubuntu.org/>`__, to latest stable version 9.04 and loosing
the ATI proprietary drivers, or, staying at the old version of kubuntu, but keep the
proprietary drivers, Kubuntu won. I was ready to stop using
`compiz <http://compiz-fusion.org/>` once more :\

So, after `google’ing`__ a bit, I found a `post`__ that encouraged me to follow that path.
The first step was to un-install the ATI drivers:

__ http://www.google.com
__ http://mebentley.blogspot.com/2009/03/upgrading-to-jaunty-kill-fglrx.html

.. code-block:: bash

   sudo apt-get remove --purge xorg-driver-fglrx fglrx-kernel-source

After that, the `post`__ suggested a reboot, and so I did. I was no longer able to get Xorg up
and running!

__ http://mebentley.blogspot.com/2009/03/upgrading-to-jaunty-kill-fglrx.html

There was a step missing, edit ``/etc/X11/xorg.conf`` and change the
driver from ``fglrx`` to ``ati``.

Now you restart ``kdm`` and you’re now running the ATI Open-Source drivers.

As suggested by other people, I also thought I’d loose 3D rendering but **NO**!

What’s even greater is that the compiz effects are even faster than with the proprietary drivers.
Sure, there are still glitches with the open-source drivers, but nothing one can’t live with,
at least for now.

So, here comes what I said in the title of this post:

.. class:: center

**Long Live Open Source!!!**
