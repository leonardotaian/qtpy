lista:int = [21,15,48,98,12,34,78,14,21,54,87,98,99,23,54,78,32,45,87];

soma:float = 0;

for i in lista:
    soma += i;
    media:float = soma / len(lista);
print(f"A média dos números da lista fornecida é de {media}")