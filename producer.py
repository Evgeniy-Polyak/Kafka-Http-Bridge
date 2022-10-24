import aiokafka as kafka
import logging
from config import KAFKA_BOOTSTRAP_SERVERS, KAFKA_CLIENT_ID


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
