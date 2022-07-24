Primeiro = 1222
VariavelAncora = 1
Soma = 0

while VariavelAncora < 51:
    if Primeiro % 2 == 0:
        Soma = Soma + Primeiro
        VariavelAncora = VariavelAncora + 1
    Primeiro = Primeiro + 1

print(Soma)


