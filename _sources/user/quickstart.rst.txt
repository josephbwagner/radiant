Quick Start
===========

Get up and running with Radiant in under 5 minutes.

First Time Setup
----------------

1. Install Radiant CLI:

   .. code-block:: bash

      pip install radiant-cli

2. Verify installation:

   .. code-block:: bash

      radiant --version

3. Connect your Meshtastic device via USB

Basic Commands
--------------

Run Diagnostics
^^^^^^^^^^^^^^^

Check your device and system configuration:

.. code-block:: bash

   radiant doctor

This will:

- Detect connected Meshtastic devices
- Check USB permissions
- Verify firmware versions
- Test device connectivity
- Provide auto-fix recommendations for issues

Monitor Network
^^^^^^^^^^^^^^^

Watch your mesh network in real-time:

.. code-block:: bash

   radiant monitor

This displays:

- Connected nodes
- Signal strength (SNR)
- Message activity
- Network topology

Press Ctrl+C to exit.

Backup Device
^^^^^^^^^^^^^

Save your device configuration:

.. code-block:: bash

   radiant backup

This creates a JSON backup of:

- Device settings
- Channel configuration
- Module settings
- Node database

Configuration
-------------

Initialize Configuration
^^^^^^^^^^^^^^^^^^^^^^^^

Create a default configuration file:

.. code-block:: bash

   radiant config init

This creates ``~/.config/radiant/config.yaml`` with sensible defaults.

View Configuration
^^^^^^^^^^^^^^^^^^

.. code-block:: bash

   radiant config show

Edit Configuration
^^^^^^^^^^^^^^^^^^

Edit the configuration file directly:

.. code-block:: bash

   # Linux/macOS
   nano ~/.config/radiant/config.yaml

   # Windows
   notepad %USERPROFILE%\\.config\\radiant\\config.yaml

Next Steps
----------

- Read the :doc:`/user/cli-reference` for all available commands
- Check the :doc:`/user/configuration` guide for advanced settings
- Visit the :doc:`/blog` for development updates and tips

Troubleshooting
---------------

Device Not Found
^^^^^^^^^^^^^^^^

If ``radiant doctor`` doesn't find your device:

1. Check USB cable is connected
2. Verify device is powered on
3. Check USB permissions (Linux: add user to ``dialout`` group)
4. Try a different USB port

Permission Denied
^^^^^^^^^^^^^^^^^

On Linux, USB device access requires permissions:

.. code-block:: bash

   sudo usermod -a -G dialout $USER

Then logout and login again.

Command Not Found
^^^^^^^^^^^^^^^^^

If ``radiant`` command is not found after installation:

1. Ensure pip installation directory is in PATH
2. Try running with ``python -m radiant`` instead

Getting Help
------------

- ``radiant --help`` - General help
- ``radiant COMMAND --help`` - Command-specific help
- GitHub Issues: https://github.com/josephbwagner/radiant/issues
- Discussions: https://github.com/josephbwagner/radiant/discussions
