import os
import logging
import asyncio
import aiosmtplib
import configparser

log = logging.getLogger(__name__)
log.setLevel(logging.INFO)

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


class Sendmail:

    def process_message(self, peer, mailfrom, rcpttos, data, **kwargs):
        log.info(f'Got a mail from {mailfrom}')
        task = asyncio.create_task(self.wrapper(mailfrom, rcpttos, data))
        asyncio.ensure_future(task)

    async def wrapper(self, mailfrom, rcpttos, data):
        try:
            await self.delivery(mailfrom, rcpttos, data)
        except Exception as e:
            log.exception(f'Sending to {rcpttos} was failed')

    async def delivery(self, mailfrom, rcpttos, data):
        async with aiosmtplib.SMTP(hostname=server, port=port, use_tls=False) as smtp:
            await smtp.ehlo()
            await smtp.starttls()
            await smtp.login(username, password)
            await smtp.sendmail(mailfrom, rcpttos, data)
            log.info(f'Mail has been successfully sent to {rcpttos}')
