cas = float(input("Zadej čas: "))

if cas<0:
    print("Hodina nemůže být záporná.")
elif cas<5:
    print("Dobrou noc!")
elif cas<10:
    print("Dobré ráno!")
elif cas<12:
    print("Dobré dopoledne!")
elif cas == 12:
    print("Dobré poledne!")
elif cas<17:
    print("Dobré odpoledne!")
elif cas<22:
    print("Dobrý večer!")
elif cas<24:
    print("Dobrou noc!")
else:
    print("Zadávejte platné hodiny.")
