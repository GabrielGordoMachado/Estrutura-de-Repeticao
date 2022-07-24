Primeiro = int(input())
Segundo = Primeiro - 1
Equacao = Primeiro * Segundo

while Equacao > 1:
    Segundo = Segundo - 1
    Equacao = Equacao * Segundo
    print(Equacao)