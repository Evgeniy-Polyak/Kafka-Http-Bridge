from datetime import datetime
import config
import uvicorn
from fastapi import FastAPI
import logging
import producer
from model import SendDataRequest, SendDataResponse 

# configuring logger
_log = logging.getLogger(__name__)


# create fastAPI application
app = FastAPI()


# init resources
@app.on_event('startup')
async def on_start():
    await producer.init()
    

# release resources
@app.on_event('shutdown')
async def on_stop():
    await producer.stop()
    

# API
@app.get('/')
async def my_api():
    _log.info('My API call')
    return 'Hello'


@app.post('/kafka/send', response_model=SendDataResponse)
async def send_to_kafka(model: SendDataRequest):
    task = await producer.send_data(model.topic, model.data)
    result = await task
    
    return SendDataResponse(topic=result.topic, 
                            partition=result.topic_partition.partition, 
                            offset=result.offset,
                            timestamp=datetime.fromtimestamp(result.timestamp/1000))
    


# Main function
if __name__ == '__main__':
    _log.info('Start application!')
    uvicorn.run(app, host=config.HOST, port=config.PORT)
    _log.info('End application!')