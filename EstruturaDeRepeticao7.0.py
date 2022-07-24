Primeiro = -1
VariavelAncora = 1
Soma = 0

while VariavelAncora < 31:
    if Primeiro % -2 != 0:
       VariavelAncora = VariavelAncora + 1
       Soma = Soma + Primeiro
    Primeiro = Primeiro - 1

print(Soma)