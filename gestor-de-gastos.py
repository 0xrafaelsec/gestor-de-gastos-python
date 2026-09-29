gasto = []
while True:
    print('1 - Adicionar gastos')
    print('2 - Ver total')
    print('3 - Sair')

    opcao = input('Escolha uma opção: ')

    if opcao == '1':
        descricao = input('O que comprou? ')
        valor = float(input('Quanto custou? '))

        gasto.append([descricao, valor])
        print('Gasto registrado com sucesso!')

    elif opcao == '2':
        total = 0
        print('\n--- o seu extrato---')

        for item in gasto:
            print(f'{item[0]} -> R$ {item[1]:.2f}')
            total = total + item[1]

        print(f'\n Total gasto: R$ {total:.2f}')

    elif opcao == '3':
        print('Você escolheu: Sair!')
        break

    else:
        print('Opção inválida')