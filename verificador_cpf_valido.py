while True:
    cpf = input("Digite um CPF: ")
    novo_cpf = cpf[:-2]
    reverso = 10
    total = 0
    for index in range(19):
        if index > 8:
            index -= 9
        total += int(novo_cpf[index]) * reverso
        reverso -= 1
        if reverso < 2:
            reverso = 11
            digito = 11 - (total % 11)
            if digito > 9:
                digito = 0
            total = 0
            novo_cpf += str(digito)
    sequencia = novo_cpf == str(novo_cpf[0]) * len(cpf)
    print("Cpf valido") if (cpf == novo_cpf and not sequencia) else print("CPF invalido")
