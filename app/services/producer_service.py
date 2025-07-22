from sqlalchemy.orm import Session, joinedload
from app.db.models.producer import Producer
from app.schemas.producer import ProducerCreate
from app.db.models.property import Property
from app.db.models.harvest import Harvest
from app.db.models.crop import Crop
from fastapi import HTTPException


def create_producer(db: Session, producer_in: ProducerCreate):
    producer = Producer(**producer_in.dict())
    db.add(producer)
    db.commit()
    db.refresh(producer)
    return producer


def list_producers(db: Session):
    return (
        db.query(Producer)
        .options(
            joinedload(Producer.properties)
            .joinedload(Property.harvests)
            .joinedload(Harvest.crops)
        )
        .all()
    )


def update_producer(db: Session, producer_id: int, producer_in: ProducerCreate):
    producer = db.query(Producer).filter(Producer.id == producer_id).first()
    if not producer:
        raise HTTPException(status_code=404, detail="Produtor não encontrado")

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
