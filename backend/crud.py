from sqlalchemy.orm import Session
from schemas import ContactUpdate, ContactCreate
from models import ContactModel


# Funções para manupulação de dados:
# CRUD - Create, Read, Update, Delete
# Create - Criar
# Read - Ler
# Update - Atualizar
# Delete - Deletar

def get_contacts(db: Session):
    """
    funcao que retorna todos os elementos da tabela Contact - Read
    """
    return db.query(ContactModel).all()


def get_contact(db: Session, contact_id: int):
    """
    funcao que recebe um id e retorna o elemento com esse id na tabela Contact - Read
    """
    return db.query(ContactModel).filter(ContactModel.id == contact_id).first()



def create_contact(db: Session, contact: ContactCreate):
    """
    funcao que cria um novo elemento - Create
    """
    db_contact = ContactModel(**contact.model_dump())
    db.add(db_contact)
    db.commit()
    db.refresh(db_contact)
    return db_contact


def delete_contact(db: Session, contact_id: int):
    """
    funcao que deleta um elemento - Delete
    """
    db_contact = db.query(ContactModel).filter(ContactModel.id == contact_id).first()
    db.delete(db_contact)
    db.commit()
    return db_contact


def update_contact(db: Session, contact_id: int, contact: ContactUpdate):
    """
    funcao que atualiza um elemento - Update
    """
    db_contact = db.query(ContactModel).filter(ContactModel.id == contact_id).first()

    if db_contact is None:
        return None

    if contact.operador is not None:
        db_contact.operador = contact.operador
    if contact.dataContato is not None:
        db_contact.dataContato = contact.dataContato
    if contact.nomeCliente is not None:
        db_contact.nomeCliente = contact.nomeCliente
    if contact.pessoaContato is not None:
        db_contact.pessoaContato = contact.pessoaContato
    if contact.formaContato1 is not None:
        db_contact.formaContato1 = contact.formaContato1
    if contact.formaContato2 is not None:
        db_contact.formaContato2 = contact.formaContato2
    if contact.tipoContato is not None:
        db_contact.tipoContato = contact.tipoContato   
    if contact.pedidoGerado is not None:
        db_contact.pedidoGerado = contact.pedidoGerado
    if contact.motivoDeclino is not None:
        db_contact.motivoDeclino = contact.motivoDeclino
    if contact.observacao is not None:
        db_contact.observacao = contact.observacao

    db.commit()
    return db_contact