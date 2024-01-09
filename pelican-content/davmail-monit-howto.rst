DavMail Monit HowTo
###################
:date: 2011-02-16 19:42
:author: s0undt3ch
:slug: davmail-monit-howto
:url: 2011/02/16/davmail-monit-howto
:save_as: 2011/02/16/davmail-monit-howto/index.html
:category: Linux
:tags: DavMail, Monit

I recently started to monitor my servers with `monit <http://mmonit.com/monit/>`_.
As such, I started creating scripts for all services that needed monitoring until I
got stuck on one of them `DavMail <http://davmail.sourceforge.net/>`_. It did not
write a pid file and didn't even had a specific process name!

This HowTo is meant to run on an ubuntu/debian system.

I started `googling <http://zine_blog/www.google.com>`__ for a solution
and it was not easy. The problem was with java not allowing or providing
a way to change the process name of a
`jvm <http://en.wikipedia.org/wiki/Java_Virtual_Machine>`__.


The solution I found was `Java Service Wrapper`_ and bellow are the steps
on how to use it.

.. _`Java Service Wrapper`: http://wrapper.tanukisoftware.com/>

First of all, download the debian DavMail package:

.. code-block:: bash

    wget http://sourceforge.net/projects/davmail/files/davmail/3.8.8/davmail_3.8.8-1608-1_all.deb/download \
      -O davmail_3.8.8-1608-1_all.deb


Since this is to be installed on a headless server, we need to remove
some of the dependencies of the package:

.. code-block:: bash

    dpkg -e davmail_3.8.8-1608-1_all.deb


Now you’ll have a DEBIAN directory, ``cd`` into it:

.. code-block:: bash

    cd DEBIAN


Now edit the control file:

.. code-block:: bash

    vi control


Delete the line which starts with ``Depends:``, save and exit. Now we’ll
have to update the package with the new control file:


.. code-block:: bash

    tar -czvf control.tar.gz *
    mv control.tar.gz ../
    cd ../
    ar r davmail_3.8.8-1608-1_all.deb control.tar.gz
    mv davmail_3.8.8-1608-1_all.deb davmail_3.8.8-1608-01_all.deb

Now install the new package:

..code-block:: bash

    dpkg -i davmail_3.8.8-1608-01_all.deb


To configure DavMail, follow their `server setup`_. My
``davmail.properties`` is saved on ``/etc/davmail/davmail.properties``

.. _`server setup`: http://davmail.sourceforge.net/serversetup.html

Now comes the wrapper part. Download the community debian package from
`here <http://wrapper.tanukisoftware.com/doc/english/download.jsp#stable>`__.
For example:

.. code-block:: bash

    wget http://wrapper.tanukisoftware.com/download/3.5.7/wrapper-linux-x86-64-3.5.7.tar.gz

Unpack it

.. code-block:: bash

    tar zxvf wrapper-linux-x86-64-3.5.7.tar.gz


The method I followed is the `Simple App Wrapper`_.
So in *baby* steps…:

.. _`Simple App Wrapper`: http://wrapper.tanukisoftware.com/doc/english/integrate-simple-nix.html

.. code-block:: bash

    cd wrapper-linux-x86-64-3.5.7/
    mkdir /usr/share/davmail/bin
    mkdir /usr/share/davmail/conf
    cp bin/wrapper /usr/share/davmail/bin/davmail
    cp src/bin/sh.script.in /usr/share/davmail/bin/davmail-laucher
    cp lib/libwrapper.so /usr/share/davmail/lib
    cp lib/wrapper.jar /usr/share/davmail/lib
    mv src/conf/wrapper.conf.in /usr/share/davmail/conf/wrapper.conf
    mkdir /var/run/davmail
    chown mail:mail /var/run/davmail


Now, let’s edit some files:

.. code-block:: bash

    vi /usr/share/davmail/bin/davmail-laucher


Here’s what I changed:

.. code-block:: sh

   # Application
   APP_NAME="davmail"
   APP_LONG_NAME="DAVMail Exchange Gateway"

   # Wrapper
   WRAPPER_CMD="./davmail"
   WRAPPER_CONF="../conf/wrapper.conf"

   # Location of the pid file.
   PIDDIR="/var/run/davmail"

   # If specified, the Wrapper will be run as the specified user.
   # IMPORTANT - Make sure that the user has the required privileges to write
   #  the PID file and wrapper.log files.  Failure to be able to write the log
   #  file will cause the Wrapper to exit without any way to write out an error
   #  message.
   # NOTE - This will set the user which is used to run the Wrapper as well as
   #  the JVM and is not useful in situations where a privileged resource or
   #  port needs to be allocated prior to the user being changed.
   RUN_AS_USER=mail

.. code-block:: bash

    vi /usr/share/davmail/conf/wrapper.conf


Here’s what I changed:

