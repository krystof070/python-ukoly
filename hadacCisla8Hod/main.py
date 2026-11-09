import random
tajne_cislo = random.randint(1, 20)

tip = 0
pokusy = 5

print(f"Myslím si číslo od 1 do 20. Hádej mé číslo! Máš na to {pokusy} pokusů.")

while tip != tajne_cislo:
    tip = int(input("Zadej svůj tip: "))
    if tip < 1 or tip > 20:
        print("Zadal jste číslo mimo interval!")
    elif tip < tajne_cislo and pokusy > 0:
        print("Moje číslo je VĚTŠÍ")
        pokusy -= 1
    elif tip > tajne_cislo and pokusy > 0:
        print("Moje číslo je MENŠÍ")
        pokusy -= 1
    elif pokusy == 0:
        print(f"Bohužel ti došly pokusy! Tajné číslo bylo {tajne_cislo}.")
        break
    elif tip == tajne_cislo:
        pokusy -= 1
        print(f"Gratuluji! Uhodl jsi číslo {tajne_cislo}, zbylo ti {pokusy} pokusů.")
        break