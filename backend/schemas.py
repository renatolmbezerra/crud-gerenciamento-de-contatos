from pydantic import BaseModel, validator, Field
from enum import Enum
from datetime import datetime
from typing import Optional


# Enums para campos com opções predefinidas
class FormaContatoEnum(str, Enum):
    WHATSAPP = "Whatsapp"
    LIGACAO = "Ligação"
    VISITA = "Visita"
    EMAIL = "E-mail"

class TipoContatoEnum(str, Enum):
    ATIVO = "Ativo"
    RECEPTIVO = "Receptivo"

class PedidoGeradoEnum(str, Enum):
    SIM = "Sim"
    NAO = "Não"

class MotivoDeclinioEnum(str, Enum):
    SEM_DEMANDA = "Sem demanda"
    PRECO = "Preço"
    SEM_ESTOQUE = "Sem estoque"
    CREDITO = "Crédito"
    LOGISTICA = "Logística"
    PROSPECCAO = "Prospecção"


# Schema para criação de um novo contato
class ContactBase(BaseModel):
    dataContato: datetime
    nomeCliente: str = Field(..., min_length=1, max_length=100)
    pessoaContato: str = Field(..., min_length=1, max_length=100)
    formaContato1: FormaContatoEnum
    formaContato2: Optional[FormaContatoEnum] = None
    tipoContato: TipoContatoEnum
    pedidoGerado: PedidoGeradoEnum
    motivoDeclino: Optional[MotivoDeclinioEnum] = None
    observacao: Optional[str] = Field(None, min_length=1, max_length=255)

    # Validação para garantir que a data do contato não seja no futuro
    @validator('dataContato')
    def data_nao_pode_ser_futura(cls, value):
        if value > datetime.now():
            raise ValueError('A data do contato não pode ser no futuro')
        return value


class ContactCreate(ContactBase):
    pass


class ContactResponse(ContactBase):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True


class ContactUpdate(BaseModel):
    dataContato: Optional[datetime] = None
    nomeCliente: Optional[str] = Field(None, min_length=1, max_length=100)
    pessoaContato: Optional[str] = Field(None, min_length=1, max_length=100)
    formaContato1: Optional[FormaContatoEnum] = None
    formaContato2: Optional[FormaContatoEnum] = None
    tipoContato: Optional[TipoContatoEnum] = None
    pedidoGerado: Optional[PedidoGeradoEnum] = None
    motivoDeclino: Optional[MotivoDeclinioEnum] = None
    observacao: Optional[str] = Field(None, min_length=1, max_length=255)

    @validator('dataContato')
    def data_nao_pode_ser_futura(cls, value):
        if value and value > datetime.now():
            raise ValueError('A data do contato não pode ser no futuro')
        return value