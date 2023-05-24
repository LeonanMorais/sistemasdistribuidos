import socket
import json


def main():
    # Configurações do cliente
    host = 'localhost'
    porta = 12345

    # Criação do socket TCP/IP
    cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Conecta ao servidor
    cliente.connect((host, porta))

    # Realiza o login
    usuario = input("Usuário: ")
    senha = input("Senha: ")

    mensagem_login = json.dumps({
        "tipo": "login",
        "conteudo": {
            "usuario": usuario,
            "senha": senha
        }
    })
    cliente.sendall(mensagem_login.encode())

    # Aguarda a resposta do servidor
    dados = cliente.recv(1024)
    resposta = json.loads(dados.decode())

    print(f'Resposta do servidor: {resposta["conteudo"]}')

    # Verifica se o login foi bem-sucedido
    if resposta["conteudo"] == "Login bem-sucedido.":
        while True:
            # Obtém a mensagem do usuário
            mensagem = input('Digite uma mensagem (ou "sair" para encerrar): ')

            if mensagem.lower() == 'sair':
                break

            # Monta a requisição
            requisicao = {
                "tipo": "requisicao",
                "usuario": usuario,
                "conteudo": mensagem
            }

            # Envia a requisição ao servidor
            mensagem_requisicao = json.dumps(requisicao)
            cliente.sendall(mensagem_requisicao.encode())

            # Aguarda a resposta do servidor
            dados = cliente.recv(1024)
            resposta = json.loads(dados.decode())

            print(f'Resposta do servidor: {resposta["conteudo"]}')

    # Encerra a conexão
    cliente.close()


if __name__ == '__main__':
    main()
