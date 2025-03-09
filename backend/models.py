from sqlalchemy import Column, Integer, String, DateTime, Date
from sqlalchemy.sql import func
from database import Base


class ContactModel(Base):
    __tablename__ = "contacts"  # esse será o nome da tabela

    id = Column(Integer, primary_key=True, index=True)
    operador = Column(String, index=True)
    dataContato = Column(Date, index=True)
    nomeCliente = Column(String, index=True)
    pessoaContato = Column(String, index=True)
    formaContato1 = Column(String, index=True)
    formaContato2 = Column(String, index=True)
    tipoContato = Column(String, index=True)
    pedidoGerado = Column(String, index=True)
    motivoDeclino = Column(String, index=True)
    observacao = Column(String, index=True)
    created_at = Column(DateTime(timezone=True), default=func.now(), index=True)