import string
import secrets

characters = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation

def pedir_numero():
    while True:
        entrada = input("Digite o tamanho da senha (de 6 a 18): ")
        try:
            tamanho = int(entrada)
        except ValueError:
            print("Por favor apenas números")
            continue

        if 6 <= tamanho <= 18:
            return tamanho
        else:
            print("entre 6 e 18")

def gerar_senha(tamanho):
    senha = ''.join(secrets.choice(characters) for i in range(tamanho))
    return senha


tamanho = pedir_numero()
senha = gerar_senha(tamanho)
print("senha gerada: ", senha)
