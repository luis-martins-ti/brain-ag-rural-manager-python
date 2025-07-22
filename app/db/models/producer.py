from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.db.database import Base


class Producer(Base):
    __tablename__ = "producers"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    cpf_cnpj = Column(String, unique=True, index=True, nullable=False)

    properties = relationship(
        "Property", back_populates="producer", cascade="all, delete-orphan"
    )
