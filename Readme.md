# Produce and consume data from Kafka with Python3 and FastAPI

Hello everyone! 
For example, we have data processing requirements to/from Kafka, and we have our project with Python3 and FastAPI. 
What should we do? 

So, let's go!

## Preconditions

_python3, docker, venv, kafka, ..._

## First step - prepare

Let's make a python3 project - run next command's in terminal (for MacOS):

```cd projects```

```mkdir python3-fast_api-kafka-sync```

```cd python3-fast_api-kafka-sync```

```python3 -m venv .env```

*_If you are using a different OS and if you don't know how do this, you can get help from Google._ 

#### Explanations:
I created a new directory and a new python3 virtual environment for our project with command ```python3 -m venv .env```.

Now let's activate the new venv:

```source .env/bin/activate```

Installing required packages:

```pip install fastapi aiokafka uvicorn```

**It's great!**

## Second step - make our FastAPI project

Let's create a new ```main.py``` file and write the following code.

```python
import os
import uvicorn
from fastapi import FastAPI
import logging


# config logger
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
        

# create fastAPI application  
app = FastAPI()


# API
@app.get('/')
async def my_api():
    _log.info('My API call')
    return 'Hello'


# Main function
if __name__ == '__main__':
    _log.info('Start application!')
    uvicorn.run(app, host=HOST, port=PORT)
    _log.info('End application!')
```

This code is a minimum FastAPI application! 

Start application with the ```python main.py``` command from your venv 
and open the ```http://127.0.0.1:8000``` URL in a browser.

Okay!

## Next step - create kafka producer

Everything is ready for Kafka!
Create new ```kafka.py``` file.

```python


```
