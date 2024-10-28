from fastapi import APIRouter, HTTPException
from books.src.services.book_service import BookService
from books.src.dto.book_dto import BookDTO

router = APIRouter()
book_service = BookService()


@router.get("/v1/books/query")
def query_books(filter_expression: str):
    books = book_service.query_books(filter_expression)
    if not books:
        raise HTTPException(status_code=404, detail="Nenhum livro encontrado")
    return books

@router.get("/v1/books", response_model=list[BookDTO])
def get_all_books():
    books = book_service.get_all_books()
    if not books:
        raise HTTPException(status_code=404, detail="Nenhum livro encontrado")
    return books

@router.delete("/v1/books/{isbn}")
def delete_book(isbn: str):
    try:
        book_service.delete_book(isbn)
        return {"message": f"Livro com ISBN {isbn} deletado com sucesso."}
    except ResourceNotFoundError:
        raise HTTPException(status_code=404, detail="Livro não encontrado para deletar")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro ao deletar o livro: {e}")

@router.put("/books/{isbn}", response_model=BookDTO)
def update_book(isbn: str, book: BookDTO):
    try:
        if book.isbn != isbn:
            raise HTTPException(status_code=400, detail="O ISBN no corpo da solicitação não corresponde ao ISBN da URL.")
        book_service.update_book(book)
        return book
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro ao atualizar o livro: {e}")


@router.get("/v1/books/{isbn}", response_model=BookDTO)
def get_book(isbn: str):
    book = book_service.get_book(isbn)
    if not book:
        raise HTTPException(status_code=404, detail="Livro não encontrado")
    return book
@router.post("/v1/books", response_model=BookDTO)
def add_book(book: BookDTO):
    """
     This endpoint API, action add/update book
    """
    try:
        book_service.add_book(book)
        return book
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro ao adicionar o livro: {e}")