import json

from azure.core.exceptions import HttpResponseError, ResourceNotFoundError

from books.src.config.azure_config import AzureConfig
from books.src.dto.book_dto import BookDTO
from books.src.repository.book_repository import BookRepository


class BookService:
    def __init__(self):
        self.queue_client = AzureConfig.get_queue_service_client().get_queue_client("livros-fila")
        self.ensure_queue_exists()
        self.book_repository = BookRepository()

    def ensure_queue_exists(self):
        try:
            self.queue_client.create_queue()
            print("Fila 'livros-fila' criada com sucesso.")
        except HttpResponseError as e:
            if "QueueAlreadyExists" in str(e):
                print("A fila 'livros-fila' já existe.")
            else:
                print(f"Erro ao criar a fila 'livros-fila': {e}")

    def process_queue_messages(self):
        try:
            messages = self.queue_client.receive_messages(max_messages=5)
            if not messages:
                print("Nenhuma mensagem encontrada na fila.")
            for message in messages:
                try:
                    # Convertendo a string para JSON
                    book_data_str = message.content.replace("'", '"')
                    book_data = json.loads(book_data_str)

                    # Converte o JSON para a classe BookDTO
                    book_dto = BookDTO(**book_data)
                    self.book_repository.save_book(book_dto)
                    self.queue_client.delete_message(message)
                    print(f"Livro salvo na tabela e mensagem excluída: {book_dto.titulo}")
                except Exception as e:
                    print(f"Erro ao processar mensagem: {e}")
                    # Opcionalmente, você pode mover a mensagem para uma fila de mensagens com erro
        except ResourceNotFoundError:
            print("Erro: A fila 'livros-fila' não foi encontrada. Certifique-se de que a fila existe.")
        except HttpResponseError as e:
            print(f"Erro ao processar mensagem da fila: {e}")
