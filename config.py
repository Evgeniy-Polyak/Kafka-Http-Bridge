import logging
import os


logging.basicConfig(format='%(levelname)-8s %(asctime)s [%(msg)s]', level=logging.INFO)
_log = logging.getLogger(__name__)


# read environment variables
HOST = os.environ.get('HOST', '127.0.0.1')
PORT = os.environ.get('PORT', 8000)

# check value
if isinstance(PORT, str):
    try:
        PORT = int(PORT)
    except ValueError as err:
        _log.error('PORT error! Set default PORT value')
        PORT = 8000