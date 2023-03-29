# Cifra de deslocamento // Parte 01

# Alfabeto de letras
import string
letras = list(string.ascii_uppercase)

# Cifra de descolamento
def cifra_deslocamento(mensagem, chave_deslocamento):
    alfabeto = letras
    entrada_upper = mensagem.upper()
    cifra = ''
    for i in entrada_upper:
        if i in alfabeto:
            index = alfabeto.index(i)
            prox_letra = (index + chave_deslocamento) % 26
            cifra += alfabeto[prox_letra]
        else:
            cifra += i
    return cifra

# Inputs do usuário
mensagem = input('Mensagem: ')
chave = int(input('Chave: '))

# Cifra da mensagem
mensagem_cifrada = (cifra_deslocamento(mensagem, chave))

# Resultado
print(f'Mensagem cifrada:\n {mensagem_cifrada}')


# Quebra da cifra de deslocamento // Parte 02

# Função de quebra da cifra de deslocamento
def contagem(cifra):
    alfabeto = letras
    contador_letras = []
    count = 0

    while count < len(alfabeto):
        contador_loop = 0
        for letra in cifra.upper():
            if letra == alfabeto[count]:
                contador_loop += 1
        contador_letras.append(contador_loop)
        count += 1
    
    total = sum(contador_letras)
    porcentagem = []
    for i in range(len(contador_letras)):
        porcentagem.append((contador_letras[i]/total) * 100) 

    return contador_letras, porcentagem

# Quebra de chave
porcentagem_letras = contagem(mensagem_cifrada)
chave_revelada = porcentagem_letras[1].index(max(porcentagem_letras[1]))

# Chave descoberta
print(f'Chave quebrada:\n {chave_revelada}')
print('Mensagem inicial: ')

# Ajuste visual
mensagem_inicial = cifra_deslocamento(mensagem_cifrada, chave_revelada * (-1))

# Mensagem inicial
print(f' {str(mensagem_inicial.capitalize())}')