Primeiro = 0.01
VariavelAncora = 1
print("Considere: 1 = 0.01")
print("\n_____________________________________________________________________")
while VariavelAncora < 200:
 print("|{0:.2f}| |{1:.2f}| |{2:.2f}| |{3:.2f}| |{4:.2f}| |{5:.2f}| |{6:.2f}| |{7:.2f}| |{8:.2f}| |{9:.2f}|".format(Primeiro, Primeiro + 0.02, Primeiro + 0.04, Primeiro + 0.06, Primeiro + 0.08, Primeiro + 0.1, Primeiro + 0.12, Primeiro + 0.14, Primeiro + 0.16, Primeiro + 0.18))
 VariavelAncora = VariavelAncora + 20
 Primeiro = Primeiro + 0.2