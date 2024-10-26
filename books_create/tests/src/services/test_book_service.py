import pytest
from books_create.src.services.book_service import BookService
from books_create.src.services.interfaces.book_service_interface import BookServiceInterface
from books_create.src.dto.book_dto import BookDTO
from unittest.mock import patch, MagicMock
from azure.core.exceptions import HttpResponseError
from pydantic import ValidationError

@pytest.fixture
@patch('books_create.src.services.book_service.AzureConfig.get_queue_service_client')
def book_service(mock_get_queue_service_client) -> BookServiceInterface:
    mock_queue_client = MagicMock()
    mock_get_queue_service_client.return_value.get_queue_client.return_value = mock_queue_client
    return BookService()

# Fixture para dados do livro
@pytest.fixture
def book_data() -> dict:
    return {
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

def test_add_book_success(book_service, book_data):
    with patch.object(book_service.queue_client, 'send_message') as mock_send_message:
        result = book_service.add_book(book_data)
        mock_send_message.assert_called_once()
        assert result == book_data

def test_add_book_duplicate_isbn(book_service, book_data):
    # Primeiro envio
    book_service.add_book(book_data)
    # Segundo envio deve falhar
    with pytest.raises(RuntimeError, match="Este livro já foi enviado para a fila anteriormente."):
        book_service.add_book(book_data)

def test_add_book_queue_error(book_service, book_data):
    with patch.object(book_service.queue_client, 'send_message', side_effect=HttpResponseError("Erro ao enviar mensagem")):
        with pytest.raises(RuntimeError, match="Erro ao enviar mensagem para a fila: Erro ao enviar mensagem"):
            book_service.add_book(book_data)
