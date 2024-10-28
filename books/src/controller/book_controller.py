from fastapi import APIRouter, HTTPException
from books.src.services.book_service import BookService
from books.src.dto.book_dto import BookDTO

router = APIRouter()
book_service = BookService()


@router.get("/books/query")
def query_books(filter_expression: str):
    books = book_service.query_books(filter_expression)
    if not books:
        raise HTTPException(status_code=404, detail="Nenhum livro encontrado")
    return books

@router.delete("/books/{isbn}")
def delete_book(isbn: str):
    try:
        book_service.delete_book(isbn)
        return {"message": f"Livro com ISBN {isbn} deletado com sucesso."}
    except ResourceNotFoundError:
        raise HTTPException(status_code=404, detail="Livro não encontrado para deletar")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro ao deletar o livro: {e}")


@router.get("/books/{isbn}", response_model=BookDTO)
def get_book(isbn: str):
    book = book_service.get_book(isbn)
    if not book:
        raise HTTPException(status_code=404, detail="Livro não encontrado")
    return book
