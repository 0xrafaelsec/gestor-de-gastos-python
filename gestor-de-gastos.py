gasto = []

try:
    arq_gastos = open('gastos.txt', 'r')
    for i in arq_gastos:
        pedaco = i.split(' - ')
        quantidade = int(pedaco[0])
        descricao = pedaco[1]
        valor = float(pedaco[2])
        gasto.append([quantidade, descricao, valor])
    arq_gastos.close()

except FileNotFoundError:
    pass

while True:
    print('1 - Adicionar gastos')
    print('2 - Ver total')
    print('3 - Remover gastos')
    print('4 - Sair')

    opcao = input('Escolha uma opção: ')

    if opcao == '1':
        while True:
            descricao = input('O que comprou? ')
            if descricao.strip() == '':
                print('A descrição não pode ficar vazia. Tente novamente!')
            else:
                break

        while True:
            try:
                valor = float(input('Quanto custou? '))
                break

            except ValueError:
                print('Erro: Valor incorreto. Digite apenas números e tente novamente')

        while True:
            try:
                quantidade = int(input('Quantos você comprou? '))
                break

            except ValueError:
                print('Erro: Quantidade incorreta. Digite apenas números inteiros.')

        encontrado = False

        for item in gasto:
            if descricao.upper() == item[1].upper() and valor == item[2]:
                print('Quantidade atualizada com sucesso!')
                encontrado = True
                break

        if not encontrado:
            gasto.append([quantidade, descricao, valor])
            print('Gasto registrado com sucesso!')

        arq_gastos = open('gastos.txt', 'a')
        arq_gastos.write(f'{quantidade} - {descricao} - {valor}\n')
        arq_gastos.close()

    elif opcao == '2':
        if len(gasto) == 0:
            print('Nenhum item na lista!')
        else:
            TOTAL = 0
            print('\n--- O SEU EXTRATO ---')

            for item in gasto:
                subtotal = item[0] * item[2]
                print(f'{item[0]} - {item[1]}: R$ {item[2]:.2f} subtotal: R$ {subtotal:.2f} ')
                TOTAL = TOTAL + subtotal

            print(f'\n O total gasto foi: R$ {TOTAL:.2f}')

    elif opcao == '3':
        if len(gasto) == 0:
            print('Nenhum item na lista!')

        else:
            for item in gasto:
                print(f'{item[1]}')

            remover = input('Quais itens quer remover? ')

            for item in gasto:
                if remover.upper() == item[1].upper():
                    qtd_remover = int(input('Quantos itens quer remover? '))

                    if qtd_remover >= item[0]:
                        gasto.remove(item)
                        print('Item removido com sucesso!')

                    else:
                        item[0] -= qtd_remover
                        print('Quantidade atualizada com sucesso!')

                    arq_gasto = open('gastos.txt', 'w')
                    for i in gasto:
                        arq_gasto.write(f'{i[0]} - {i[1]} - {i[2]}\n')
                    arq_gasto.close()

                    break

    elif opcao == '4':
        sair = input('Você quer sair: S/N ? ').upper()
        if sair == 'S':
            break
        else:
            print('Você voltou ao MENU!')

    else:
        print('Opção inválida')