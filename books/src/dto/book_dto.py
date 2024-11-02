from pydantic import BaseModel

class BookDTO(BaseModel):
    isbn: str
    tipo_livro: str
    estante: str
    idioma: str
    titulo: str
    autor: str
    editora: str
    ano: int
    edicao: int
    preco: float
    peso: int
    descricao: str
    capa: str
