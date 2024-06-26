from pydantic import BaseModel
from datetime import date
from enum import Enum
from sqlalchemy import Column, String, Date, Integer
from app.database.database import Base
from typing import Optional


class MedicationRequestStatus(str, Enum):
    """Enumeration representing the status of a MedicationRequest."""
    active = "active"
    completed = "completed"


class MedicationRequest(Base):
    """Represents a medication request."""
    __tablename__ = "medication_requests"

    id: int = Column(
        Integer,
        primary_key=True,
        index=True,
        doc="Unique identifier for the medication request."
    )
    patient_reference: str = Column(
        String,
        doc="Reference to the patient for whom the medication is requested."
    )
    clinician_reference: str = Column(
        String,
        doc="Reference to the clinician who prescribed the medication."
    )
    medication_reference: str = Column(
        String,
        doc="Reference to the medication being requested."
    )
    reason_text: str = Column(
        String,
        doc="Text describing the reason for the medication request."
    )
    prescribed_date: date = Column(
        Date,
        doc="Date when the medication was prescribed."
    )
    start_date: date = Column(
        Date,
        doc="Date when the medication should start."
    )
    end_date: Optional[date] = Column(
        Date,
        nullable=True,
        doc="Optional end date for the medication."
    )
    frequency: str = Column(
        String,
        doc="Frequency of medication dosage."
    )
    status: str = Column(
        String,
        doc="Current status of the medication request."
    )


class MedicationRequestIn(BaseModel):
    """Input model for creating or updating a medication request."""
    patient_reference: str
    clinician_reference: str
    medication_reference: str
    reason_text: str
    prescribed_date: date
    start_date: date
    frequency: str
    status: MedicationRequestStatus


class MedicationRequestOut(BaseModel):
    """Output model for returning a medication request."""
    id: int
    patient_reference: str
    clinician_reference: str
    medication_reference: str
    reason_text: str
    prescribed_date: date
    start_date: date
    end_date: Optional[date]
    frequency: str
    status: MedicationRequestStatus
