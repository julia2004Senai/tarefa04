lista = []
num = int(input("Quantos elementos deseja?"))

for i in range(num):
    val = int(input("Entre com o número: "))
    lista.append(val) 
    
maior_numero = lista[0]

for numero in lista:
    if numero > maior_numero:
        maior_numero = numero
        
menor_numero = lista[0]

for numero in lista:
    if numero < menor_numero:
        menor_numero = numero
        
        
print(menor_numero, maior_numero)