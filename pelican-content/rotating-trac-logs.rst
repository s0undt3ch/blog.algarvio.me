Rotating Trac Logs
##################
:date: 2007-12-19 16:49
:author: s0undt3ch
:category: Linux
:tags: Linux, Trac
:slug: rotating-trac-logs
:url: rotating-trac-logs
:save_as: rotating-trac-logs/index.html

So, you're like me and like to have `trac`_ constantly logging to file and you hate those files getting huge?

It is assumed that you keep all your `trac`_ environments on the same base directory, for example ``/var/lib/trac/``


Here's a simple logrotate config file(normaly under ``/etc/logrotate.d/``):

.. code-block:: sh

   /var/lib/trac/*/log/trac.log {
     weekly
     rotate 7
     missingok
     create 640 www-data www-data
     compress
  }

I hope you enjoy this simple solution.

.. _`trac`: http://trac.edgewall.org/
