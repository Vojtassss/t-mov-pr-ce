import random

auta = ["BMW", "Mercedes", "Audi", "Škoda", "Honda"]
print(auta)
hodnota = input("Zadejte jiné další auto:")


auta.append(hodnota)

for i in auta :
    print(i)

nahodnahodnota = random.choice(auta)

print ("Náhodná hodnota je:", nahodnahodnota)