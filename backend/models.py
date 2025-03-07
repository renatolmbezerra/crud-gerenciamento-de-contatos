from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql import func
from database import Base


class ContactModel(Base):
    __tablename__ = "contatos"  # esse será o nome da tabela

    id = Column(Integer, primary_key=True, index=True)
    dataContato = Column(DateTime(timezone=True), index=True)
    nomeCliente = Column(String, index=True)
    pessoaContato = Column(String, index=True)
    formaContato1 = Column(String, index=True)
    formaContato2 = Column(String, index=True)
    tipoContato = Column(String, index=True)
    pedidoGerado = Column(String, index=True)
    motivoDeclino = Column(String, index=True)
    observacao = Column(String, index=True)
    created_at = Column(DateTime(timezone=True), default=func.now(), index=True)