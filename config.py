import logging
import os

KAFKA_TOPIC = os.environ.get('KAFKA_TOPIC', 'test.topic')
KAFKA_BOOTSTRAP_SERVERS = os.environ.get('KAFKA_BOOTSTRAP_SERVERS', 'localhost:9092')
KAFKA_CLIENT_ID = os.environ.get('KAFKA_CLIENT_ID', 'test.client')
KAFKA_GROUP_ID = os.environ.get('KAFKA_GROUP_ID', 'test.group_id')
KAFKA_CONSUMER_OFFSET_MODE = os.environ.get('KAFKA_CONSUMER_OFFSET_MODE', 'latest')


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
