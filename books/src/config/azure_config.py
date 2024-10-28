import os

from azure.core.exceptions import ResourceExistsError
from azure.core.pipeline.transport import RequestsTransport
from azure.data.tables import TableServiceClient, TableClient
from azure.storage.queue import QueueServiceClient


class AzureConfig:
    @staticmethod
    def get_queue_service_client():
        connect_str = os.getenv("AZURE_STORAGE_QUEUE_CONNECTION_STRING")
        if not connect_str:
            raise ValueError(
                "AZURE_STORAGE_QUEUE_CONNECTION_STRING não está configurado. Certifique-se de definir esta variável de ambiente.")
        transport = RequestsTransport(verify=False)  # Desabilitar SSL para ambiente local
        queue_service_client = QueueServiceClient.from_connection_string(connect_str, transport=transport)
        return queue_service_client

    @staticmethod
    def get_table_service_client():
        connect_str = os.getenv("AZURE_STORAGE_TABLE_CONNECTION_STRING")
        if not connect_str:
            raise ValueError(
                "AZURE_STORAGE_TABLE_CONNECTION_STRING não está configurado. Certifique-se de definir esta variável de ambiente.")
        transport = RequestsTransport(verify=False)  # Desabilitar SSL para ambiente local
        table_service_client = TableServiceClient.from_connection_string(connect_str, transport=transport)
        return table_service_client

    @staticmethod
    def create_table_if_not_exists(table_name):
        connect_str = os.getenv("AZURE_STORAGE_TABLE_CONNECTION_STRING")
        if not connect_str:
            raise ValueError(
                "AZURE_STORAGE_CONNECTION_STRING não está configurado. Certifique-se de definir esta variável de ambiente.")
        try:
            table_client = TableClient.from_connection_string(conn_str=connect_str, table_name=table_name)
            table_client.create_table()
            print(f"Tabela '{table_name}' criada com sucesso!")
        except ResourceExistsError:
            print("A tabela já existe.")
        except Exception as e:
            print(f"Erro ao criar a tabela '{table_name}': {e}")
