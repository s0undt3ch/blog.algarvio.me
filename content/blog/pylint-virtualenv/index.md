+++
title = "PyLint + Virtualenv"
date = 2012-12-27T14:27:00
slug = "pylint-virtualenv"
aliases = [
  "2012/12/27/pylint-+-virtualenv"
]
[taxonomies]
categories = ["Python"]
tags = ["PyLint"]

[extra]
social_media_card = "imgs/social-cards/blog_pylint_virtualenv.jpg"
+++

I don't have the time to write the full blog post, so, here's the recipe!

<!-- more -->

On your pylint rcfile setting:

```
init-hook="
    exec 'aW1wb3J0IHN5cywgb3MKCmlmICdWSVJUVUFMX0VOVicgbm90IGluIG9zLmVudmlyb246CiAgICBz \
    eXMuZXhpdCgwKQoKdmVfZGlyID0gb3MuZW52aXJvblsnVklSVFVBTF9FTlYnXQp2ZV9kaXIgaW4g \
    c3lzLnBhdGggb3Igc3lzLnBhdGguaW5zZXJ0KDAsIHZlX2RpcikKYWN0aXZhdGVfdGhpcyA9IG9z \
    LnBhdGguam9pbihvcy5wYXRoLmpvaW4odmVfZGlyLCAnYmluJyksICdhY3RpdmF0ZV90aGlzLnB5 \
    JykKCiMgRml4IGZvciB3aW5kb3dzCmlmIG5vdCBvcy5wYXRoLmV4aXN0cyhhY3RpdmF0ZV90aGlz \
    KToKICAgIGFjdGl2YXRlX3RoaXMgPSBvcy5wYXRoLmpvaW4ob3MucGF0aC5qb2luKHZlX2Rpciwg \
    J1NjcmlwdHMnKSwgJ2FjdGl2YXRlX3RoaXMucHknKQoKZXhlY2ZpbGUoYWN0aXZhdGVfdGhpcywg \
    ZGljdChfX2ZpbGVfXz1hY3RpdmF0ZV90aGlzKSkK'.decode('base64')"
```

Don't be scared, the decoded version of the above is:

```python
import sys, os

if 'VIRTUAL_ENV' not in os.environ:
    sys.exit(0)

ve_dir = os.environ['VIRTUAL_ENV']
ve_dir in sys.path or sys.path.insert(0, ve_dir)
activate_this = os.path.join(os.path.join(ve_dir, 'bin'), 'activate_this.py')

# Fix for windows
if not os.path.exists(activate_this):
    activate_this = os.path.join(os.path.join(ve_dir, 'Scripts'), 'activate_this.py')

execfile(activate_this, dict(__file__=activate_this))
```
