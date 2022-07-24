Primeiro = 100
Numero = 1

while Primeiro < 1001:
    if Primeiro % 12 == 0:
        print("{0} | {1} | {2} | {3} |  {4}º - {5}º".format(Primeiro, Primeiro + 12, Primeiro + 24, Primeiro + 36, Numero, Numero + 4))
        Numero = Numero + 4
        Primeiro = Primeiro + 47
    Primeiro = Primeiro + 1
