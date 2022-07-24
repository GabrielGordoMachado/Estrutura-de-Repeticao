Primeiro = 0.005
VariavelAncora = 0

print("Considere: 1 = 0.001")
print("\n_______________________________________")

while VariavelAncora < 200:
    print("|{0:.3f}| |{1:.3f}| |{2:.3f}| |{3:.3f}| |{4:.3f}|".format(Primeiro, Primeiro+0.005, Primeiro+0.010, Primeiro+0.015, Primeiro+0.020))
    Primeiro = Primeiro + 0.025
    VariavelAncora = VariavelAncora + 5