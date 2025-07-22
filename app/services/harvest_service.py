from sqlalchemy.orm import Session
from app.db.models.harvest import Harvest
from app.schemas.harvest import HarvestCreate


def create_harvest(db: Session, property_id: int, harvest_in: HarvestCreate):
    harvest = Harvest(**harvest_in.dict(), property_id=property_id)
    db.add(harvest)
    db.commit()
    db.refresh(harvest)
    return harvest
