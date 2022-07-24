Primeiro = 0.05
VariavelAncora = 0
print("Considere: 1 = 0.01")
print("\n__________________________________")
while VariavelAncora < 20:
 print("|{0:.2f}| |{1:.2f}| |{2:.2f}| |{3:.2f}| |{4:.2f}|".format(Primeiro, Primeiro+0.05, Primeiro+0.10, Primeiro+0.15, Primeiro+0.20))
 Primeiro = Primeiro + 0.25
 VariavelAncora = VariavelAncora + 5