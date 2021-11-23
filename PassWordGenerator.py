import random, string

size = 16 # Quantidade de caracteres da senha

class PassWordGenerator:

    def password(self, size):
        chars = string.ascii_letters + string.digits + '!?<,>.()_-+=&*$#@'
        rnd = random.SystemRandom()
        self.size = size
        
        return (''.join(rnd.choice(chars) for i in range(size)))
    
if __name__ == "__main__":
    
    minhasenha = PassWordGenerator()
    
    size = int(input('Tamanho da senha desejada: '))
    
    print(minhasenha.password(size))
        
        
            
        