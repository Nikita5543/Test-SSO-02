from sqlalchemy import Column, Integer, String, DateTime, Boolean
from sqlalchemy.orm import declarative_base
from datetime import datetime

Base = declarative_base()

class NetworkDevice(Base):
    __tablename__ = "network_devices"
    id = Column(Integer, primary_key=True, index=True)
    hostname = Column(String, unique=True, index=True)
    ip = Column(String, index=True)
    status = Column(Boolean, default=True)
    last_seen = Column(DateTime, default=datetime.utcnow)