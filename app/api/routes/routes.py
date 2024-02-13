from fastapi import HTTPException, Path, Depends, APIRouter
from sqlalchemy.orm import Session
from app.database.database import SessionLocal
from app.models.models import (
    MedicationRequestOut,
    MedicationRequestIn,
    MedicationRequest
)
from typing import List


# Dependency to get a database session
def get_db():
    """Dependency to get a database session."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


router = APIRouter()


# Routes
@router.post("/medication_requests/", response_model=MedicationRequestOut)
def create_medication_request(
    medication_request: MedicationRequestIn,
    db: Session = Depends(get_db)
):
    """Create a new medication request in the database."""
    db_request = MedicationRequest(**medication_request.dict())
    db.add(db_request)
    db.commit()
    db.refresh(db_request)
    return db_request


@router.get("/medication_requests/", response_model=List[MedicationRequestOut])
def get_medication_requests(
    status: str = None,
    prescribed_date_start: str = None,
    prescribed_date_end: str = None,
    db: Session = Depends(get_db)
):
    """Retrieve medication requests from the database based on optional filters."""
    query = db.query(MedicationRequest)
    if status:
        query = query.filter(MedicationRequest.status == status)
    if prescribed_date_start:
        query = query.filter(MedicationRequest.prescribed_date >= prescribed_date_start)
    if prescribed_date_end:
        query = query.filter(MedicationRequest.prescribed_date <= prescribed_date_end)
    return query.all()


@router.get("/medication_requests/{request_id}", response_model=MedicationRequestOut)
def get_single_medication_request(
    request_id: str = Path(..., description="The ID of the medication request to retrieve"),
    db: Session = Depends(get_db)
):
    """Retrieve a single medication request by its ID."""
    db_request = db.query(MedicationRequest).filter(MedicationRequest.id == request_id).first()
    if db_request is None:
        raise HTTPException(status_code=404, detail="Medication request not found")
    return db_request


@router.patch("/medication_requests/{request_id}", response_model=MedicationRequestOut)
def update_medication_request(
    request_id: str,
    medication_request: MedicationRequestIn,
    db: Session = Depends(get_db)
):
    """Update a medication request in the database."""
    db_request = db.query(MedicationRequest).filter(MedicationRequest.id == request_id).first()
    if db_request is None:
        raise HTTPException(status_code=404, detail="Medication request not found")

    for var, value in medication_request.dict(exclude_unset=True).items():
        setattr(db_request, var, value)

    db.commit()
    db.refresh(db_request)
    return db_request
