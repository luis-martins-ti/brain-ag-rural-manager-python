from sqlalchemy.orm import Session
from app.db.models.property import Property
from app.schemas.property import PropertyCreate


def create_property(db: Session, producer_id: int, property_in: PropertyCreate):
    property = Property(**property_in.dict(), producer_id=producer_id)
    db.add(property)
    db.commit()
    db.refresh(property)
    return property
