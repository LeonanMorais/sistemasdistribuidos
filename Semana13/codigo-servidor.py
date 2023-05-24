import socket
import json

# Dicionário de usuários e senhas
usuarios = {
    "JP": "Viking",
    "E++": "meninodeprograma",
    "Cintra": "senior"
}


def processar_requisicao(requisicao):
    # Verifica se o usuário está autenticado
    if "usuario" not in requisicao:
        return "Erro: Usuário não autenticado. Faça o login primeiro."

    # Aqui você pode implementar a lógica de processamento da requisição
    # e retornar a resposta adequada
    if requisicao["conteudo"] == "oi":
        return f"Olá, {requisicao['usuario']}!"
    else:
        return f"Desculpe, {requisicao['usuario']}, não entendi sua requisição."


def autenticar_usuario(usuario, senha):
    # Verifica se o usuário e senha correspondem aos cadastrados
    if usuario in usuarios and usuarios[usuario] == senha:
        return True
    else:
        return False


def main():
    # Configurações do servidor
    host = 'localhost'
    porta = 12345

    # Criação do socket TCP/IP
    servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Vincula o socket à porta e endereço local
    servidor.bind((host, porta))

    # Inicia escuta por conexões
    servidor.listen(1)

    print(f'Servidor ouvindo em {host}:{porta}')

    while True:
        # Aguarda por novas conexões
        conexao, endereco = servidor.accept()

        print(f'Conexão estabelecida com {endereco[0]}:{endereco[1]}')

        try:
            while True:
                # Recebe dados do cliente
                dados = conexao.recv(1024)

                if dados:
                    requisicao = json.loads(dados.decode())
                    print(f'Requisição recebida: {requisicao}')

                    # Verifica se o usuário está autenticado
                    if "usuario" not in requisicao:
                        # Verifica se é uma tentativa de login
                        if requisicao["tipo"] == "login":
                            usuario = requisicao.get("conteudo", {}).get("usuario")
                            senha = requisicao.get("conteudo", {}).get("senha")

                            if autenticar_usuario(usuario, senha):
                                # Autenticação bem-sucedida
                                requisicao["usuario"] = usuario
                                resposta = {"tipo": "resposta", "conteudo": "Login bem-sucedido."}
                            else:
                                # Autenticação falhou
                                resposta = {"tipo": "resposta", "conteudo": "Login falhou. Usuário ou senha inválidos."}
                        else:
                            # Requisição inválida (sem autenticação)
                            resposta = {"tipo": "resposta", "conteudo": "Erro: Usuário não autenticado."}
                    else:
                        # Usuário autenticado, processa a requisição
                        resposta = processar_requisicao(requisicao)

                    print(f'Resposta enviada: {resposta}')

                    # Envia a resposta ao cliente
                    mensagem_resposta = json.dumps(resposta)
                    conexao.sendall(mensagem_resposta.encode())

                else:
                    # Não há mais dados a receber, encerra a conexão
                    print(f'Conexão encerrada com {endereco[0]}:{endereco[1]}')
                    conexao.close()
                    break

        except Exception as e:
            print(f'Ocorreu um erro na conexão com {endereco[0]}:{endereco[1]}: {str(e)}')
            conexao.close()


if __name__ == '__main__':
    main()
