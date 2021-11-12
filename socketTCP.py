import socket, sys

def main():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
    except socket.error as e:
        print('A conexão falhou!!!')
        print(f'Erro: {e}')
        sys.exit()
    print('Host criado com sucesso!')
    
    HostAlvo = str(input('Digite o Ip ou Host para ser conectado: '))
    Porta = int(input('Digite a porta para ser explorada: '))
    
    try:
        s.connect((HostAlvo, Porta))
        print(f'Cliente TCP conectado com sucesso no host: {HostAlvo}, porta: {Porta}...')
        s.shutdown(2)
    except socket.error as e:
        print(f'Não foi possível conectar ao host: {HostAlvo}, porta: {Porta}...')
        print(f'Erro: {e}')
        sys.exit()
          
    
if __name__ == "__main__":
    main()

