ZTE MF622 USB Modem Under Linux
###############################
:date: 2007-11-30 09:40
:author: s0undt3ch
:category: Linux
:tags: Linux
:slug: zte-mf622-usb-modem-under-linux
:summary: I recently bought a 3G wireless card to use with my laptop, a ZTE, model MF622.
          Since the first time I tried Linux, also the first time I encountered this kind
          of problems with my USB ADSL modem, and this being an USB modem also, I knew I was going to have troubles.

          At first I tried `USB ModeSwitch`_  which has experimental support for ZTE's MF620 model with no luck.
          I then followed the instructions on the site to *snoop* the usb communication under M$ Win to get the
          messages being sent to the device so I could mimic that under Linux. **Still**, no luck.

          I then tried to code a python script which used the ``libusb`` so that I could make the device switch
          to the modem configuration. **Still**, no luck.

          I spent a lot of time on this subject and then one time I removed the ``usb_storage`` module while
          `HAL`_ was waiting for the device to settle down and guess what!? After a few seconds, the device
          changed itself to the modem configuration. All I needed now was to automate this procedure.


I recently bought a 3G wireless card to use with my laptop, a ZTE, model MF622.
Since the first time I tried Linux, also the first time I encountered this kind
of problems with my USB ADSL modem, and this being an USB modem also, I knew I was going to have troubles.

At first I tried `USB ModeSwitch`_  which has experimental support for ZTE's MF620 model with no luck.
I then followed the instructions on the site to *snoop* the usb communication under M$ Win to get the
messages being sent to the device so I could mimic that under Linux. **Still**, no luck.

I then tried to code a python script which used the ``libusb`` so that I could make the device switch
to the modem configuration. **Still**, no luck.

I spent a lot of time on this subject and then one time I removed the ``usb_storage`` module while
`HAL`_ was waiting for the device to settle down and guess what!? After a few seconds, the device
changed itself to the modem configuration. All I needed now was to automate this procedure.

Here's the **udev** script that does the job:

.. code-block:: sh

  ACTION!="add", GOTO="ZTE_End"

  # Is this the ZeroCD device?
  SUBSYSTEM=="usb", SYSFS{idProduct}=="2000",
  SYSFS{idVendor}=="19d2", GOTO="ZTE_ZeroCD"

  # Is this the actual modem?
  SUBSYSTEM=="usb", SYSFS{idProduct}=="0001",
  SYSFS{idVendor}=="19d2", GOTO="ZTE_Modem"

  LABEL="ZTE_ZeroCD"
  # This is the ZeroCD part of the card, remove
  # the usb_storage kernel module so
  # it does not get treated like a storage device
  RUN+="/sbin/rmmod usb_storage"

  LABEL="ZTE_Modem"
  # This is the Modem part of the card, let's
  # load usbserial with the correct vendor
  # and product ID's so we get our usb serial devices
  RUN+="/sbin/modprobe usbserial vendor=0x19d2 product=0x0001",
  # Make users belonging to the dialout group
  # able to use the usb serial devices.
  MODE="660", GROUP="dialout"

  LABEL="ZTE_End"


Save this file as ``/etc/udev.d/15-zte-mf622.rules`` for example(this path is a good one under (K)Ubuntu).

The next time you plug-in the modem, at first, the ``usb_storage`` module gets removed. After a few seconds,
since the modem is not being handled like a storage device, it'll switch to the modem configuration. At this
stage we tell `UDEV`_ to load the ``usbserial`` kernel module with the vendor and product id's and you'll get
3 ``ttyUSB`` devices. The ``/dev/ttyUSB0`` will be the one you should use to make a connection.

You can now point ``ppp`` or ``wvdial`` to that device a start the connection, or, you might also want to check
`UMTSmon`_, this is an application suited for these kind of modems.



.. _`USB ModeSwitch`: http://www.draisberghof.de/usb_modeswitch/
.. _`HAL`: http://www.freedesktop.org/wiki/Software/hal
.. _`UDEV`: http://www.kernel.org/pub/linux/utils/kernel/hotplug/udev.html
.. _`UMTSmon`: http://umtsmon.sourceforge.net/
