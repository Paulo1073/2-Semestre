nome = input("Digite seu nome: ")
disciplina = input("Digite a disciplina: ") 
nota = float(input("Digite sua nota: "))
if nota < 0 or nota > 10:
    print("Nota inválida, tente novamente ")
else:
    if nota < 5.5 and nota >= 0:
        print(f'{nome}, está reprovado na disciplina de {disciplina} com nota {nota}')
    if nota >= 5.5 and nota < 6:
        nota = 6
    if nota >= 6:
        print(f'{nome}, está aprovado na disciplina de {disciplina} com nota {nota}')