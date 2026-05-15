from datetime import datetime
from sqlalchemy import Column, DateTime, Integer, String, Text
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Incident(Base):
    __tablename__ = "incidents"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(140), nullable=False)
    description = Column(Text, nullable=False)
    category = Column(String(50), nullable=False, default="Bache")
    location = Column(String(150), nullable=False)
    reporter_name = Column(String(100), nullable=False)
    _media_urls = Column("media_urls", Text, nullable=True)
    status = Column(String(40), default="Pendiente")
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    @property
    def media_urls(self):
        if not self._media_urls:
            return []
        return [url for url in self._media_urls.split(",") if url]

    @media_urls.setter
    def media_urls(self, value):
        if isinstance(value, list):
            self._media_urls = ",".join(value)
        else:
            self._media_urls = value
