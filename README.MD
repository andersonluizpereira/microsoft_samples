# Projeto de Books com Azurite e Docker Compose

Descrição

Este projeto é uma aplicação de gerenciamento de livros desenvolvida em Python usando FastAPI. Ela inclui duas APIs e um worker para consumir mensagens de uma fila. A arquitetura do sistema é baseada em microsserviços que interagem com o Azurite, um emulador local do Azure Storage.

Estrutura do Projeto

books: API FastAPI para gerenciar livros, incluindo operações de CRUD.

books_create: API FastAPI responsável por enviar livros para uma fila.

books/src/batch/worker_book: Um worker para processar mensagens da fila e salvar os dados na tabela.

O sistema é gerenciado pelo Docker Compose, que orquestra os serviços, incluindo o Azurite para simular o Azure Storage.

## Pré-requisitos

Docker e Docker Compose instalados.

Python 3.11 (opcional, caso queira rodar o projeto localmente).

Estrutura do Diretório

A estrutura do projeto é organizada da seguinte forma:

```
├── README.MD
├── books
│   ├── __init__.py
│   ├── main.py
│   └── src
│       ├── batch
│       │   └── worker_book
│       │       └── worker.py
│       ├── config
│       │   └── azure_config.py
│       ├── controller
│       │   └── book_controller.py
│       ├── dto
│       │   └── book_dto.py
│       ├── repository
│       │   └── book_repository.py
│       └── services
│           └── book_service.py
├── books_create
│   ├── main.py
│   └── src
│       ├── config
│       │   └── azure_config.py
│       ├── controller
│       │   └── book_controller.py
│       ├── dto
│       │   └── book_dto.py
│       └── services
│           └── book_service.py
├── docker-compose.yaml
├── requirements.txt
```
Instalação e Configuração
  Clone o repositório:

````bash
git clone https://github.com/andersonluizpereira/microsoft_samples.git
cd microsoft_samples
````
## Configuração do Docker Compose:
O arquivo docker-compose.yaml já está configurado para rodar os seguintes serviços:

  * Azurite: Emulador do Azure Storage.
  * books_api: API FastAPI para gerenciar livros.
  * books_queue: API FastAPI para enviar livros para a fila.
  * books_worker: Worker para processar mensagens da fila e salvar os dados na tabela.

## Executar a aplicação:
Execute o comando abaixo para iniciar todos os serviços:
````bash
docker-compose up --build -d
````

## Instalação das dependências:
As dependências do projeto são instaladas automaticamente usando o serviço books_requirements no docker-compose.yaml. Certifique-se de que o requirements.txt esteja atualizado.

```bash
pip install -r requirements.txt
```
# Endpoints

## Books API (books/main.py)
* GET /api/v1/books/{isbn}: Retorna os detalhes de um livro específico pelo ISBN.
* GET /api/v1/books/query: Permite buscar livros com uma expressão de filtro.
* GET /api/v1/books: Retorna todos os livros cadastrados.
* POST /api/v1/books: Cadastra um novo livro.
* PUT /api/v1/books/{isbn}: Atualiza as informações de um livro existente.
* DELETE /api/v1/books/{isbn}: Deleta um livro pelo ISBN.

# Books Create API (books_create/main.py)
* POST /books: Envia um livro para a fila de mensagens.

# Variáveis de Ambiente
As seguintes variáveis de ambiente são usadas para configurar o Azurite e o Azure Storage:
  * AZURE_STORAGE_QUEUE_CONNECTION_STRING
  * AZURE_STORAGE_TABLE_CONNECTION_STRING
  * AZURITE_ACCOUNTS

Essas variáveis são configuradas no docker-compose.yaml.

# Executando os Testes
Os testes estão localizados em books_create/tests. Para executar os testes:
```bash
pytest books_create/tests
```
# Licença
Este projeto é distribuído sob a licença MIT. Veja o arquivo LICENSE para mais detalhes.

