#Imprimir una lista de ingredientes
chipa = ["queso","harina","sal","agua"]
print(chipa)

for chipas in chipa:
    if "queso" in chipas:
        print("El ingrediente si fue comprado")

chipa.append("Cebolla")

print(chipa)

chipa.insert(0,"mandioca")
print(chipa)

chipa.remove("sal")
print(chipa)

chipa.pop()
print(chipa)

del chipa[3]
print(chipa)

