Documenting Python Code
=======================

At this point you would normaly have your python project with multiple ``.py`` files
that contain various classes and functions. Here you could let *Sphinx* create ``.rst`` files
automatically based on your project by running:

.. code-block:: bash

    sphinx-apidoc -o source/ ../sphinx_apidoc

**sphinx-apidoc** is a tool for automatic generation of Sphinx sources that,
using the autodoc extension, document a whole package in the style of other automatic
API documentation tools.

The usage is as follows:

.. code-block:: bash

    sphinx-apidoc [OPTIONS] -o <OUTPUT_PATH> <MODULE_PATH> [EXCLUDE_PATTERN …]

**MODULE_PATH** is the path to a Python package to document,
and **OUTPUT_PATH** is the directory where the generated sources are placed.
Any **EXCLUDE_PATTERNs** given are fnmatch-style file and/or directory patterns
that will be excluded from generation.

------------------------------------------------------------------------------------------

For the purpose of simple demonstration we will skip this automatic generation
and create some *.py* files that we want to document manualy.

Following the structure of our project in ``/sphinx-demo`` directory run:

.. code-block:: bash

    mkdir demo_code

Here create files:

.. code-block:: bash

    touch demo_functions.py
    touch demo_classes.py


Documenting in Docstrings
----------------------------

To document your code use *docstrings*.
Since Sphinx’s native language is reStructuredText, it is recomended to write in reST style:

.. code-block::

    """
    :param x: Input value
    :return: Output value
    """

You can also write in Google-style docstrings:

.. code-block::

    """
    Args:
    x (int): Input value


    Returns:
    int: Output value
    """

Or Num-Py style docstrings:

.. code-block::

    """
    Parameters
    ----------
    x : int


    Returns
    -------
    int
    """

.. note::
    Since we added napoleon extention, it allows Google & NumPy styles!

----------------------------------------------------------------------------

Docstrings in Functions Example
--------------------------------

.. code-block:: python

   def add(a: int, b: int) -> int:
       """
       Add two integers.

       :param a: First number
       :param b: Second number
       :return: Sum of both numbers
       """
       return a + b

----------------------------------------------------------------------------

Automatic Documentation of the Functions
------------------------------------------
**By adding this code block to your** ``.rst`` **file:**

.. code-block::

    .. autofunction:: demo_code.demo_functions.add

    .. autofunction:: demo_code.demo_functions.divide

**This part of the documentation is created automatically:**

.. autofunction:: demo_code.demo_functions.add

.. autofunction:: demo_code.demo_functions.divide


.. hint::

    We can add another function documentation from a different path

.. code-block::

    .. autofunction:: main.main

.. autofunction:: main.main

----------------------------------------------------------------------------

Automatic Documentation of the Classes
----------------------------------------
This part of the documentation was also created automatically.

In the ``.rst`` file this block was added for **Sphinx** to pull docstrings
from from ``demo_classes.py`` file and build the documentation.

.. code-block::

    .. autoclass:: demo_code.demo_classes.DemoClass
        :members:
        :no-index:

.. autoclass:: demo_code.demo_classes.DemoClass
    :members:
    :no-index:

----------------------------------------------------------------------------

Automatic Documentation of a Module
--------------------------------------

You can document whole module by adding this in the ``.rst`` file:

.. code-block::

    .. automodule:: demo_code.demo_classes
        :members:
        :member-order: bysource
        :undoc-members:
        :show-inheritance:

.. automodule:: demo_code.demo_classes
    :members:
    :member-order: bysource
    :undoc-members:
    :show-inheritance:

.. note::
    We used **:no-index:** when we added a class with *autoclass*.
    This is due to how Sphinx is indexing the documentation.
    It affects search, sidebar and other ways to link to this specific description of the object
