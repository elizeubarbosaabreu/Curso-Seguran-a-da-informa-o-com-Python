import hashlib

class conversor:
    def md5(self, string:str):
        self.string = string
        return (hashlib.md5(string.encode("utf-8"))).hexdigest()
    def sha1(self, string:str):
        self.string = string
        return (hashlib.sha1(string.encode("utf-8"))).hexdigest()
    def sha256(self, string:str):
        self.string = string
        return (hashlib.sha256(string.encode("utf-8"))).hexdigest()
    def sha512(self, string:str):
        self.string = string
        return (hashlib.sha512(string.encode("utf-8"))).hexdigest()
            
    
if __name__ == "__main__":
    

    app = conversor()
    
    string = str(input('Digite um texto para Cryptografar: '))    
    
    escolha = input('''
Escolha O tipo de criptografia:
    1) MD5
    2) SHA1
    3) SHA256
    4) SHA512
Sua escolha: '''
                    )
    if escolha == '1':
        print(app.md5(string))
    elif escolha == '2':
        print(app.sha1(string))
    elif escolha == '3':
        print(app.sha256(string))
    elif escolha == '4':
        print(app.sha512(string))
    else:
        print('Algo de errado não está certo. bye')
        