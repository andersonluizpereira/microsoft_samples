from books_create.src.config.azure_config import AzureConfig
from azure.core.exceptions import ResourceExistsError, HttpResponseError

from books_create.src.services.interfaces.book_service_interface import BookServiceInterface

class BookService(BookServiceInterface):
    def __init__(self):
        self.queue_client = AzureConfig.get_queue_service_client().get_queue_client("livros-fila")
        self.sent_books = set()  # Armazenamento em memória para controlar os livros já enviados
        try:
            self.queue_client.create_queue()
        except ResourceExistsError:
            pass  # A fila já existe, então ignoramos o erro

    def add_book(self, book_data: dict):
        try:
            # Verificar se o livro já foi enviado
            if book_data['isbn'] in self.sent_books:
                raise RuntimeError("Este livro já foi enviado para a fila anteriormente.")

            self.queue_client.send_message(book_data)
            self.sent_books.add(book_data['isbn'])  # Registrar que o livro foi enviado
            print(f"Mensagem enviada: {book_data}")
        except HttpResponseError as e:
            raise RuntimeError(f"Erro ao enviar mensagem para a fila: {e}")
        return book_data
