+++
title = "Webhelpers and Javascript Minification"
date = 2007-12-31T16:51:00
updated = 2008-01-02
slug = "webhelpers-and-javascript-minification"
[taxonomies]
tags = ["Javascript", "Pylons", "WebHelpers"]

[extra]
social_media_card = "imgs/social-cards/blog_webhelpers_and_javascript_minification.jpg"
+++

Here's a practical idea which I have in use in a [project of mine](http://pastie.ufsoft.org/).

Most of you probably use some javascript library or have some javascript files that you use in your pylons application.

There's also some talk going on related to javascript files compression, and more recently, minification.

While I'm developing, I like to use the normal(non compressed) javascript files, because it helps on debugging.
But for production, using compressed javascript files reduces page load times.

Pylons Webhelpers comes with a useful function to help you include javascript files on your templates,
`javascript_include_tag`.

<!-- more -->

The idea I had was at first, make that function provide the minified version of the JS file if we're not running
our application in debug mode. If we are on debug mode, server the normal file.

So, I added a minified option to that function above, which does just that.

After a while, I wanted to know how I could _minify_ my own javascript files, and I found out about [JSMin](http://www.crockford.com/javascript/jsmin.html).
There's also a python version of it.

That's when I also thought, hell, I could minify my own javascript files upon request, and even cache that so
the routine only runs once.

Ok, the first thing you should do, is download a copy of the python version of [JSMin](http://www.crockford.com/javascript/jsmin.html), save it inside the
lib directory of your project, and, on your project helpers file, have the following code:

```python
import log
import os
from pylons import config
from pylons.decorators.cache import beaker_cache

log = logging.getLogger(__name__)

__javascript_include_tag = javascript_include_tag

def javascript_include_tag(*sources, **options):

    @beaker_cache(key='sources', expire='never', type='dbm')
    def combine_sources(sources, fs_root):
        if len(sources) < 2:
            log.debug('No need to combine, only one source provided')
            return sources

        log.debug('combining javascripts: %r', sources)
        httpbase = os.path.commonprefix(['/'.join(s.split('/')[:-1])+'/'
                                          for s in sources])
        jsbuffer = StringIO.StringIO()
        names = []
        bases = os.path.commonprefix([b.split('/')[:-1] for b in sources])
        log.debug('Base: %s', httpbase)
        for source in sources:
            log.debug('appending %s', source)
            _source = os.path.join(fs_root, *(source).split('/'))
            names.append(source.split('/')[-1:][0][:-3])
            jsbuffer.write(open(_source, 'r').read())
            jsbuffer.write('\n')
        fname = '.'.join(names+['COMBINED', 'js'])
        log.debug('Names: %r', names)
        log.debug('Combined Name: %s', fname)
        fpath = os.path.join(fs_root, 'js', fname)
        log.debug('writing %s', fname)
        open(fpath, 'w').write(jsbuffer.getvalue())
        return [httpbase + fname]

    @beaker_cache(key='sources', expire='never', type='dbm')
    def get_sources(sources, fs_root=''):
        log.debug('Generating minified sources if needed')
        from pastie.lib.jsmin import JavascriptMinify
        jsm = JavascriptMinify()
        _sources = []

        for source in sources:
            _source = os.path.join(fs_root, *(source[:-3]+'.min.js').split('/'))
            if os.path.exists(_source):
                _sources.append(source[:-3]+'.min.js')
            else:
                _source = os.path.join(fs_root, *source.split('/'))
                minified = _source[:-3]+'.min.js'
                log.debug('minifying %s -&gt; %s', source,
                            source[:-3]+'.min.js')
                jsm.minify(open(_source, 'r'), open(minified, 'w'))
                _sources.append(source[:-3]+'.min.js')
        return _sources

    if not config.get('debug', False):
        fs_root = root = config.get('pylons.paths').get('static_files')
        if options.pop('combined', False):
            sources = combine_sources([source for source in sources], fs_root)

        if options.pop('minified', False):
            sources = get_sources([source for source in sources], fs_root)
    return __javascript_include_tag(*sources, **options)
```

Now, on your templates, all you have to do is:

```html+genshi
${ h.javascript_include_tag('/js/jquery-latest.js', minified=True) }
```

Hope the has helped you in some way.
Happy coding and **Happy New Year**!!!!

**Update on 2008/01/02**

Changed function to also combine the several JS files into a single one to reduce requests,
just pass `combined=True`.
