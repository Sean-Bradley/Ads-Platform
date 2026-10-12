from pydantic import BaseModel


class AdCreate(BaseModel):
    title: str
    description: str
    price: str
