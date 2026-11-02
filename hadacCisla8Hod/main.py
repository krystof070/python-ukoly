import random
tajne_cislo = random.randint(1, 20)

tip = 0
pokusy = 5

print(f"Myslím si číslo od 1 do 20. Hádej mé číslo! Máš na to {pokusy} pokusů.")

while tip != tajne_cislo:
    tip = int(input("Zadej svůj tip: "))
    pokusy -= 1
    if tip < tajne_cislo and pokusy > 0:
        print("Moje číslo je VĚTŠÍ")
    elif tip > tajne_cislo and pokusy > 0:
        print("Moje číslo je MENŠÍ")
    elif pokusy == 0:
        print("Prohrál jsi, už nemáš žádné pokusy!")
        break

if tip == tajne_cislo:
    print(f"Grauluji, uhádl jsi moje číslo {tajne_cislo} a zbylo ti {pokusy} pokusů!")