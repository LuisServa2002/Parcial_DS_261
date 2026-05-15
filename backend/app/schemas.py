from datetime import datetime
from typing import List, Optional, Literal

from pydantic import BaseModel, Field


class IncidentBase(BaseModel):
    title: str = Field(..., max_length=140, example="Bache en avenida principal")
    description: str = Field(..., example="El bache se abrió frente a la parada de bus.")
    category: Literal["Bache"] = Field("Bache", example="Bache")
    location: str = Field(..., example="Calle 12 con Avenida Central")
    reporter_name: str = Field(..., example="María Pérez")
    media_urls: Optional[List[str]] = Field(default_factory=list, example=["/media/bache.jpg"])


class IncidentCreate(IncidentBase):
    pass


class IncidentUpdate(BaseModel):
    title: Optional[str] = Field(None, max_length=140)
    description: Optional[str] = None
    category: Optional[Literal["Bache"]] = None
    location: Optional[str] = None
    reporter_name: Optional[str] = None
    media_urls: Optional[List[str]] = None
    status: Optional[str] = Field(None, example="Resuelto")


class Incident(BaseModel):
    id: int
    title: str
    description: str
    category: str
    location: str
    reporter_name: str
    media_urls: List[str] = []
    status: str
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True


class MediaUploadResponse(BaseModel):
    filename: str
    url: str
