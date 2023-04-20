# Import da biblioteca random
import random
import string

# Import de bibliotecas
import random
import string

# Cria um alfabeto contendo letras maiúsculas e minúsculas
letras = list(string.ascii_letters)

def limpar_mensagem(msg_bruta):
    # Dicionário de caracteres acentuados e seus correspondentes sem acentos
    acentuados_para_sem_acento = {
        'á': 'a', 'à': 'a', 'â': 'a', 'ã': 'a', 'ä': 'a',
        'é': 'e', 'è': 'e', 'ê': 'e', 'ë': 'e', '&': 'e',
        'í': 'i', 'ì': 'i', 'î': 'i', 'ï': 'i',
        'ó': 'o', 'ò': 'o', 'ô': 'o', 'õ': 'o', 'ö': 'o',
        'ú': 'u', 'ù': 'u', 'û': 'u', 'ü': 'u',
        'ç': 'c',
        'ñ': 'n',
        'ý': 'y'
    }

    texto_limpo = ''
    for char in msg_bruta:
        if char in letras:
            texto_limpo += char
        else:
            texto_limpo += acentuados_para_sem_acento.get(char.lower(), '')

    return texto_limpo

# Exponencial Modular
def ExpMod(a, b, n):
    if a==0:
        return 0
    elif b==0:
        return 1
    elif b%2 == 0:
        return ExpMod((a*a)%n, b//2, n)
    else:
        return (a*ExpMod((a*a)%n,(b-1)//2, n))%n

exp_a, exp_b, exp_n = input("Digite os valores de A,B,N: ").split(",")

resultado = ExpMod(int(exp_a),int(exp_b),int(exp_n))

print(f"Exponencial modular: {resultado}")


# Gerar senhas

# Gerar números primos 
def G_Primos(k):
    def verificar(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    while True:
        p = random.randint(10**(k-1), 10**k - 1)
        q = random.randint(10**(k-1), 10**k - 1)
        if verificar(p) and verificar(q):
            return p, q

# Calculo do MDC
def mdc(a, b):
    if a < b:
        a, b = b, a
    while b != 0:
        a, b = b, a % b
    return a

# MDC estendido
def mdcext(a, b):
    if b == 0:
        return[1, 0, a]
    else:
        x, y, d = mdcext(b, a % b)
        return [y, x- (a//b) * y, d]
    
# Inverso modular
def invmod(a, n):
    if mdc(a, n) != 1:
        return 0, False
    else:
        x, y, d = mdcext(a, n)
        return x%n, True
    
# Criar a chave E
def G_Chave_E(tot_n):
    while True:
        num = random.randint(1, tot_n)
        if mdc(num, tot_n) == 1:
            return num

def G_De_E(tot_n):
    while True:
        e = G_Chave_E(tot_n)
        d, verificador = invmod(e, tot_n)

        if verificador:
            return d,e

def G_Senhas(k):
    p, q = G_Primos(k)
    n = p*q
    tot_n = (p-1)*(q-1)
    d, e = G_De_E(tot_n)
    chave_publica = list((n,e))
    chave_privada = list((n,d))
    return chave_publica, chave_privada 

chave_k = input("Quantos algarismos terão os números primos?: ")
chave_publica, chave_privada  = G_Senhas(int(chave_k))
print(f"Chaves públicas (n,e) : {chave_publica[0]},{chave_publica[1]}")
print(f"Chaves privadas (n,d) : {chave_privada[0]},{chave_privada[1]}")


# Tradução
def Translate(m, n, x):
    lista_m = []
    for i in m:
        lista_m.append(ExpMod(int(i),x,n))
    
    return lista_m

# Encriptação:
def encriptar(m, n, e):
    lista_m = [] 
    for i in m:
        lista_m.append(ord(i))
    lista_m_cifrada = Translate(lista_m, n, e) 
    return lista_m_cifrada

m = input("Insira a mensagem que deseja criptografar: ")
m = limpar_mensagem(m)
n, e = input("Insira as chaves N e E separadas por vírgula: ").split(",")
n.replace(" ", "")
e.replace(" ", "")
lista_m_cifrada = encriptar(m, int(n), int(e))
print("Mensagem cifrada: ")
for i in lista_m_cifrada:
    print(f" {i}", end="")

# Decifração
def decifrar(m, n, d):
    lista_m = Translate(m, n, d)
    lista_m_decifrada = []
    for i in lista_m:
        lista_m_decifrada.append(chr(i))

    return lista_m_decifrada

m_cifrada = input("\n\nInsira a mensagem cifrada: ").split(" ")
n, d = input("\nInsira as chaves N e D: ").split(",")
n.replace(" ", "")
d.replace(" ", "")
lista_m_decifrada = decifrar(m_cifrada, int(n), int(d))
print("Mensagem decifrada:")
for i in lista_m_decifrada:
    print(f" {i}", end="")
print('\n')