.. code-block:: java

   # Java Main class.  This class must implement the WrapperListener interface
   #  or guarantee that the WrapperManager class is initialized.  Helper
   #  classes are provided to do this for you.  See the Integration section
   #  of the documentation for details.
   wrapper.java.mainclass=org.tanukisoftware.wrapper.WrapperSimpleApp

   # Java Classpath (include wrapper.jar)  Add class path elements as
   #  needed starting from 1
   wrapper.java.classpath.1=../lib/wrapper.jar
   wrapper.java.classpath.2=/usr/share/davmail/davmail.jar
   wrapper.java.classpath.3=../lib/activation-1.1.1.jar
   wrapper.java.classpath.4=../lib/commons-logging-1.0.4.jar
   wrapper.java.classpath.5=../lib/jcifs-1.3.14.jar
   wrapper.java.classpath.6=../lib/log4j-1.2.15.jar
   wrapper.java.classpath.7=../lib/stax2-api-3.0.3.jar
   wrapper.java.classpath.8=../lib/commons-codec-1.3.jar
   wrapper.java.classpath.9=../lib/htmlcleaner-2.1.jar
   wrapper.java.classpath.10=../lib/jdom-1.0.jar
   wrapper.java.classpath.11=../lib/mail-1.4.3.jar
   wrapper.java.classpath.12=../lib/woodstox-core-asl-4.0.9.jar
   wrapper.java.classpath.13=../lib/commons-collections-3.1.jar
   wrapper.java.classpath.14=../lib/jackrabbit-webdav-1.4.jar
   wrapper.java.classpath.15=../lib/junit-3.8.1.jar
   wrapper.java.classpath.16=../lib/slf4j-api-1.3.1.jar
   wrapper.java.classpath.17=../lib/commons-httpclient-3.1.jar
   wrapper.java.classpath.18=../lib/jcharset-1.3.jar
   wrapper.java.classpath.19=../lib/slf4j-log4j12-1.3.1.jar
   wrapper.java.classpath.20=../lib/xercesImpl-2.8.1.jar
   wrapper.java.classpath.21=/usr/share/java/swt.jar

   # Maximum Java Heap Size (in MB)
   wrapper.java.maxmemory=512

   # Application parameters.  Add parameters as needed starting from 1
   wrapper.app.parameter.1=davmail.DavGateway
   wrapper.app.parameter.2=/etc/davmail/davmail.properties

   # Log file to use for wrapper output logging.
   wrapper.logfile=/var/log/davmail-wrapper.log

   # Maximum size that the log file will be allowed to grow to before
   #  the log is rolled. Size is specified in bytes.  The default value
   #  of 0, disables log rolling.  May abbreviate with the 'k' (kb) or
   #  'm' (mb) suffix.  For example: 10m = 10 megabytes.
   wrapper.logfile.maxsize=10m

   # Maximum number of rolled log files which will be allowed before old
   #  files are deleted.  The default value of 0 implies no limit.
   wrapper.logfile.maxfiles=3


Let's test it:

.. code-block:: bash

   /usr/share/davmail/bin/davmail-launcher start
   Starting DAVMail Exchange Gateway...
   Waiting for DAVMail Exchange Gateway.......
   running: PID:13569

It's running!!!!

Now, the monit configuration file:

.. code-block:: text

   check process davmail with pidfile /var/run/davmail/davmail.pid
       group mail
       start program = "/usr/share/davmail/bin/davmail-launcher start"
       stop  program = "/usr/share/davmail/bin/davmail-launcher stop"
       if failed host YOUR_SERVER_PUBLIC_FQDN port IMAP_PORT protocol imap then restart
       if 5 restarts within 5 cycles then timeout

Make sure you replace ``YOUR_SERVER_PUBLIC_FQDN`` and ``IMAP_PORT`` with
what’s you’ve setup on your ``davmail.properties``.

For the sake of completeness, here’s my ``davmail.properties``,
obviously obscured where needed :)

.. code-block: conf

   #DavMail settings
   #Wed Jan 12 18:05:34 WET 2011
   davmail.allowRemote=true
   davmail.bindAddress=YOUR_PUBLIC_ADDRESS
   davmail.caldavPastDelay=90
   davmail.caldavPort=11080
   davmail.disableUpdateCheck=false
   davmail.enableEws=true
   davmail.enableProxy=false
   davmail.imapIdleDelay=
   davmail.imapPort=11143
   davmail.keepDelay=30
   davmail.ldapPort=11389
   davmail.logFilePath=/var/log/davmail.log
   davmail.popPort=11110
   davmail.proxyHost=
   davmail.proxyPassword=
   davmail.proxyPort=
   davmail.proxyUser=
   davmail.sentKeepDelay=90
   davmail.server=true
   davmail.server.certificate.hash=
   davmail.smtpPort=11025
   davmail.ssl.keyPass=
   davmail.ssl.keystoreFile=
   davmail.ssl.keystorePass=
   davmail.ssl.keystoreType=JKS
   davmail.url=https\://YOUR_EXCHANGE_DOMAIN/owa
   davmail.useSystemProxies=false
   log4j.logger.davmail=DEBUG
   log4j.logger.httpclient.wire=WARN
   log4j.logger.org.apache.commons.httpclient=WARN
   log4j.rootLogger=WARN

And that’s it, hope you find this useful. If you find anything
confusing, let me know…
