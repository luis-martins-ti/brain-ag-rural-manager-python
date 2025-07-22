from fastapi import APIRouter, Depends, Query, Request
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from app.auth.deps import get_db, get_current_user
from app.schemas.producer import ProducerCreate, ProducerOut
from app.services.producer_service import (
    create_producer,
    list_producers,
    update_producer,
    delete_producer,
)

router = APIRouter(prefix="/producers", tags=["Producers"])


@router.post("/", response_model=ProducerOut)
def add_producer(
    producer_in: ProducerCreate,
    db: Session = Depends(get_db),
    user=Depends(get_current_user),
):
    return create_producer(db, producer_in)


@router.get("/")
def get_producers(
    db: Session = Depends(get_db),
    user=Depends(get_current_user),
    request: Request = None,
    page: int = Query(1, ge=1),
    limit: int = Query(10, ge=1, le=100),
):
    skip = (page - 1) * limit
    return list_producers(db=db, skip=skip, limit=limit, page=page, request=request)


@router.put("/{producer_id}", response_model=ProducerOut)
def edit_producer(
    producer_id: int,
    producer_in: ProducerCreate,
    db: Session = Depends(get_db),
    user=Depends(get_current_user),
):
    return update_producer(db, producer_id, producer_in)


@router.delete("/{producer_id}", status_code=204)
def remove_producer(
    producer_id: int,
    db: Session = Depends(get_db),
    user=Depends(get_current_user),
):
    delete_producer(db, producer_id)
    return None
