import itertools

'''
Wordlist são lista de senhas  ou autenticação para testar segurança via força bruta
'''
print('-=' * 25)
print('Word List Generator')
print('-=' * 25)
string = str(input('Caracteres utilizadas: '))
size = int(input('Tamanho da senha: '))

resultado = itertools.permutations(string, size)
count = 0
for i in resultado:
    print(''.join(i))
    count += 1
print('-=' * 25)
print(f'Fim. Um total de {count} combinações encontradas...')
print('-=' * 25)