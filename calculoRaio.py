import math

cont:bool = True;


while cont == True:
    raio:float = float(input("Raio da esfera ( cm | m | mm | in | ft | km ): "));

    print("----------------------------------------------------------------------------");
    print("Opção 1: cm (Centímetros)");
    print("Opção 2: m (Metros)");
    print("Opção 3: mm (Milímetros)");
    print("Opção 4: in (Polegadas)");
    print("Opção 5: ft (Pés)");
    print("Opção 6: km (Quilômetros)");
    print("----------------------------------------------------------------------------");

    uni:int = int(input("Qual unidade será usada para o cálculo? ( 1 | 2 | 3 | 4 | 5 | 6 ): "));



    un:str = "";

    if uni == 1:
        un = "Centímetros";
    elif uni == 2:
        un = "Metros";
    elif uni == 3:
        un = "Milímetros";
    elif uni == 4:
        un = "Polegadas";
    elif uni == 5:
        un = "Pés";
    elif uni == 6:
        un = "Quilômetros";
    else:
        un = "Error"
        if un == "Error":
            print("Opção inválida.")
        cont = False;
        again:str = (input("Deseja tentar novamente? S|N "))
        if again == "s" or "S":
            cont = True;
        else:
            cont = False;
            print("Fim da execução.")
    

    if cont == True:
        vol:float = (4 * math.pi * (raio * raio * raio)) / 3;
        print(f"O volume da esfera é de {vol:.2f} {un}.")
        again:str = str(input("Deseja realizar outro cálculo? S|N "))
        if again == "s":
            cont = True;
        else:
            cont = False;
            print("Fim da execução.")
    
    



