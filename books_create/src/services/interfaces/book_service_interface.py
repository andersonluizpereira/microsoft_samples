from abc import ABC, abstractmethod


class BookServiceInterface(ABC):
    @abstractmethod
    def add_book(self, book_data: dict):
        pass
