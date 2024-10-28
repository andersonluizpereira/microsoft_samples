from books.src.config.azure_config import AzureConfig
from azure.data.tables import TableServiceClient, TableClient, UpdateMode
from books.src.dto.book_dto import BookDTO
import json


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

