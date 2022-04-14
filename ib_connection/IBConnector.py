from threading import Thread

import logging

class IBConnector:

    def __init__(self, app):
        self.thread = Thread(
            target=self.run,
            name='IB connector',
        )