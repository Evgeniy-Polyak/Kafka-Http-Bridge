from datetime import datetime
from pydantic import BaseModel


class SendDataRequest(BaseModel):
    topic: str
    data: str
    
    
class SendDataResponse(BaseModel):
    topic: str
    partition: int
    offset: int
    timestamp: datetime