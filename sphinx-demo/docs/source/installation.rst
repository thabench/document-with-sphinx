Installation Using *uv*
========================

This project uses **uv** and a modern `pyproject.toml` setup.

* Crate the project directory and navigate to it:

.. code-block:: bash

    mkdir sphinx-demo
    cd sphinx-demo

* Create the environment:

.. code-block:: bash

    uv init
    uv venv
    source .venv/bin/activate

* Add Sphinx and (optional) theme:

.. code-block:: bash

   uv add sphinx renku-sphinx-theme

.. important::
    Next step is mandatory

* Create a *docs* directory and navigate to it. This is where **Sphinx** will generate all the necessary files for automatic documentation

.. code-block:: bash

    mkdir docs
    cd docs
