Primeiro = -1
VariavelAncora = 1
Numero = 1

while VariavelAncora < 51:
    if Primeiro % -2 == 0:
        if Primeiro == -2:
            print("{0} | {1}º".format(Primeiro, Numero))
            VariavelAncora = VariavelAncora + 1
            Numero = Numero + 1

    elif Primeiro % -3 == 0:
        if Primeiro == -3:
            print("{0} | {1}º".format(Primeiro, Numero))
            VariavelAncora = VariavelAncora + 1
            Numero = Numero + 1

    elif Primeiro % -5 == 0:
        if Primeiro == -5:
            print("{0} | {1}º".format(Primeiro, Numero))
            VariavelAncora = VariavelAncora + 1
            Numero = Numero + 1

    elif Primeiro % -7 == 0:
        if Primeiro == -7:
            print("{0} | {1}º".format(Primeiro, Numero))
            VariavelAncora = VariavelAncora + 1
            Numero = Numero + 1

    elif Primeiro == -11:
        print("{0} | {1}º".format(Primeiro, Numero))
        VariavelAncora = VariavelAncora + 1
        Numero = Numero + 1

    else:
        print("{0} | {1}º".format(Primeiro, Numero))
        VariavelAncora = VariavelAncora + 1
        Numero = Numero + 1
    Primeiro = Primeiro - 1
