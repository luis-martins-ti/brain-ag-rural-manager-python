from sqlalchemy.orm import Session
from app.db.models.crop import Crop
from app.schemas.crop import CropCreate


def create_crop(db: Session, harvest_id: int, crop_in: CropCreate):
    crop = Crop(**crop_in.dict(), harvest_id=harvest_id)
    db.add(crop)
    db.commit()
    db.refresh(crop)
    return crop
