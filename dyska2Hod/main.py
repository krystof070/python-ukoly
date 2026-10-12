# *******************************
# Kalkulačka spropitného
# 30.9. 2026
# *******************************

print("Vítejte v kalkulačce spropitného.")
celkova_cena = float(input("Zadejte celkovou cenu: "))
spropitne = int(input("Zadejte spropitné v %: "))
pocet_lidi = int(input("Zadejte počet lidí u stolu: "))

spropitne = 1 + spropitne / 100
celkova_cena *= spropitne
cena_clovek = round(celkova_cena / pocet_lidi, 2)
print("Celková cena je " + str(celkova_cena) + "Kč.")
print("Každý u stolu zaplatí " + str(cena_clovek) + "Kč.")