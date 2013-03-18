Setting up a blog with Pelican and Amazon S3.
==============================================

:tags: aws, pelican, python
:summary: Instructions on how to setup a blog with both Pelican and Amazon S3.

The blog you are now reading is hosted on S3 and generated using Pelican_.


This is a quick outline of the steps involved in getting your own blog setup
using the excellent Pelican_ blogging software, written in Python_, and getting
it hosted on `Amazon S3`_.

Why use Pelican_? Because it let's you write your content in reStructuredText_
or Markdown_ and it handles turning that into static html/css/etc content for
you.

Why use S3? Because it can host your content, serve it fast, and it'll cost 
you next to nothing. Especially if you expect to receive next to no traffic
like me ;)

And `S3 can now handle root domains.
<http://www.allthingsdistributed.com/2012/12/root-domain-amazon-s3-website.html>`_


The code for this site is on `my github account`_ so you can follow along, or 
refer to it later. And this blog post itself, in reStructuredText_ format,
can be found `here
<https://raw.github.com/lexual/lexual.com/master/content/blog/tech/2013-03-15_setup-pelican-blog-on-s3.rst>`_

Installing Pelican.
-------------------

I'll assume you're already familiar with virtualenv_ and the excellent
virtualenvwrapper_.

From within your virtualenv do a simple:

.. code-block:: console

    $ pip install pelican

Setting up your Pelican blog.
------------------------------

After you've created a repo, run:

.. code-block:: console

    $ pelican-quickstart

And answer the questions that it prompts. Sticking with the defaults should be
fine, and I recommend getting it to generate you a Makefile as we'll be using
this later.

Now you should have a bunch of files like this:

.. code-block:: console

    $ ls
    content/
    output/
    Makefile
    develop_server.sh
    pelicanconf.py
    publishconf.py


content/
    This is where you write your content (Markdown_ or reStructuredText_)
output/
    This is where the generated html content goes.
    I add this to my .gitignore and keep it out of version control.
Makefile
    Gives some really nice make commands to build and push our content around.
develop_server.sh
    Script to run a dev server to view your content.
pelicanconf.py
    Here's where you can specify your Pelican_ settings.
publishconf.py
    Settings specific to publishing.

I've added support to the Makefile for `pushing to S3`_, hopefully it will be
merged into Pelican_ by the time you read this, if not here's the additions to
the Makefile you'll need.

.. code-block:: make

    S3_BUCKET=put_your_s3_bucket_name_here

    s3_upload: publish
        s3cmd sync $(OUTPUTDIR)/ s3://$(S3_BUCKET) --acl-public --delete-removed


Writing some content
--------------------

A quick search on the interwebs should give you some good resources to learn 
the basics of reStructuredText_ or Markdown_. You can always checkout the 
source for this blog post `here
<https://raw.github.com/lexual/lexual.com/master/content/blog/tech/2013-03-15_setup-pelican-blog-on-s3.rst>`_

Your files should live under the content directory.

If you'd like to add pages that aren't blog posts, do this under content/pages.

A few Pelican_ specifics.

You specify metadata for your blog post like so:

.. code-block:: rst

    :date: 2013-03-15 20:20
    :tags: aws, pelican, python
    :category: yeah
    :slug: my-super-post
    :author: Guy Incognito
    :summary: Short version for index and feeds

To have a post in draft mode:

.. code-block:: rst

    :status: draft

This will put the post online, but there'll be no links to it. To read it you
have to type the url in directly.

And code snippets look like this::

    .. code-block:: python
    
        def plus_one(n):
            return n + 1

And renders like this:

.. code-block:: python

    def plus_one(n):
        return n + 1

What's it look like?
--------------------

To test what your site will look like locally, run:

.. code-block:: console

    $ make html

This generates the static content into output/. And then:

.. code-block:: console

    $ make serve

And you can now check your site out at http://localhost:8000/ in your browser.

Creating S3 buckets.
--------------------

Let's say your site is www.mysite.com. Go into Amazon's `AWS Console`_ and 
create 2 buckets: 'www.mysite.com' and 'mysite.com'. We'll only actually load
content into one of these, the other just helps route traffic from
www.mysite.com to mysite.com.

Under properties for 'www.mysite.com', choose 'redirect all requests to another
host name' under 'Static Web Hosting'.

Under properties for 'mysite.com', choose 'enable website hosting' under
'Static Web Hosting', and set 'Index Document' to 'index.html'.

Putting your content up on S3.
------------------------------

First install s3cmd_:

.. code-block:: console

    $ pip install s3cmd

Now let it know your Amazon credentials:

.. code-block:: console

    $ s3cmd --configure

And give it your AWS access key and secret key.

Now any time you want to rebuild your content and push it to s3, it's a simple
call to:

.. code-block:: console

    $ make s3_upload

This rebuilds all the static content, then pushes it to s3.  
All you need to do after editing or adding any content is run this command
again.


Routing through Amazon's Route 53.
----------------------------------

I'm assuming your domain registrar dns is pointing to Amazon's Route 53. If not
it's a simple as copying and pasting the 4 domain names Amazon provide you.

All we have to do is create 2 A records and we're done. One for 'mysite.com'
and one for 'www.mysite.com'.

For each one, set 'Alias' to yes, and then set the 'Alias Target' to the s3
bucket with the same name.

Learning more about Pelican
---------------------------

The docs for Pelican_ are pretty good way to learn more about the ins and out
of the project. Another good way to learn more is to checkout github repos
for people who are using Pelican_ for the blog. One pythonista's I've referred
to is `pydanny's repo <https://github.com/pydanny/pydanny.github.com>`_

`kernel.org is another notable Pelican user.
<https://www.kernel.org/pelican.html>`_

If I've missed anything, or made any mistakes here, please let me know and
I'll correct them and update the post.

The End
-------

There you have it. With a few small tweaks to the settings file you can have
Disqus comments, Google Analytics tracking, links to your Github and Twitter.

.. You can also get it to generate pdf files of your content. `Here's this blog
    post as a pdf <http://lexual.com/pdf/setup-pelican-blog-on-s3.pdf>`_

All of this without having written a single line of html, css, or javascript.
Massive win!

.. _Pelican: http://docs.getpelican.com
.. _Python: http://python.org
.. _Amazon S3: http://aws.amazon.com/s3
.. _reStructuredText: http://docutils.sourceforge.net/rst.html
.. _Markdown: http://daringfireball.net/projects/markdown/
.. _my github account: https://github.com/lexual/lexual.com
.. _virtualenv: http://virtualenv.org
.. _virtualenvwrapper: http://virtualenvwrapper.readthedocs.org
.. _pushing to S3: https://github.com/getpelican/pelican/pull/775
.. _AWS Console: http://aws.amazon.com/console
.. _s3cmd: http://s3tools.org
.. _kernel.org: https://www.kernel.org/pelican.html
