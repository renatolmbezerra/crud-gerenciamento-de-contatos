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
def create_product_route(product: ContactCreate, db: Session = Depends(get_db)):
    return create_contact(db=db, product=product)


@router.get("/contacts/", response_model=List[ContactResponse])
def read_all_products_route(db: Session = Depends(get_db)):
    products = get_contacts(db)
    return products


@router.get("/contacts/{product_id}", response_model=ContactResponse)
def read_product_route(product_id: int, db: Session = Depends(get_db)):
    db_product = get_contact(db, product_id=product_id)
    if db_product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return db_product


@router.delete("/contacts/{product_id}", response_model=ContactResponse)
def detele_product_route(product_id: int, db: Session = Depends(get_db)):
    db_product = delete_contact(db, product_id=product_id)
    if db_product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return db_product


@router.put("/contacts/{product_id}", response_model=ContactResponse)
def update_product_route(
    product_id: int, product: ContactUpdate, db: Session = Depends(get_db)
):
    db_product = update_contact(db, product_id=product_id, product=product)
    if db_product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return db_product