from pydantic import BaseModel
from typing import List
from .crop import CropOut


class HarvestBase(BaseModel):
    name: str


class HarvestCreate(HarvestBase):
    pass


class HarvestOut(HarvestBase):
    id: int
    crops: List[CropOut] = []

    model_config = {"from_attributes": True}
