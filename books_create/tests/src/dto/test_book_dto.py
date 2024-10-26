import pytest
from books_create.src.dto.book_dto import BookDTO
from pydantic import ValidationError

# Testes para BookDTO

def test_book_dto_valid():
    valid_data = {
        "isbn": "978-3-16-148410-0",
        "tipo_livro": "Novo",
        "estante": "Ficção",
        "idioma": "Português",
        "titulo": "Aventuras no Mundo da Programação",
        "autor": "João da Silva",
        "editora": "Programadores Editora",
        "ano": 2023,
        "edicao": 1,
        "preco": 49.90,
        "peso": 300,
        "descricao": "Um livro sobre aventuras no mundo da programação.",
        "capa": "link_da_imagem.jpg"
    }
    book = BookDTO(**valid_data)
    assert book.isbn == valid_data["isbn"]
    assert book.titulo == valid_data["titulo"]

def test_book_dto_missing_required_field():
    missing_field_data = {
        "tipo_livro": "Novo",
        "estante": "Ficção",
        "idioma": "Português",
        "titulo": "Aventuras no Mundo da Programação",
        "autor": "João da Silva",
        "editora": "Programadores Editora",
        "ano": 2023,
        "edicao": 1,
        "preco": 49.90,
        "peso": 300,
        "descricao": "Um livro sobre aventuras no mundo da programação.",
        "capa": "link_da_imagem.jpg"
    }
    with pytest.raises(ValidationError):
        BookDTO(**missing_field_data)