# Contribuição
Contribuições são bem-vindas! Por favor, envie um Pull Request ou abra uma Issue para discutir melhorias ou problemas.

# Contato
Para mais informações, entre em contato pelo email: andy2903.alp@gmail.com.



# Exemplo de curl
# GET /api/v1/books/{isbn}
```bash
curl -X GET "http://localhost:8001/api/v1/books/{isbn}"
```
# GET /api/v1/books/query
```bash
curl -X GET "http://localhost:8001/api/v1/books/query?filter_expression={filter_expression}"
```

# GET /api/v1/books
```bash
curl -X GET "http://localhost:8001/api/v1/books"
```

# POST /api/v1/books
```bash
curl -X POST "http://localhost:8001/api/v1/books" \
  -H "Content-Type: application/json" \
  -d '{
    "isbn": "978-3-16-148410-0",
    "tipo_livro": "Novo",
    "estante": "Ficção",
    "idioma": "Português",
    "titulo": "Aventuras no Mundo da Programação",
    "autor": "João da Silva",
    "editora": "Programadores Editora",
    "ano": 2023,
    "edicao": 1,
    "preco": 49.9,
    "peso": 300,
    "descricao": "Um livro sobre aventuras no mundo da programação.",
    "capa": "link_da_imagem.jpg"
  }'
```

# PUT /api/v1/books/{isbn}
```bash
curl -X PUT "http://localhost:8001/api/v1/books/{isbn}" \
  -H "Content-Type: application/json" \
  -d '{
    "isbn": "978-3-16-148410-0",
    "tipo_livro": "Novo",
    "estante": "Ficção",
    "idioma": "Português",
    "titulo": "Aventuras no Mundo da Programação - Atualizado",
    "autor": "João da Silva",
    "editora": "Programadores Editora",
    "ano": 2023,
    "edicao": 2,
    "preco": 59.9,
    "peso": 320,
    "descricao": "Edição atualizada com novas aventuras no mundo da programação.",
    "capa": "link_da_imagem_atualizada.jpg"
  }'
```

# DELETE /api/v1/books/{isbn}
```bash
curl -X DELETE "http://localhost:8001/api/v1/books/{isbn}"
```

# Exemplo de chaves locais

## AZURE_STORAGE_QUEUE_CONNECTION_STRING: DefaultEndpointsProtocol=http;AccountName=devstoreaccount1;AccountKey=Eby8vdM02xNOcqFlqUwJPLlmEtlCDXJ1OUzFT50uSRZ6IFsuFq2UVErCz4I6tq/K1SZFPTOtr/KBHBeksoGMGw==;QueueEndpoint=http://127.0.0.1:10001/devstoreaccount1;
## AZURE_STORAGE_TABLE_CONNECTION_STRING: DefaultEndpointsProtocol=http;AccountName=devstoreaccount1;AccountKey=Eby8vdM02xNOcqFlqUwJPLlmEtlCDXJ1OUzFT50uSRZ6IFsuFq2UVErCz4I6tq/K1SZFPTOtr/KBHBeksoGMGw==;TableEndpoint=http://localhost:10002/devstoreaccount1;
## AZURITE_ACCOUNTS: account1:key1:key2

## Linux e macOS

