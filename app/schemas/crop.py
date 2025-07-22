from pydantic import BaseModel


class CropBase(BaseModel):
    culture_name: str


class CropCreate(CropBase):
    pass


class CropOut(CropBase):
    id: int

    model_config = {"from_attributes": True}
