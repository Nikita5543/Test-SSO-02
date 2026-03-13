from fastapi import APIRouter, Depends
from sqlalchemy.future import select
from app.plugins.monitoring.models import NetworkDevice
from app.plugins.monitoring.schemas import DeviceSchema
from app.core.database import get_db
from sqlalchemy.ext.asyncio import AsyncSession

router = APIRouter(prefix="/monitoring", tags=["monitoring"])

@router.get("/devices", response_model=list[DeviceSchema])
async def get_devices(db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(NetworkDevice))
    devices = result.scalars().all()
    return devices