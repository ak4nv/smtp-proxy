About
=====

This is a dead simple smtp proxy for quick getting mails and resend it
in asynchronous mode via external smtp server.

Requirements
============

Python 3.5.3+, compiled with SSL support, is required.

Installation
============

.. code-block:: bash

$ git clone https://github.com/ak04nv/smtp-proxy.git /var/www/aiosmtpd
$ cd /var/www/aiosmtpd
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
