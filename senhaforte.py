import secrets
import string

pequenas = string.ascii_lowercase
grandes = string.ascii_uppercase
numeros = string.digits
simbolos = '!@#$%¨&*()_+`{}'

tamanho = 10

def gera_senha(caracteres, tamanho):
    return ''.join(secrets.choice(caracteres) for _ in range(tamanho))

print('Caso tenha alguma especificação para a criação, utilize o menu abaixo: ')
print('1: CRIAR SENHA SEM SIMBOLOS')
print('2: CRIAR SENHA SEM LETRAS')
print('3: CRIAR SENHA SEM NUMEROS')
print('4: CRIAR SENHA NÚMERICA')
print('5: CRIAR SENHA COM TODOS')

r = input('Digite a opção selecionada: ')

if r == '1':
    print(f'A sua senha gerada foi: {gerar_senha(pequenas + grandes + numeros, tamanho)}')
elif r == '2':
    print(f'A sua senha gerada foi: {gerar_senha(numeros + simbolos, tamanho)}')
elif r == '3':
    print(f'A sua senha gerada foi: {gerar_senha(pequenas + grandes + simbolos, tamanho)}')
elif r == '4':
    print(f'A sua senha gerada foi: {gerar_senha(numeros, tamanho)}')
elif r == '5':
    print(f'A sua senha gerada foi: {gerar_senha(pequenas + grandes + numeros + simbolos, tamanho)}')
else:
    print('Opção incorreta, tente novamente!')
