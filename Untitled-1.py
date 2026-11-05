vstup = input("Zadaj čísla oddelené medzerou: ")
cisla = [int(x) for x in vstup.split()]

for i in range(len(cisla) - 1):
    for j in range(i + 1, len(cisla)):
        if cisla[i] > cisla[j]:
            cisla[i], cisla[j] = cisla[j], cisla[i]

print("Zoradené:", cisla)