from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.auth.deps import get_db, get_current_user
from app.schemas.harvest import HarvestCreate, HarvestOut
from app.services.harvest_service import create_harvest

router = APIRouter(prefix="/harvests", tags=["Harvests"])


@router.post("/{property_id}", response_model=HarvestOut)
def add_harvest(
    property_id: int,
    harvest_in: HarvestCreate,
    db: Session = Depends(get_db),
    user=Depends(get_current_user),
):
    return create_harvest(db, property_id, harvest_in)
