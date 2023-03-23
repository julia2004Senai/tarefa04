lista = []
num = int(input("Quantos elementos deseja?"))
lista_sem_duplicatas = []
for i in range(num):
    val = int(input("Entre com o número: "))
    lista.append(val)
    

while lista:
    elemento = lista.pop(0)
    if elemento not in lista_sem_duplicatas:
        lista_sem_duplicatas.append(elemento)
print(lista_sem_duplicatas)