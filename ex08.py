names = input("Digite uma lista de nomes separados por vírgula: ")
names_list = names.split(",")

longest_name = "" 
shortest_name = names_list[0] 

for name in names_list:
    if len(name) > len(longest_name):
        longest_name = name
    if len(name) < len(shortest_name):
        shortest_name = name

print("O nome mais longo é:", longest_name)
print("O nome mais curto é:", shortest_name)