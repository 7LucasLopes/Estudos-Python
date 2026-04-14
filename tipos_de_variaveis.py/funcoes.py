import os
os.system("cls")

# Exemplo
def saudacao(nome):
    print(f"Olá, {nome}.")

print("\nChamando a função saudação")

saudacao("Sophia")
saudacao("Lucas")

#Função com retorno
def quadrado(numero):
    resultado = numero ** 2
    return resultado

print("\nChamando função ao quadrado")
resultado_quadrado = quadrado(9)
print(f"Resultado do número ao quadrado: {resultado_quadrado}")

# Função com múltiplos parametros 

def soma(numero1, numero2):
    resultado = numero1 + numero2
    return resultado

print("\nChamando a função soma")
numero1 = 30
numero2 = 25
resultado_soma = soma(numero1, numero2)
print(f"A soma entre {numero1} e {numero2} é igual a: {resultado_soma}")
