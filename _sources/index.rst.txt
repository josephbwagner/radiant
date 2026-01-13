Radiant Documentation
=====================

Professional administration platform for Meshtastic radio networks.

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   user/installation
   user/quickstart
   user/cli-reference
   user/configuration
   api/index
   blog

Overview
--------

Radiant is a comprehensive administration platform for Meshtastic mesh radio networks, consisting of:

- **CLI Tools**: Professional command-line interface for diagnostics, monitoring, and device management
- **Server Backend**: Optional FastAPI-based backend with PostgreSQL for historical data and analytics
- **Web Dashboard**: React-based frontend for real-time monitoring and network visualization

Key Features
------------

- Comprehensive device diagnostics with auto-fix recommendations
- Real-time network monitoring
- Historical data tracking and analytics
- Multi-device management
- Alert system with multiple notification channels
- Cross-platform support (Linux, macOS, Windows)

Installation
------------

CLI Only
^^^^^^^^

.. code-block:: bash

   pip install radiant-cli

Full Platform
^^^^^^^^^^^^^

.. code-block:: bash

   docker-compose up

Quick Start
-----------

Run diagnostics on your Meshtastic devices:

.. code-block:: bash

   radiant doctor

Monitor your mesh network:

.. code-block:: bash

   radiant monitor

License
-------

GPL v3

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
