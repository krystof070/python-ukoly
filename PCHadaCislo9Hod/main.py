print("Vyberte si číslo od 1 do 100. Počítač bude hádat a vy napíšete 'v' pokud je vaše číslo větší, 'm' pokud je číslo menší a nebo 's' pokud to počítač uhodne správně. ")

pokusy = 0
odpoved = ""

dole = 1
nahore = 100

while odpoved != "s":
    tip = (dole + nahore) // 2
    pokusy += 1
    print(f"Můj tip je číslo {tip}.")
    odpoved = input("Vaše odpověď: ")
    if odpoved == "v":
        dole = tip + 1
    elif odpoved == "m":
        nahore = tip - 1
    elif odpoved == "s":
        print(f"Počítač uhodl číslo správně! Vaše číslo bylo číslo {tip}")
        print(f"Počet využitých pokusů: {pokusy}")
        break