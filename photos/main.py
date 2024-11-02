from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.responses import JSONResponse
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient
import os

app = FastAPI()

# Configurações do Azurite
AZURITE_CONNECTION_STRING = (
    "DefaultEndpointsProtocol=http;"
    "AccountName=devstoreaccount1;"
    "AccountKey=Eby8vdM02xNOcqFeqC9eK9Z3mPj4JydK3uWqvFQ==;"
    "BlobEndpoint=http://127.0.0.1:10000/devstoreaccount1;"
)
CONTAINER_NAME = "fotos"

def initialize_blob_service():
    """Inicializa o serviço Blob e o container."""
    try:
        blob_service_client = BlobServiceClient.from_connection_string(AZURITE_CONNECTION_STRING)
        container_client = blob_service_client.get_container_client(CONTAINER_NAME)
        try:
            container_client.create_container()
            print(f"Container '{CONTAINER_NAME}' criado.")
        except Exception as e:
            print(f"Container '{CONTAINER_NAME}' já existe ou ocorreu um erro: {e}")
        return blob_service_client
    except Exception as e:
        print(f"Erro ao conectar ao Azurite: {e}")
        raise e

blob_service_client = initialize_blob_service()

@app.post("/upload")
async def upload_photo(file: UploadFile = File(...)):
    """
    Endpoint para fazer upload de uma foto.
    """
    if not file.content_type.startswith('image/'):
        raise HTTPException(status_code=400, detail="Arquivo enviado não é uma imagem.")

    blob_name = file.filename
    blob_client = blob_service_client.get_blob_client(container=CONTAINER_NAME, blob=blob_name)

    try:
        # Lê o conteúdo do arquivo
        file_content = await file.read()
        blob_client.upload_blob(file_content, overwrite=True)
        return JSONResponse(status_code=200, content={"message": f"Foto '{blob_name}' enviada com sucesso."})
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro ao enviar a foto: {e}")

@app.get("/photos/{blob_name}")
async def get_photo(blob_name: str):
    """
    Endpoint para obter informações sobre uma foto específica.
    """
    blob_client = blob_service_client.get_blob_client(container=CONTAINER_NAME, blob=blob_name)
    try:
        blob = blob_client.download_blob()
        return JSONResponse(status_code=200, content={"blob_name": blob_name, "size": blob.size})
    except Exception as e:
        raise HTTPException(status_code=404, detail="Foto não encontrada.")

# Função main opcional para rodar com Uvicorn
def main():
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)

# Executa main() se o script for executado diretamente
if __name__ == "__main__":
    main()
