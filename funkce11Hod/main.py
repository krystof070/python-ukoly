def spocitej_obsah(a, b):
    if a <= 0 or b <= 0:
        return None
    obsah = a * b
    return obsah

print("Výpoet rozlohy bytu")
pocet_mistnosti = int(input("Zadej počet místností: "))
mistnost = 1
obsah = 0
while mistnost <= pocet_mistnosti:
    print(f"Zadej rozměry {mistnost}. mistnosti")
    a = int(input("Zadej rozměr 'a': "))
    b = int(input("Zadej rozměr 'b': "))
    obsah_mistnosti += spocitej_obsah(a, b)
    if obsah_mistnosti != None:
        obsah += obsah_mistnosti
        mistnost += 1
print(f"Celková výměra bytu je {obsah}")