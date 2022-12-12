# Cifra Baconiana """" http://practicalcryptography.com/ciphers/classical-era/baconian/ """"
"""
    Essa cifra baconiana em questão possui o alfabeto completo, ou seja, cada letra possuindo seu código em específico, e ela foi feita de modo a cifrar apenas as letras maiúsculas.
"""
    # Dicionário contendo as correspondências de letras
dic = {
    "A": "00001", "B": "00010", "C": "00100", "D": "01000", "E": "10000", "F": "00011", "G": "00110", "H": "01100", "I": "11000", "J": "10001",
    "K": "00111", "L": "01110", "M": "11100", "N": "11001", "O": "10011", "P": "01111", "Q": "11110", "R": "11101", "S": "11011", "T": "10111",
    "U": "11111", "V": "00000", "W": "00101", "X": "01010", "Y": "10100", "Z": "01001",
    }

    # Mensagem a ser cifrada
mensagem = "Amanhã Teremos Alguém Chegando Aqui na Rua"
    # Processo construtor da mensagem cifrada
chave = [] # Lista de trabalho da mensagem cifrada
for i in mensagem:
    if i not in dic:
        continue
    else:
        chave.append(str(dic[i]))
mensagem_cifrada = ''.join([str(letra) for letra in chave]) # Transformando a lista de trabalho na mensagem cifrada

    # Processo decifrador da mensagem
def encontrar_chave(valor_chave): # Função que será utilizada para associar o valor cifrado a letra no dicionário de trabalho
    for chave, valor in dic.items():
        if valor_chave == valor: return chave
chave_decifrada = [] # Lista contendo as mensagem decifrada
for i in chave: chave_decifrada.append(encontrar_chave(i))
mensagem_decifrada = ''.join([str(cifra) for cifra in chave_decifrada]) # Processo de construção da mensagem decifrada

    # Mensagens
print(mensagem_cifrada) # Mensagem pós Cifrada
print(mensagem_decifrada) # Mensagem pós Decifrada