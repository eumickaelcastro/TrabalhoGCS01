def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        return "Erro: divisão por zero!"
    return a / b

def potencia (a,b):
    return a**b

def raiz_quadrada(a):
    if a < 0:
        return "Erro: não existe raiz real de número negativo!"
    return a ** 0.5