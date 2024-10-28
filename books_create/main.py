from fastapi import FastAPI
from books_create.src.controller.book_controller import router as book_created_router
import uvicorn 

app = FastAPI()

app.include_router(book_created_router, prefix="/books", tags=["books"])

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)