About
=====

This is a dead simple smtp proxy server for quickly getting mails and
sending it in asynchronous mode with external smtp server.

Requirements
============

Python 3.6+, compiled with SSL support, is required.

Installation
============

.. code-block:: bash

  git clone https://github.com/ak4nv/smtp-proxy.git /srv/aiosmtpd
  cd /srv/aiosmtpd
  virtualenv -p python3 .venv
  source .venv/bin/activate
  pip install -r requirements.txt
  chown -R www-data:www-data .


Create `config.ini` file and fill it like content below

.. code-block:: ini

  SERVER = smtp.gmail.com
  PORT = 587
  USERNAME = my_mail@gmail.com
  PASSWORD = my_strong_password

Activation
==========

.. code-block:: bash

  cp smtpd.service /etc/systemd/system
  systemd enable smtpd.service
  systemd start smtpd.service

Service binds on localhost and 1025 port by default. You can change it in ``smtpd.service`` file in ``ExecStart`` param.

Finally
=======

Script was successfully tested on Ubuntu 16.04 with actual updates. Use
this command for seeing logs.

.. code-block:: bash

  journalctl -u smtpd.service
