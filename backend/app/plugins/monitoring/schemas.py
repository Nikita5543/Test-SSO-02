from pydantic import BaseModel
from datetime import datetime

class DeviceSchema(BaseModel):
    id: int
    hostname: str
    ip: str
    status: bool
    last_seen: datetime

    class Config:
        from_attributes = True