import os
from pathlib import Path
from typing import List

from fastapi import Depends, FastAPI, File, HTTPException, UploadFile, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from sqlalchemy.orm import Session

from . import crud, models, schemas
from .database import SessionLocal, engine
from .config import settings

models.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Registro de Incidencias Pública",
    description="API para el registro y consulta de incidencias en vía pública con soporte de multimedia.",
    version="1.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

MEDIA_DIR = Path(__file__).resolve().parent.parent / "media"
MEDIA_DIR.mkdir(parents=True, exist_ok=True)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/", response_model=List[schemas.Incident])
def read_incidents(skip: int = 0, limit: int = 50, db: Session = Depends(get_db)):
    return crud.get_incidents(db, skip=skip, limit=limit)


@app.get("/incidents/{incident_id}", response_model=schemas.Incident)
def read_incident(incident_id: int, db: Session = Depends(get_db)):
    incident = crud.get_incident(db, incident_id=incident_id)
    if not incident:
        raise HTTPException(status_code=404, detail="Incidente no encontrado")
    return incident


@app.post("/incidents", response_model=schemas.Incident, status_code=status.HTTP_201_CREATED)
def create_incident(incident_in: schemas.IncidentCreate, db: Session = Depends(get_db)):
    return crud.create_incident(db=db, incident=incident_in)


@app.put("/incidents/{incident_id}", response_model=schemas.Incident)
def update_incident(incident_id: int, incident_in: schemas.IncidentUpdate, db: Session = Depends(get_db)):
    incident = crud.get_incident(db, incident_id=incident_id)
    if not incident:
        raise HTTPException(status_code=404, detail="Incidente no encontrado")
    return crud.update_incident(db=db, incident=incident, incident_in=incident_in)


@app.delete("/incidents/{incident_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_incident(incident_id: int, db: Session = Depends(get_db)):
    incident = crud.get_incident(db, incident_id=incident_id)
    if not incident:
        raise HTTPException(status_code=404, detail="Incidente no encontrado")
    crud.delete_incident(db=db, incident=incident)
    return None


@app.post("/media/upload", response_model=schemas.MediaUploadResponse)
def upload_media(file: UploadFile = File(...)):
    allowed = ["image/jpeg", "image/png", "image/svg+xml", "video/mp4", "audio/mpeg", "audio/wav"]
    if file.content_type not in allowed:
        raise HTTPException(status_code=415, detail="Tipo de archivo no admitido")

    save_path = MEDIA_DIR / file.filename
    with save_path.open("wb") as buffer:
        buffer.write(file.file.read())

    url = f"/media/{file.filename}"
    return schemas.MediaUploadResponse(filename=file.filename, url=url)


@app.get("/media/{filename}")
def serve_media(filename: str):
    path = MEDIA_DIR / filename
    if not path.exists():
        raise HTTPException(status_code=404, detail="Archivo de media no encontrado")
    return FileResponse(path)
