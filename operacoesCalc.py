cont:str = "s";

while cont == "s":

    def soma(n1:int,n2:int,op:str):
        if op == '+':
            return n1 + n2;
        elif op == '-':
            return n1 - n2;
        elif op == '*':
            return n1 * n2;
        elif op == '/':
            return n1 / n2;
        else:
            msg = "Digite a operação."
            return msg
    
    nu1 = int(input("1° número: "));
    nu2 = int(input("2° número: "));
    op = str(input("Operação: "));
    print(soma(nu1,nu2,op))

    cont = str(input("Deseja realizar outra operação? s/n "))