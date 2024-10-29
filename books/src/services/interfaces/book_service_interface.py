from abc import ABC, abstractmethod
from books.src.dto.book_dto import BookDTO

class IBookService(ABC):
    @abstractmethod
    def process_queue_messages(self):
        pass

    @abstractmethod
    def get_book(self, isbn: str) -> BookDTO:
        pass

    @abstractmethod
    def query_books(self, filter_expression: str):
        pass

    @abstractmethod
    def delete_book(self, isbn: str):
        pass

    @abstractmethod
    def get_all_books(self):
        pass

    @abstractmethod
    def add_book(self, book_dto: BookDTO):
        pass

    @abstractmethod
    def update_book(self, book_dto: BookDTO):
        pass