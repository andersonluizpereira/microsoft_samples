import os
from azure.storage.queue import QueueServiceClient


class AzureConfig:
    @staticmethod
    def get_queue_service_client():
        # String de conexão para o emulador local
        connect_str = os.getenv("AZURE_STORAGE_QUEUE_CONNECTION_STRING")
        return QueueServiceClient.from_connection_string(connect_str)
