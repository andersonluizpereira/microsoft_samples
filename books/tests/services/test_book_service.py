import unittest
from unittest.mock import patch, MagicMock
from books.src.dto.book_dto import BookDTO
from books.src.services.book_service import BookService
from books.src.config.azure_config import AzureConfig
import os
import pytest


class TestBookService(unittest.TestCase):
    @patch('books.src.config.azure_config.AzureConfig.get_queue_service_client')
    @patch('books.src.repository.book_repository.BookRepository')
    @patch('books.src.config.azure_config.AzureConfig.get_table_service_client')
    @patch.dict(os.environ, {"AZURE_STORAGE_TABLE_CONNECTION_STRING": "DefaultEndpointsProtocol=http;AccountName=devstoreaccount1;AccountKey=key;TableEndpoint=http://localhost:10002/devstoreaccount1;"})
    def setUp(self, mock_table_service_client, mock_book_repository, mock_queue_service_client):
        # Mocking the QueueClient and BookRepository
        self.mock_queue_client = MagicMock()
        mock_queue_service_client.return_value.get_queue_client.return_value = self.mock_queue_client
        self.mock_repository = mock_book_repository.return_value
        self.mock_table_client = MagicMock()
        mock_table_service_client.return_value.get_table_client.return_value = self.mock_table_client
        self.book_service = BookService()

    @patch('books.src.repository.book_repository.BookRepository.get_book_by_isbn')
    def test_get_book(self):
        isbn = '1234567890'
        book = BookDTO(
            isbn=isbn,
            tipo_livro='Novo',
            estante='Ficção',
            idioma='Português',
            titulo='Livro Teste',
            autor='Autor Teste',
            editora='Editora Teste',
            ano=2021,
            edicao=1,
            preco=29.90,
            peso=300,
            descricao='Descrição do livro.',
            capa='link_da_imagem.jpg'
        )
        self.mock_repository.get_book_by_isbn.return_value = book

        result = self.book_service.get_book(isbn)

        self.mock_repository.get_book_by_isbn.assert_called_once_with(isbn)
        self.assertEqual(result, book)
    @patch('books.src.repository.book_repository.BookRepository.get_all_books')
    def test_get_book_mock_fix(self, mock_get_all_books):
        isbn = '1234567890'
        book = BookDTO(
            isbn=isbn,
            tipo_livro='Novo',
            estante='Ficção',
            idioma='Português',
            titulo='Livro Teste',
            autor='Autor Teste',
            editora='Editora Teste',
            ano=2021,
            edicao=1,
            preco=29.90,
            peso=300,
            descricao='Descrição do livro.',
            capa='link_da_imagem.jpg'
        )
        mock_get_all_books.return_value = [book]

        result = self.book_service.get_all_books()

        mock_get_all_books.assert_called_once_with()
        self.assertEqual(result, [book])

if __name__ == '__main__':
    unittest.main()