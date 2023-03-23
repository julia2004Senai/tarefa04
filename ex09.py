lista = []
num = int(input("Quantos elementos deseja?"))

for i in range(num):
    val = int(input("Entre com o número: "))
    lista.append(val)
    
for num in lista:
      
    if num > 10:
       print(num, end = " ")