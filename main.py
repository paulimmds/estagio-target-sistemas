"""
TESTE ESTÁGIO JOB ROTATION Target Sistemas

QUESTÃO 2) Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores 
anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), escreva um programa na linguagem que desejar onde, informado 
um número, ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número informado pertence ou não 
a sequência.

IMPORTANTE: Esse número pode ser informado através de qualquer entrada de sua preferência ou pode ser previamente 
            definido no código;

"""
def is_fibonacci(n):
    if n == 0 or n == 1:
        return True

    x = [0,1]

    while x[-1] < n :
        z = x[-1] + x[-2]
        if z == n:
            return True
        x.append(z)

    return False

print(is_fibonacci(0)) # True
print(is_fibonacci(1)) # True
print(is_fibonacci(12)) # False
print(is_fibonacci(90)) # False
print(is_fibonacci(34)) # True


""" 
QUESTÃO 5) Escreva um programa que inverta os caracteres de um string.

IMPORTANTE:
    a) Essa string pode ser informada através de qualquer entrada de sua preferência ou pode ser previamente 
       definida no código;
    b) Evite usar funções prontas, como, por exemplo, reverse;

"""

def reverse_string(string):
    output = ''
    while len(string) > 0:
        output = output + string[-1]
        string = string[:-1]
    return output

print(reverse_string("Hello World")) #return "dlroW olleH"
