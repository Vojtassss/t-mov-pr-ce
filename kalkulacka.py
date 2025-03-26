while True:
    cislo1 = int(input("Zadejte první číslo: "))
    cislo2 = int(input("Zadejte druhé čislo: "))
    operace = input("Zadejte kterou chcete použít početní operaci? (Součet/Rozdíl/Součin/Podíl):")
    if operace == "Součet":
        print("Součet:", cislo1 + cislo2)
    elif operace == "Rozdíl":
        print("Rozdíl:", cislo1 - cislo2)
    elif operace == "Součin":
        print("Součin:", cislo1 * cislo2)
    elif operace == "Podíl":
        print("Podíl:", cislo1 / cislo2)
    bye = input("Pokud nechcete program opakovat napište (exit) ")
    if bye == "exit":
        break