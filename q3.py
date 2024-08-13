nome = input("Digite seu nome: ")
idade = int(input("Qual sua idade: "))

if idade >= 16:
    print(f'ola {nome} você tem {idade} ano(s),você poderá tirar o titulo')
else:
    print(f'ola {nome} você tem {idade} ano(s),você não poderá tirar o titulo')