from sqlalchemy import Column, Integer, String, ForeignKey, Float
from sqlalchemy.orm import relationship
from app.db.database import Base


class Property(Base):
    __tablename__ = "properties"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    city = Column(String)
    state = Column(String)
    total_area = Column(Float, nullable=False)
    agricultural_area = Column(Float, nullable=False)
    vegetation_area = Column(Float, nullable=False)

    producer_id = Column(Integer, ForeignKey("producers.id"), nullable=False)
    producer = relationship("Producer", back_populates="properties")

    harvests = relationship(
        "Harvest", back_populates="property", cascade="all, delete-orphan"
    )
