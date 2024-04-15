cont:bool = True;

while cont == True:
    n:int = int(input("Número que deseja verificar: "));

    if n == 0:
        print("Este é zero meu amigo.")
    elif n % 2 == 0:
        print("Número par.");
    else:
        print("Número ímpar.");
    cont = True;