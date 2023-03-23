lista = []
palavras = int(input("Quantas palavras deseja?"))

for i in range(palavras):
    letra = (input("Entre com as palavras: "))
    lista.append(letra)
    
for palavras in lista:
      
    if palavras.startswith("a") or palavras.startswith("A"):
        print(palavras)
   