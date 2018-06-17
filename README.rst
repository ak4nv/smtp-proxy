About
=====

This is a deadly simple smtp proxy server for quickly getting mails and
sending it in asynchronous mode with external smtp server.

Requirements
============

Python 3.5.3+, compiled with SSL support, is required.

Installation
============

.. code-block:: bash

  $ git clone https://github.com/ak04nv/smtp-proxy.git /srv/aiosmtpd
  $ cd /srv/aiosmtpd
  $ virtualenv -p python3 .env
  $ source .env/bin/activate
  $ pip install -r requirements.txt
  $ chown -R www-data:www-data .


Create `config.ini` file and fill it like content below

.. code-block:: ini

  SERVER = smtp.gmail.com
  PORT = 587
  USERNAME = my_mail@gmail.com
  PASSWORD = my_strong_password

Activation
==========

.. code-block:: bash

  $ cp smtp-proxy.service /etc/systemd/system
  $ cd /etc/systemd/system
  $ systemd enable smtp-proxy.service
  $ systemd start smtp-proxy.service

Finally
=======

Script was successfully tested on Ubuntu 16.04 with actual updates. Use
this command for seeing logs.

.. code-block:: bash

  $ journalctl -u smtp-proxy.service

License
=======

MIT License
