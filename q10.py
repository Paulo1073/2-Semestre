op = '1'
while op != '0':
    print('''---------Calculadora---------
    Escolha a Operação:
    1 - soma
    2 - subtração
    3 - multiplicação
    4 - Divisão
    5 - exponenciação
    0 - sair
------------------------------
          ''')
    nn = int(input(print('Qual a Operação: ')))
    if nn < 0 or nn > 5:
        print('Dados Invalidos,tente Novemente')
        break
    elif nn == 1:
        n1 = int(input(print('Digite o primeiro Numero')))
        n2 = int(input(print('Digite o Segundo Numero')))
        m = n1+n2
        print(f'A Soma dos Dois é "{m}"')
        rr = input(print("Deseja Continuar(s/n): "))
        if rr == 'n':
            break

    elif nn == 2:
        n1 = int(input(print('Digite o primeiro Numero')))
        n2 = int(input(print('Digite o Segundo Numero')))
        m = n1-n2
        print(f'A Subtração dos Dois é "{m}"')
        rr = input(print("Deseja Continuar(s/n): "))
        if rr == 'n':
            break


    elif nn == 3:
        n1 = int(input(print('Digite o primeiro Numero')))
        n2 = int(input(print('Digite o Segundo Numero')))
        m = n1*n2
        print(f'A Multiplicação dos Dois é "{m}"')
        rr = input(print("Deseja Continuar(s/n): "))
        if rr == 'n':
            break


    elif nn == 4:
        n1 = int(input(print('Digite o primeiro Numero')))
        n2 = int(input(print('Digite o Segundo Numero')))
        m = n1/n2
        print(f'A Divisão dos Dois é "{m}"')
        rr = input(print("Deseja Continuar(s/n): "))
        if rr == 'n':
            break


    elif nn == 5:
        n1 = int(input(print('Digite o primeiro Numero')))
        n2 = int(input(print('Digite o Segundo Numero')))
        m = n1**n2
        print(f'A Exponenciação dos Dois é "{m}"')
        rr = input(print("Deseja Continuar(s/n): "))
        if rr == 'n':
            break


    elif nn == 0:
        break