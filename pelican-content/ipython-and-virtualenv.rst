IPython and virtualenv
######################
:date: 2009-01-29 00:48
:author: s0undt3ch
:slug: ipython-and-virtualenv
:category: Python
:tags: IPython, virtualenv
:url: 2009/1/29/ipython-and-virtualenv
:save_as: 2009/1/29/ipython-and-virtualenv/index.html


.. _`virtualenv`: http://pypi.python.org/pypi/virtualenv
.. _`IPython`: http://ipython.scipy.org/
.. _`IPython's documentation`: http://ipython.scipy.org/moin/Cookbook/UserConfigFile


Recently I started developing my python applications using `virtualenv`_ so that I don't
clutter up the system's python installation with non-system python packages.

Everything was good until I wanted to use `IPython`_ instead of python's shell...

The issue is that `virtualenv`_ creates a different python executable that includes the
`virtualenv`_'s packages into ``sys.path`` while `IPython`_ stays unaware of the `virtualenv`_'s
packages.

Yet, there's a solution!!!

In order to solve this issue, `IPython`_ comes along to save the day.

`IPython`_ provides a way to include additional code to be executed when `IPython`_'s shell is started.

First, the small script that allows `IPython`_ to get `virtualenv`_'s packages into its ``sys.path``.

.. code-block:: python

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


Save the above snippet into your user's `IPython`_ configuration directory ``~/.ipython``.
Save it has, for example, ``virtualenv.py``.

Now, as `IPython's documentation`_  suggests, edit ``~/.ipython/ipy_user_conf.py`` and somewhere
inside the ``main()`` function add:

.. code-block:: python

   def main():
       execf('~/.ipython/virtualenv.py')

Now, the next time you start `IPython`_'s shell,  if you've activated your `virtualenv`_
environment, you’ll also get the packages from there too.

.. code-block:: sh

   Develop:user@machine:~$ ipython
   VIRTUAL_ENV -> /home/user/.virtual_python/lib/python2.5/site-packages

   In [1]:


And that's it, there you have your `virtualenv`_ aware `IPython`_ shell!
