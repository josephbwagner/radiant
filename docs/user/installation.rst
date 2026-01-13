Installation
============

Radiant can be installed in several ways depending on your use case.

CLI Only (Recommended for Basic Use)
-------------------------------------

The CLI tools are the simplest way to get started:

.. code-block:: bash

   pip install radiant-cli

Requirements:

- Python 3.9 or higher
- pip

Verification
^^^^^^^^^^^^

After installation, verify it works:

.. code-block:: bash

   radiant --version
   radiant doctor --help

Full Platform (Server + Web Dashboard)
---------------------------------------

Using Docker Compose (Recommended)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The easiest way to run the full platform:

.. code-block:: bash

   git clone https://github.com/josephbwagner/radiant.git
   cd radiant/docker
   cp .env.example .env  # Edit with your settings
   docker-compose up

This starts:

- PostgreSQL database
- FastAPI backend server
- React frontend
- Nginx reverse proxy

Access the web interface at: http://localhost:3000

From Source (Development)
^^^^^^^^^^^^^^^^^^^^^^^^^^

For development or customization:

.. code-block:: bash

   git clone https://github.com/josephbwagner/radiant.git
   cd radiant

   # Install CLI
   cd cli
   poetry install
   cd ..

   # Install Server
   cd server
   poetry install
   cd ..

   # Install Frontend
   cd frontend
   npm install

Server Only (No Web Dashboard)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

If you only need the backend API:

.. code-block:: bash

   pip install radiant-server

Requirements:

- Python 3.12 or higher
- PostgreSQL 16+

Platform-Specific Notes
-----------------------

Linux
^^^^^

USB device access requires appropriate permissions:

.. code-block:: bash

   sudo usermod -a -G dialout $USER
   # Logout and login for changes to take effect

macOS
^^^^^

Install via pip or Homebrew (when available):

.. code-block:: bash

   pip3 install radiant-cli

Windows
^^^^^^^

Install via pip:

.. code-block:: bash

   pip install radiant-cli

For USB device access, ensure you have the appropriate drivers installed.

Upgrading
---------

CLI
^^^

.. code-block:: bash

   pip install --upgrade radiant-cli

Server
^^^^^^

.. code-block:: bash

   pip install --upgrade radiant-server

Docker
^^^^^^

.. code-block:: bash

   cd radiant/docker
   docker-compose pull
   docker-compose up -d

Uninstallation
--------------

CLI
^^^

.. code-block:: bash

   pip uninstall radiant-cli

Server
^^^^^^

.. code-block:: bash

   pip uninstall radiant-server

Docker
^^^^^^

.. code-block:: bash

   cd radiant/docker
   docker-compose down -v  # -v removes volumes (database data)
