from fastapi import APIRouter, HTTPException
from books_create.src.dto.book_dto import BookDTO
from books_create.src.services.book_service import BookService

router = APIRouter()
book_service = BookService()


@router.post("/add-book/", status_code=201)
async def add_book(book_dto: BookDTO):
    try:
        book = book_service.add_book(book_dto.dict())
        return {"message": "Livro enviado para a fila com sucesso", "book": book}
    except RuntimeError as e:
        raise HTTPException(status_code=500, detail=str(e))
