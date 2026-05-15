from typing import List

from sqlalchemy.orm import Session

from . import models, schemas


def get_incident(db: Session, incident_id: int):
    return db.query(models.Incident).filter(models.Incident.id == incident_id).first()


def get_incidents(db: Session, skip: int = 0, limit: int = 50) -> List[models.Incident]:
    return db.query(models.Incident).offset(skip).limit(limit).all()


def create_incident(db: Session, incident: schemas.IncidentCreate):
    incident_data = incident.dict()
    incident_data["category"] = "Bache"
    incident_data["media_urls"] = ",".join(incident_data.get("media_urls", []))
    db_incident = models.Incident(**incident_data)
    db.add(db_incident)
    db.commit()
    db.refresh(db_incident)
    return db_incident


def update_incident(db: Session, incident: models.Incident, incident_in: schemas.IncidentUpdate):
    update_data = incident_in.dict(exclude_unset=True)
    if "media_urls" in update_data:
        if update_data["media_urls"] is None:
            update_data["media_urls"] = None
        else:
            update_data["media_urls"] = ",".join(update_data["media_urls"])

    for field, value in update_data.items():
        setattr(incident, field, value)
    db.add(incident)
    db.commit()
    db.refresh(incident)
    return incident


def delete_incident(db: Session, incident: models.Incident):
    db.delete(incident)
    db.commit()
