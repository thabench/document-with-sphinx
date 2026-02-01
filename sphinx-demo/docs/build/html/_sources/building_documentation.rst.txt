Building the Documentation
==========================

Once you are satisfied with your configurations
and finished setting up all ``.rst`` files and documenting in your docstrings
You can generate HTML output:

.. code-block:: bash

    make html

**Sphinx** provides a *Makefile* that lets you run this command.
It builds all necessary files for documentation deployment.

In ``/docs/build/html`` you will find ``index.html`` that can be opened in your browser to
check the built documentation result
