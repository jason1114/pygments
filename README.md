HTTP interface for pygments
===========================

[http://pygments.simplabs.com](http://pygments.simplabs.com) is an **unofficial HTTP API
for the Pygments syntax highlighting library**. It's designed to provide syntax highlighting
for web applications that cynnot execute the Python script directly.

Usage
-----

**POST to [http://pygments.simplabs.com](http://pygments.simplabs.com) with "lang" and "code"
parameters in the body**. You'll receive pygmentized HTML back, which you can store for later
display on your site. You can style the pygmentized HTML using CSS like this: [default.css](default.css)

Ruby Example
------------

<script src="https://gist.github.com/marcoow/5228177.js"></script>

More Information
----------------

Visit [http://pygments.org](http://pygments.org) for more information about Pygments. 

Visit [http://github.com/richleland/pygments-css](http://github.com/richleland/pygments-css) for more example CSS files for use with Pygments.

Visit [http://github.com/simplabs/pygments](http://github.com/simplabs/pygments) for more information about this site, and to see the source code. 

See also: [http://www.hilite.me](http://www.hilite.me) for a similar application with more options.

Copyright/ Acknowledgement
--------------------------

This was originally implemented by [Trevor Turk](https://github.com/trevorturk) and published at
[http://pygments.appspot.com](http://pygments.appspot.com) and later changed by [Marco Otte-Witte](https://github.com/marcoow)
and moved to [http://pygments.simplabs.com](http://pygments.appspot.com).
