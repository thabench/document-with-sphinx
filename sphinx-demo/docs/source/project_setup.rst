Project Creation and Configuration
==================================

Inside *docs* directory run this command to initialize Sphinx:

.. code-block:: bash

   sphinx-quickstart

Follow the questions to complete the initialization:

.. image:: _static/questions.png

Recommended options:

- Separate source and build directories: Yes
- Language: en

.. tip::
    For now you can skip *Project release* part.
    This is where you can later store the version of your documentation

Configuration File
------------------

.. note::
    After initialization process is finished you will notice that inside *docs*
    new directories and files where created.

    For now lets look inside *source* directory

Here you will find the configuration file. Let's edit ``conf.py`` to enable extensions:

.. code-block:: python

   extensions = [
       "sphinx.ext.autodoc",
       "sphinx.ext.napoleon",
       "sphinx.ext.viewcode",
   ]

For **Sphinx** to find your documented code you also need to configure the path to your project:

.. code-block:: python

    import os
    import sys

    sys.path.insert(0, os.path.abspath("../.."))

This configuration shows **Sphinx** that the root of this project is ``/sphinx-docs``
