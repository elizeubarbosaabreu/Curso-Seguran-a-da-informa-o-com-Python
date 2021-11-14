import hashlib

class CompararHashes:
    def compara_arquivos(self, file1, file2):
        self.file1 = file1
        self.file2 = file2
        
        hash1, hash2 = hashlib.new('ripemd160'), hashlib.new('ripemd160')

        hash1.update(open(file1, 'rb').read())
        hash2.update(open(file2, 'rb').read())

        if hash1.digest() != hash2.digest():
            return(f'Os arquivos {file1} e {file2} são diferentes...')
        else:
            return(f'Os arquivos {file1} e {file2} são iguais...\nAmbos posuem o hash {hash1.digest()}...')
if __name__ == "__main__":
    
    compara = CompararHashes()
    
    file1 = 'a.txt'
    file2 = 'b.txt'
    
    print(compara.compara_arquivos(file1, file2))


