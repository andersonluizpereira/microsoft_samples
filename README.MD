

# Exemplo de curl
curl -X 'GET' \
  'http://0.0.0.0:8001/api/v1/books/978-3-16-148410-3' \
  -H 'accept: application/json'

curl -X 'DELETE' \
  'http://0.0.0.0:8001/api/v1/books/978-3-16-148410-3' \
  -H 'accept: application/json'

curl -X 'POST' \
  'http://0.0.0.0:8001/api/v1/books' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
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
  "preco": 49.90,
  "peso": 300,
  "descricao": "Um livro sobre aventuras no mundo da programação.",
  "capa": "link_da_imagem.jpg"
}'

# Exemplo de chaves locais

AZURE_STORAGE_QUEUE_CONNECTION_STRING: DefaultEndpointsProtocol=http;AccountName=devstoreaccount1;AccountKey=Eby8vdM02xNOcqFlqUwJPLlmEtlCDXJ1OUzFT50uSRZ6IFsuFq2UVErCz4I6tq/K1SZFPTOtr/KBHBeksoGMGw==;QueueEndpoint=http://127.0.0.1:10001/devstoreaccount1;

AZURE_STORAGE_TABLE_CONNECTION_STRING: DefaultEndpointsProtocol=http;AccountName=devstoreaccount1;AccountKey=Eby8vdM02xNOcqFlqUwJPLlmEtlCDXJ1OUzFT50uSRZ6IFsuFq2UVErCz4I6tq/K1SZFPTOtr/KBHBeksoGMGw==;TableEndpoint=http://localhost:10002/devstoreaccount1;

AZURITE_ACCOUNTS: account1:key1:key2