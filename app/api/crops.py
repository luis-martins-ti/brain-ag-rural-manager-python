from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.auth.deps import get_db, get_current_user
from app.schemas.crop import CropCreate, CropOut
from app.services.crop_service import create_crop

router = APIRouter(prefix="/crops", tags=["Crops"])


@router.post("/{harvest_id}", response_model=CropOut)
def add_crop(
    harvest_id: int,
    crop_in: CropCreate,
    db: Session = Depends(get_db),
    user=Depends(get_current_user),
):
    return create_crop(db, harvest_id, crop_in)
