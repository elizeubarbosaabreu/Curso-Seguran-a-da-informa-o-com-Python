import os, time

class testes:
    
    def pingar(self, pacotes, host):
        self.pacotes = pacotes
        self.host = host
        
        try:
            return os.system(f'ping -n {pacotes} {host}')
        except:
            return 'ERRO'
        
    def pingar_simples(self, host):        
        self.host = host
        
        try:
            return os.system(f'ping {host}')
        except:
            return 'ERRO'
        
    def pingar_txt(self, filename, pacotes):
        
        self.pacotes = pacotes
        self.filename = filename
        
        with open(filename, 'r') as file:
            hosts = file.read()
            hosts = hosts.split()
            
        for host in hosts:            
            try:
                return os.system(f'ping -n {pacotes} {host}')                
            except:
                return 'ERRO'
            time.sleep(5)

if __name__ == "__main__":
    
    app = testes()
    
    pacotes = int(input('Entre com o numero de pacotes para pingar: '))
    
    host = input('Entre com o host ou ip para pingar: ')
    
    for i in range(10):
        app.pingar_simples(host)
        
    app.pingar(pacotes, host)
    
    app.pingar_txt('hosts.txt', pacotes)