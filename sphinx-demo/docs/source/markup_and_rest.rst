Markup Languages and reStructuredText
==========================================


What Is a Markup Language?
-----------------------------

A markup language describes document structure using plain text.

Examples include:

- Markdown
- reStructuredText
- AsciiDoc


Why reStructuredText?
---------------------------

Sphinx uses **reStructuredText (reST)** because it is expressive and designed
for technical documentation.


Basic Syntax
---------------------------

::

   Section Title
   ================

   **Bold**, *italic*

   - Bullet list

   ..code-block:: python

       print("Hello, Sphinx")


Sphinx Admonitions, Messages, and Warnings
-------------------------------------------

You can draw reader's attention by adding highlighted blocks.
These blocks (or in Sphinx called directives) are called admonitions and can be used anywhere
an ordinary body element can, and can contain arbitrary body elements.

The content of these directives should be written in complete sentences and include
all appropriate punctuation.

There are nine specific named admonitions:

.. attention::¶

    attention - Information that requires the reader’s attention.

.. caution::¶

    caution - Information with regard to which the reader should exercise care.

.. danger::

    danger - Information which may lead to near and present danger if not heeded.

.. error::

    error - Information relating to failure modes of some description.

.. hint::

    hint - Information that is helpful to the reader.

.. important::

    important - Information that is of paramount importance and which the reader must not ignore.

.. note::

    note - An especially important bit of information that the reader should know.

.. tip::

    tip - Some useful tidbit of information for the reader.

.. warning::

    warning - An important bit of information that the reader should be very aware of.

There is also a generic admonition, with an optional title:

.. admonition:: demo_title

    admonition - A generic admonition, with an optional title.

And an admonition to help sort out references to internal or external links:

.. seealso::

   For official documentation, tutorials, and extension references,
   see the `Sphinx documentation website <https://www.sphinx-doc.org/>`_.
