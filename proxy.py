import os
import logging
import asyncio
import aiosmtplib
import configparser

log = logging.getLogger('aiosmtpd')

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
config = os.path.join(BASE_DIR, 'config.ini')

with open(config, 'r') as f:
    config_string = '[default]\n' + f.read()

settings = configparser.ConfigParser()
settings.read_string(config_string)

server = settings.get('default', 'SERVER')
port = settings.get('default', 'PORT')
username = settings.get('default', 'USERNAME')
password = settings.get('default', 'PASSWORD')

loop = asyncio.get_event_loop()
smtp = aiosmtplib.SMTP(hostname=server, port=port, loop=loop, use_tls=False)


class Sendmail:

    def process_message(self, peer, mailfrom, rcpttos, data, **kws):
        log.info('Got a mail from %s', mailfrom)
        loop.create_task(self.delivery(mailfrom, rcpttos, data))

    async def delivery(self, mailfrom, rcpttos, data):
        try:
            await smtp.connect()
            await smtp.ehlo()
            await smtp.starttls()
            await smtp.login(username, password)
            await smtp.sendmail(mailfrom, rcpttos, data)
        except Exception as e:
            log.exception('Sending was failed')
        else:
            log.info('Mail has been successfully sent to %s', rcpttos)
