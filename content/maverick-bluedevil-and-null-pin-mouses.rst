Maverick Bluedevil and Null pin Mouse's
#######################################
:date: 2011-02-18 19:58
:author: s0undt3ch
:slug: maverick-bluedevil-and-null-pin-mouses
:url: 2011/02/18/maverick-bluedevil-and-null-pin-mouse-s
:save_as: 2011/02/18/maverick-bluedevil-and-null-pin-mouse-s.html
:category: Linux
:tags: bluedevil, Bluetooth, Kubuntu
:summary:  So, I was trying out Kubuntu Maevrick and found out that my bluetooth
           mouse did not work anymore as it previously did with Jaunty...

So, I was trying out Kubuntu Maevrick and found out that my bluetooth mouse did not work
anymore as it previously did with Jaunty...

The search for the holy grail was not that easy, many posts said to get
the source and build it yourself...

*hmm.... this is a fresh install… I don’t want to start trashing it
already.... ;)*

Well, there’s a solution, add the backports to your ``sources.list``:

.. code-block:: text

    deb http://archive.ubuntu.com/ubuntu maverick-backports universe
    deb-src http://archive.ubuntu.com/ubuntu maverick-backport universe

Update your packages list:

.. code-block:: sh

    sudo apt-get update

Get the new bluedevil, the one which will handle ``null`` pin devices like my mouse:

.. code-block:: sh

    sudo apt-get upgrade

Restart bluetooth:

.. code-block:: sh

    sudo /etc/init.d/bluetooth restart

Now, adding a new device will work as supposed ;)
