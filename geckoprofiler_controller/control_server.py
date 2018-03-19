"""
This control-server will start the Web Socket server.
It will listens the connections from Gecko-Profiler Add-on and Python client.
The Gecko-Profiler Add-on will wait for commands from this server, while the commands come from Python client.
"""

import os
import logging
import subprocess

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

CURRENT_PATH = os.path.dirname(os.path.abspath(__file__))


class ServerController:
    def __init__(self):
        self.p = None
        self.command = os.path.join(CURRENT_PATH, 'server', 'websocket_server.py')

    def start_server(self):
        logger.info('Starting Web Socket server ...')
        sub_env = os.environ.copy()
        self.p = subprocess.Popen(['python', self.command], env=sub_env)

        logger.info('Web Socket server started.')

    def stop_server(self):
        self.p.kill()
        logger.info('Server stopped.')
