lista:int = [21,15,48,98,12,34,78,14,21,54,87,98,99,23,54,78,32,45,87,210,875,984];

maior:int = 0;
for i in lista:
    if i >= maior:
        maior = i;
print(f"O maior número desta lista é {maior}");
