from pydantic import BaseModel, model_validator
from typing import List
from .harvest import HarvestOut


class PropertyBase(BaseModel):
    name: str
    city: str
    state: str
    total_area: float
    agricultural_area: float
    vegetation_area: float

    @model_validator(mode="after")
    def validate_areas(cls, values):
        total = values.total_area
        agri = values.agricultural_area
        veg = values.vegetation_area
        if (agri or 0) + (veg or 0) > (total or 0):
            raise ValueError(
                "Área agricultável + vegetação não pode exceder área total"
            )
        return values


class PropertyCreate(PropertyBase):
    pass


class PropertyOut(PropertyBase):
    id: int
    harvests: List[HarvestOut] = []

    model_config = {"from_attributes": True}
