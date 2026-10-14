print("--------------------------------------------------------------------------------------------------")
print("studenti mladší 26 let mají slevu 30 %")
print("senioři ve věku 65 let a více mají slevu 20 %")
print("pokud přijdou 4 a více osob, získají místo běžných slev skupinovou slevu 25 % na všechny vstupenky")
print("--------------------------------------------------------------------------------------------------")

vstupenky = 500

osoby = int(input("Kolik vás je?: "))
if osoby >= 4:
    cena = vstupenky * osoby * 0.75
    print(f"Počet lidí ve skupince: {osoby}. Dohromady zaplatíte {cena}Kč, každý zaplatíte {cena / osoby}Kč")
else:
    vek = float(input("Zadejte váš věk: "))
    if vek >= 65:
        cena = vstupenky * osoby * 0.8
        if osoby == 1:
            print(f"Vaše cena vstupenky je {cena}Kč")
        else:
            print(f"Počet lidí ve skupince: {osoby}. Dohromady zaplatíte {cena}Kč, každý zaplatíte {cena / osoby}Kč")
    elif vek < 26:
        student = input("Jste student/i? (ano/ne): ")
        if student == "ano":
            cena = vstupenky * osoby * 0.7
            if osoby == 1:
                print(f"Vaše cena vstupenky je {cena}Kč")
            else:
                print(f"Počet lidí ve skupince: {osoby}. Dohromady zaplatíte {cena}Kč, každý zaplatíte {cena / osoby}Kč")
        else:
            cena = vstupenky * osoby
            if osoby == 1:
                print(f"Vaše cena vstupenky je {cena}Kč")
            else:
                print(f"Počet lidí ve skupince: {osoby}. Dohromady zaplatíte {cena}Kč, každý zaplatíte {cena / osoby}Kč")
    else:
        cena = vstupenky * osoby
        if osoby == 1:
            print(f"Vaše cena vstupenky je {cena}Kč")
        else:
            print(f"Počet lidí ve skupince: {osoby}. Dohromady zaplatíte {cena}Kč, každý zaplatíte {cena / osoby}Kč")