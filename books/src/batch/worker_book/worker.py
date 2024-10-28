import time

from books.src.services.book_service import BookService


def start_worker():
    book_service = BookService()
    while True:
        book_service.process_queue_messages()
        time.sleep(10)  # Intervalo entre verificações na fila

if __name__ == "__main__":
    start_worker()
