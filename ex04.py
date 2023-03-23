lista = []
num = int (input("Quantos elementos deseja?"))
total = 0

for i in range(num):
    val = int (input("Entre com o número: "))
    lista.append(val)

for i in range(len(lista)):
    total += lista[i] / num

print(total)