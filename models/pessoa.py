from pydantic import BaseModel


class Pessoa(BaseModel):
    primeiro_nome: str
    ultimo_nome: str
    data_nascimento: str