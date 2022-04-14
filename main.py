import logging

from ib_connection.IBApi import IBApi

logging.basicConfig(level=logging.DEBUG, format='%(levelname)s - %(message)s')

if __name__ == '__main__':
    logging.info('Application bootstrap is starting...')

    app = IBApi()
    app.connect('127.0.0.1', 4001, 123)

