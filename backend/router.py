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

# Rota para verificar se a API está funcionando
@router.get("/health")
def health_check():
    return {"status": "ok"}


### Rota para buscar todos os itens
@router.get("/contacts/", response_model=List[ContactResponse])
def read_all_contacts_route(db: Session = Depends(get_db)):
    """
    Rota que lê todos os itens do banco de dados
    """
    contacts = get_contacts(db)
    return contacts


### Rota para buscar um item específico
@router.get("/contacts/{contact_id}", response_model=ContactResponse)
def read_one_contact_route(contact_id: int, db: Session = Depends(get_db)):
    """
    Rota que lê um item específico do banco de dados
    """
    db_contact = get_contact(db, contact_id=contact_id)
    if db_contact is None:
        raise HTTPException(status_code=404, detail="Contato não existe")
    return db_contact


### Rota para criar um item
@router.post("/contacts/", response_model=ContactResponse)
def create_contact_route(contact: ContactCreate, db: Session = Depends(get_db)):
    """"
    Rota que cria um novo item no banco de dados
    """
    return create_contact(db=db, contact=contact)


### Rota para deletar um item
@router.delete("/contacts/{contact_id}", response_model=ContactResponse)
def detele_contact_route(contact_id: int, db: Session = Depends(get_db)):
    """
    Rota que deleta um item do banco de dados
    """
    db_contact = delete_contact(db, contact_id=contact_id)
    if db_contact is None:
        raise HTTPException(status_code=404, detail="Contato não existe")
    return db_contact


### Rota para atualizar um item
@router.put("/contacts/{contact_id}", response_model=ContactResponse)
def update_contact_route(contact_id: int, contact: ContactUpdate, db: Session = Depends(get_db)):
    """
    Rota que atualiza um item do banco de dados
    """
    db_contact = update_contact(db, contact_id=contact_id, contact=contact)
    if db_contact is None:
        raise HTTPException(status_code=404, detail="Contato não existe")
    return db_contact