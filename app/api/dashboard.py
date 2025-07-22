from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.auth.deps import get_db, get_current_user
from app.db.models.property import Property
from app.db.models.crop import Crop
from app.db.models.producer import Producer
from sqlalchemy import func
from collections import defaultdict

router = APIRouter(prefix="/dashboard", tags=["Dashboard"])


@router.get("/")
def get_dashboard(db: Session = Depends(get_db), user=Depends(get_current_user)):
    total_farms = db.query(Property).count()
    total_hectares = db.query(func.sum(Property.total_area)).scalar() or 0

    # Por estado
    by_state = (
        db.query(Property.state, func.count(Property.id)).group_by(Property.state).all()
    )
    states_pie = {state: count for state, count in by_state}

    # Por cultura
    by_crop = (
        db.query(Crop.culture_name, func.count(Crop.id))
        .group_by(Crop.culture_name)
        .all()
    )
    crops_pie = {crop: count for crop, count in by_crop}

    # Uso do solo
    agri_sum = db.query(func.sum(Property.agricultural_area)).scalar() or 0
    veg_sum = db.query(func.sum(Property.vegetation_area)).scalar() or 0
    land_use = {"agricultural_area": agri_sum, "vegetation_area": veg_sum}

    return {
        "total_farms": total_farms,
        "total_hectares": total_hectares,
        "by_state": states_pie,
        "by_crop": crops_pie,
        "land_use": land_use,
    }