## Definir variáveis de ambiente temporariamente (válido apenas na sessão atual do terminal):
```bash
export AZURE_STORAGE_QUEUE_CONNECTION_STRING="DefaultEndpointsProtocol=http;AccountName=devstoreaccount1;AccountKey=Eby8vdM02xNOcqFlqUwJPLlmEtlCDXJ1OUzFT50uSRZ6IFsuFq2UVErCz4I6tq/K1SZFPTOtr/KBHBeksoGMGw==;QueueEndpoint=http://127.0.0.1:10001/devstoreaccount1;"
export AZURE_STORAGE_TABLE_CONNECTION_STRING="DefaultEndpointsProtocol=http;AccountName=devstoreaccount1;AccountKey=Eby8vdM02xNOcqFlqUwJPLlmEtlCDXJ1OUzFT50uSRZ6IFsuFq2UVErCz4I6tq/K1SZFPTOtr/KBHBeksoGMGw==;TableEndpoint=http://localhost:10002/devstoreaccount1;"
export AZURITE_ACCOUNTS="account1:key1:key2"
```
## Definir variáveis de ambiente permanentemente (adicionando ao arquivo ~/.bashrc ou ~/.zshrc):
````bash
echo 'export AZURE_STORAGE_QUEUE_CONNECTION_STRING="DefaultEndpointsProtocol=http;AccountName=devstoreaccount1;AccountKey=Eby8vdM02xNOcqFlqUwJPLlmEtlCDXJ1OUzFT50uSRZ6IFsuFq2UVErCz4I6tq/K1SZFPTOtr/KBHBeksoGMGw==;QueueEndpoint=http://127.0.0.1:10001/devstoreaccount1;"' >> ~/.bashrc
echo 'export AZURE_STORAGE_TABLE_CONNECTION_STRING="DefaultEndpointsProtocol=http;AccountName=devstoreaccount1;AccountKey=Eby8vdM02xNOcqFlqUwJPLlmEtlCDXJ1OUzFT50uSRZ6IFsuFq2UVErCz4I6tq/K1SZFPTOtr/KBHBeksoGMGw==;TableEndpoint=http://localhost:10002/devstoreaccount1;"' >> ~/.bashrc
echo 'export AZURITE_ACCOUNTS="account1:key1:key2"' >> ~/.bashrc
source ~/.bashrc
````
Para zsh, substitua ~/.bashrc por ~/.zshrc.

# Windows
## Definir variáveis de ambiente temporariamente (PowerShell):
````bash
$env:AZURE_STORAGE_QUEUE_CONNECTION_STRING = "DefaultEndpointsProtocol=http;AccountName=devstoreaccount1;AccountKey=Eby8vdM02xNOcqFlqUwJPLlmEtlCDXJ1OUzFT50uSRZ6IFsuFq2UVErCz4I6tq/K1SZFPTOtr/KBHBeksoGMGw==;QueueEndpoint=http://127.0.0.1:10001/devstoreaccount1;"
$env:AZURE_STORAGE_TABLE_CONNECTION_STRING = "DefaultEndpointsProtocol=http;AccountName=devstoreaccount1;AccountKey=Eby8vdM02xNOcqFlqUwJPLlmEtlCDXJ1OUzFT50uSRZ6IFsuFq2UVErCz4I6tq/K1SZFPTOtr/KBHBeksoGMGw==;TableEndpoint=http://localhost:10002/devstoreaccount1;"
$env:AZURITE_ACCOUNTS = "account1:key1:key2"
````
## Definir variáveis de ambiente permanentemente (Prompt de Comando):
````bash
setx AZURE_STORAGE_QUEUE_CONNECTION_STRING "DefaultEndpointsProtocol=http;AccountName=devstoreaccount1;AccountKey=Eby8vdM02xNOcqFlqUwJPLlmEtlCDXJ1OUzFT50uSRZ6IFsuFq2UVErCz4I6tq/K1SZFPTOtr/KBHBeksoGMGw==;QueueEndpoint=http://127.0.0.1:10001/devstoreaccount1;"
setx AZURE_STORAGE_TABLE_CONNECTION_STRING "DefaultEndpointsProtocol=http;AccountName=devstoreaccount1;AccountKey=Eby8vdM02xNOcqFlqUwJPLlmEtlCDXJ1OUzFT50uSRZ6IFsuFq2UVErCz4I6tq/K1SZFPTOtr/KBHBeksoGMGw==;TableEndpoint=http://localhost:10002/devstoreaccount1;"
setx AZURITE_ACCOUNTS "account1:key1:key2"
````
Essas variáveis de ambiente serão usadas para configurar o acesso ao Azurite local para simular o Azure Storage no projeto.