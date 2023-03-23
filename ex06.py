lista = []

num = int(input("Quantos elementos deseja?"))

for i in range(num):
 num = int(input("Digite os números: "))
 lista.append(num)

lista.sort(reverse = True)   
print(lista)