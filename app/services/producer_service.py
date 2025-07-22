from sqlalchemy.orm import Session, joinedload
from app.db.models.producer import Producer
from app.schemas.producer import ProducerCreate
from app.db.models.property import Property
from app.db.models.harvest import Harvest
from app.db.models.crop import Crop
from fastapi import HTTPException, Request


def create_producer(db: Session, producer_in: ProducerCreate):
    producer = Producer(**producer_in.model_dump())  # Use model_dump()
    db.add(producer)
    db.commit()
    db.refresh(producer)
    return producer


def list_producers(db: Session, skip: int, limit: int, page: int, request: Request):
    query = (
        db.query(Producer)
        .options(
            joinedload(Producer.properties)
            .joinedload(Property.harvests)
            .joinedload(Harvest.crops)
        )
        .order_by(Producer.id)
    )
    total = query.count()
    producers = query.offset(skip).limit(limit).all()

    base_url = str(request.url).split("?")[0]
    query_params = request.query_params.multi_items()
    query_dict = dict(query_params)

    def build_url(new_page: int):
        query_dict["page"] = str(new_page)
        query_dict["limit"] = str(limit)
        params = "&".join(f"{k}={v}" for k, v in query_dict.items())
        return f"{base_url}?{params}"

    next_page = build_url(page + 1) if skip + limit < total else None
    prev_page = build_url(page - 1) if page > 1 else None

    return {
        "total": total,
        "page": page,
        "limit": limit,
        "next_page": next_page,
        "prev_page": prev_page,
        "data": producers,
    }


def update_producer(db: Session, producer_id: int, producer_in: ProducerCreate):
    producer = db.query(Producer).filter(Producer.id == producer_id).first()
    if not producer:
        raise HTTPException(status_code=404, detail="Produtor não encontrado")

    # Verifica se o CPF/CNPJ já está sendo usado por outro produtor
    cpf_cnpj_exists = (
        db.query(Producer)
        .filter(Producer.cpf_cnpj == producer_in.cpf_cnpj, Producer.id != producer_id)
        .first()
    )
    if cpf_cnpj_exists:
        raise HTTPException(
            status_code=400,
            detail="Já existe um produtor cadastrado com este CPF/CNPJ.",
        )

    producer.name = producer_in.name
    producer.cpf_cnpj = producer_in.cpf_cnpj
    db.commit()
    db.refresh(producer)
    return producer


def delete_producer(db: Session, producer_id: int):
    producer = db.query(Producer).filter(Producer.id == producer_id).first()
    if not producer:
        raise HTTPException(status_code=404, detail="Produtor não encontrado")
    db.delete(producer)
    db.commit()
