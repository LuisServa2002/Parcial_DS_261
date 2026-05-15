import os
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from backend.app import main
from backend.app.models import Base

SQLALCHEMY_DATABASE_URL = "sqlite:///./test_db.sqlite"
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base.metadata.create_all(bind=engine)


def override_get_db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()


main.app.dependency_overrides[main.get_db] = override_get_db
client = TestClient(main.app)


def test_create_and_read_incident():
    payload = {
        "title": "Bache peligroso",
        "description": "Un gran hueco en la intersección.",
        "category": "Bache",
        "location": "Av. Principal 123",
        "reporter_name": "Test User",
        "media_urls": ["/media/bache.jpg"],
    }

    response = client.post("/incidents", json=payload)
    assert response.status_code == 201
    data = response.json()
    assert data["title"] == payload["title"]
    assert data["category"] == "Bache"
    assert "/media/bache.jpg" in data["media_urls"]

    response_list = client.get("/")
    assert response_list.status_code == 200
    assert isinstance(response_list.json(), list)
    assert response_list.json()[0]["title"] == payload["title"]


def test_read_incident_not_found():
    response = client.get("/incidents/9999")
    assert response.status_code == 404
    assert response.json()["detail"] == "Incidente no encontrado"
