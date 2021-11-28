import ctypes, os

pasta = str(input('Digite ou cole o caminho do arquivo ou diretório a ser ocultado: '))

atributo_ocultar = 0x02


try:
    
    # No Windows
    retorno = ctypes.windll.kernel32.SetFileAttributeW(pasta, atributo)
    if retorno:
        print("Arquivo ocultado")
    else:
        print("Arquivo não ocultado")
except:
    
    # No Linux, ocultamos arquivos adicionando um "." antes do nome
    rename = pasta.split('/')
    rename = rename[-1]
    caminho_relativo = pasta.replace(rename, '')
    
    os.system(f'mv {pasta} {caminho_relativo}.{rename}')
    print(f"Arquivo {rename} ocultado")
    
    