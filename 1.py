# from azure.storage.queue import QueueServiceClient, QueueClient
# import os
#
# def main1():
#     cn ="""DefaultEndpointsProtocol=http;AccountName=devstoreaccount1;AccountKey=Eby8vdM02xNOcqFlqUwJPLlmEtlCDXJ1OUzFT50uSRZ6IFsuFq2UVErCz4I6tq/K1SZFPTOtr/KBHBeksoGMGw==;QueueEndpoint=http://127.0.0.1:10001/devstoreaccount1;"""
#     # Configurando a conexão com a conta do Azure Storage
#     connect_str = cn
#     queue_name = "minhafila"
#
#     # Criando o serviço de fila
#     queue_service = QueueServiceClient.from_connection_string(connect_str)
#     queue_client = queue_service.get_queue_client(queue_name)
#
#     # Criando uma fila (se não existir)
#     queue_client.create_queue()
#
#     # Enviando uma mensagem para a fila
#     message_content = "Minha mensagem de exemplo"
#     queue_client.send_message(message_content)
#     print(f"Mensagem enviada: {message_content}")
#
#     # Recebendo uma mensagem da fila
#     messages = queue_client.receive_messages(messages_per_page=1)
#     for message in messages:
#         print(f"Mensagem recebida: {message.content}")
#         # Excluindo a mensagem da fila após o processamento
#         queue_client.delete_message(message)
#         print("Mensagem excluída da fila")
#
#
# if __name__ == "__main__":
#     main1()
