

# Exemplo de curl
curl -X 'GET' \
  'http://0.0.0.0:8001/v1/books/978-3-16-148410-3' \
  -H 'accept: application/json'

curl -X 'DELETE' \
  'http://0.0.0.0:8001/v1/books/978-3-16-148410-3' \
  -H 'accept: application/json'

# Exemplo de chaves locais

AZURE_STORAGE_QUEUE_CONNECTION_STRING: DefaultEndpointsProtocol=http;AccountName=devstoreaccount1;AccountKey=Eby8vdM02xNOcqFlqUwJPLlmEtlCDXJ1OUzFT50uSRZ6IFsuFq2UVErCz4I6tq/K1SZFPTOtr/KBHBeksoGMGw==;QueueEndpoint=http://127.0.0.1:10001/devstoreaccount1;

AZURE_STORAGE_TABLE_CONNECTION_STRING: DefaultEndpointsProtocol=http;AccountName=devstoreaccount1;AccountKey=Eby8vdM02xNOcqFlqUwJPLlmEtlCDXJ1OUzFT50uSRZ6IFsuFq2UVErCz4I6tq/K1SZFPTOtr/KBHBeksoGMGw==;TableEndpoint=http://localhost:10002/devstoreaccount1;

AZURITE_ACCOUNTS: account1:key1:key2