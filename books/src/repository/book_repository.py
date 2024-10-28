from books.src.config.azure_config import AzureConfig
from azure.data.tables import TableServiceClient, TableClient, UpdateMode
from books.src.dto.book_dto import BookDTO
import json
from azure.core.exceptions import ResourceExistsError, ResourceNotFoundError


class BookRepository:
    def __init__(self):
        AzureConfig.create_table_if_not_exists("BooksTable")
        self.table_client = AzureConfig.get_table_service_client().get_table_client("BooksTable")

    def save_book(self, book_dto: BookDTO):
        entity = {
            'PartitionKey': 'Book',
            'RowKey': book_dto.isbn,
            'BookData': json.dumps(book_dto.dict())  # Salva o livro como JSON
        }
        insert_entity = self.table_client.upsert_entity(mode=UpdateMode.REPLACE, entity=entity)
        print(f"Inserted entity: {insert_entity}")
    def get_book_by_isbn(self, isbn: str) -> BookDTO:
        try:
            entity = self.table_client.get_entity(partition_key='Book', row_key=isbn)
            book_data = json.loads(entity['BookData'])
            return BookDTO(**book_data)
        except ResourceNotFoundError:
            print(f"Livro com ISBN {isbn} não encontrado.")
            return None
        except Exception as e:
            print(f"Erro ao buscar o livro: {e}")
            return None

    def query_books(self, filter_expression: str):
        try:
            entities = self.table_client.query_entities(filter=filter_expression)
            books = [BookDTO(**json.loads(entity['BookData'])) for entity in entities]
            return books
        except Exception as e:
            print(f"Erro ao realizar a consulta: {e}")
            return []

    def delete_book_by_isbn(self, isbn: str):
        try:
            self.table_client.delete_entity(partition_key='Book', row_key=isbn)
            print(f"Livro com ISBN {isbn} deletado com sucesso.")
        except ResourceNotFoundError:
            print(f"Livro com ISBN {isbn} não encontrado para deletar.")
        except Exception as e:
            print(f"Erro ao deletar o livro: {e}")
    def get_all_books(self):
        try:
            entities = self.table_client.list_entities()
            books = [BookDTO(**json.loads(entity['BookData'])) for entity in entities]
            return books
        except Exception as e:
            print(f"Erro ao buscar todos os livros: {e}")
            return []

    def update_book(self, book_dto: BookDTO):
        # O método save_book já faz a atualização, pois usa upsert_entity
        self.save_book(book_dto)