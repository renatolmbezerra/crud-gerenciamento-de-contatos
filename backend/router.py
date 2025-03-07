from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal, get_db
from schemas import ContactResponse, ContactUpdate, ContactCreate
from typing import List
from crud import (
    create_contact,
    get_contacts,
    get_contact,
    delete_contact,
    update_contact,
)

router = APIRouter()

# Health Check Route
@router.get("/health")
def health_check():
    return {"status": "ok"}

@router.post("/contacts/", response_model=ContactResponse)
def create_contact_route(contact: ContactCreate, db: Session = Depends(get_db)):
    return create_contact(db=db, contact=contact)


@router.get("/contacts/", response_model=List[ContactResponse])
def read_all_contacts_route(db: Session = Depends(get_db)):
    contacts = get_contacts(db)
    return contacts


@router.get("/contacts/{contact_id}", response_model=ContactResponse)
def read_contact_route(contact_id: int, db: Session = Depends(get_db)):
    db_contact = get_contact(db, contact_id=contact_id)
    if db_contact is None:
        raise HTTPException(status_code=404, detail="Contact not found")
    return db_contact


@router.delete("/contacts/{contact_id}", response_model=ContactResponse)
def detele_contact_route(contact_id: int, db: Session = Depends(get_db)):
    db_contact = delete_contact(db, contact_id=contact_id)
    if db_contact is None:
        raise HTTPException(status_code=404, detail="Contact not found")
    return db_contact


@router.put("/contacts/{contact_id}", response_model=ContactResponse)
def update_contact_route(
    contact_id: int, contact: ContactUpdate, db: Session = Depends(get_db)
):
    db_contact = update_contact(db, contact_id=contact_id, contact=contact)
    if db_contact is None:
        raise HTTPException(status_code=404, detail="Contact not found")
    return db_contact