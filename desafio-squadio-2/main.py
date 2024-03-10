MAX_ITENS = 3
itens = []

for i in range(0, MAX_ITENS):
    item = str(input(f"Insira o item {i + 1}: "))
    itens.append(item)

print("Lista de itens:")
for item in itens:
    print(f"- {item}")