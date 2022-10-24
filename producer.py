import aiokafka as kafka
import os
import logging

KAFKA_TOPIC = os.environ.get('KAFKA_TOPIC', 'test.topic')
KAFKA_BOOTSTRAP_SERVERS = os.environ.get('KAFKA_BOOTSTRAP_SERVERS', 'localhost:9092')
KAFKA_CLIENT_ID = os.environ.get('KAFKA_CLIENT_ID', 'test.client')
KAFKA_GROUP_ID = os.environ.get('KAFKA_GROUP_ID', 'test.group_id')
KAFKA_CONSUMER_OFFSET_MODE = os.environ.get('KAFKA_CONSUMER_OFFSET_MODE', 'latest')


__producer = None
_log = logging.getLogger(__name__)

async def init():
    global __producer
    __producer = kafka.AIOKafkaProducer(bootstrap_servers=KAFKA_BOOTSTRAP_SERVERS,
                                    client_id=KAFKA_CLIENT_ID,
                                    value_serializer=str.encode
                                    )
    _log.info('Инициализация Kafka Producer')
    await __producer.start()


async def stop():
    _log.info('Остановка Kafka Producer')
    await __producer.stop()
    

async def send_data(topic: str, data: str):
    _log.info('Отправка данных в Kafka')
    return await __producer.send(topic, value=data)