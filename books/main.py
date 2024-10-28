import uvicorn
from fastapi import FastAPI

from books.src.controller.book_controller import router as book_router

app = FastAPI()

# Registrar as rotas do controlador de livros
app.include_router(book_router, prefix="/api", tags=["books"])

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8001)
