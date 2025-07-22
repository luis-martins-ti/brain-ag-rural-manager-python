from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.db.database import Base


class Crop(Base):
    __tablename__ = "crops"

    id = Column(Integer, primary_key=True, index=True)
    culture_name = Column(String, nullable=False)  # Ex: Soja, Milho

    harvest_id = Column(Integer, ForeignKey("harvests.id"), nullable=False)
    harvest = relationship("Harvest", back_populates="crops")
