from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.auth.deps import get_db, get_current_user
from app.schemas.property import PropertyCreate, PropertyOut
from app.services.property_service import create_property

router = APIRouter(prefix="/properties", tags=["Properties"])


@router.post("/{producer_id}", response_model=PropertyOut)
def add_property(
    producer_id: int,
    property_in: PropertyCreate,
    db: Session = Depends(get_db),
    user=Depends(get_current_user),
):
    return create_property(db, producer_id, property_in)
