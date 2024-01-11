+++
title = "IPython and virtualenv"
date = 2009-01-29T00:48:00
slug = "ipython-and-virtualenv"
aliases = [
  "2009/1/29/ipython-and-virtualenv",
]
[taxonomies]
categories = ["Python"]
tags = ["IPython", "virtualenv"]

[extra]
social_media_card = "imgs/social-cards/blog_ipython_and_virtualenv.jpg"
+++

Recently I started developing my python applications using [virtualenv](http://pypi.python.org/pypi/virtualenv) so that I don't
clutter up the system's python installation with non-system python packages.

Everything was good until I wanted to use [IPython](http://ipython.scipy.org) instead of python's shell...

<!-- more -->

The issue is that [virtualenv](http://pypi.python.org/pypi/virtualenv) creates a different python executable that includes the
[virtualenv](http://pypi.python.org/pypi/virtualenv)'s packages into `sys.path` while [IPython](http://ipython.scipy.org) stays unaware of the [virtualenv](http://pypi.python.org/pypi/virtualenv)'s
packages.

Yet, there's a solution!!!

In order to solve this issue, [IPython](http://ipython.scipy.org) comes along to save the day.

[IPython](http://ipython.scipy.org) provides a way to include additional code to be executed when [IPython](http://ipython.scipy.org)'s shell is started.

First, the small script that allows [IPython](http://ipython.scipy.org) to get [virtualenv](http://pypi.python.org/pypi/virtualenv)'s packages into its `sys.path`.

```python
import site
from os import environ
from os.path import join
from sys import version_info

if 'VIRTUAL_ENV' in environ:
    virtual_env = join(environ.get('VIRTUAL_ENV'),
                      'lib',
                      'python%d.%d' % version_info[:2],
                      'site-packages')
    site.addsitedir(virtual_env)
    print 'VIRTUAL_ENV ->', virtual_env
    del virtual_env
del site, environ, join, version_info
```

Save the above snippet into your user's [IPython](http://ipython.scipy.org) configuration directory `~/.ipython`.
Save it has, for example, `virtualenv.py`.

Now, as [IPython's documentation](http://ipython.scipy.org/moin/Cookbook/UserConfigFile) suggests, edit `~/.ipython/ipy_user_conf.py` and somewhere
inside the `main()` function add:

```python

def main():
    execf('~/.ipython/virtualenv.py')
```

Now, the next time you start [IPython](http://ipython.scipy.org)'s shell, if you've activated your [virtualenv](http://pypi.python.org/pypi/virtualenv)
environment, you’ll also get the packages from there too.

```sh

Develop:user@machine:~$ ipython
VIRTUAL_ENV -> /home/user/.virtual_python/lib/python2.5/site-packages

In [1]:
```

And that's it, there you have your [virtualenv](http://pypi.python.org/pypi/virtualenv) aware [IPython](http://ipython.scipy.org) shell!
