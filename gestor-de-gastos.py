
gasto = []
while True:
    print('1 - Adicionar gastos')
    print('2 - Ver total')
    print('3 - Sair')
    
    opcao = input('Escolha uma opção: ')
    
    if opcao == '1':
        descricao = input('O que comprou? ')
        valor = float(input('Quanto custou? '))
        quantidade = int(input('Quantos você comprou? '))
        
        gasto.append([quantidade, descricao, valor])
        print('Gasto registrado com sucesso!')
        
    elif opcao == '2':
         if len(gasto) == 0:
             print('Nenhum item na lista! ')
         else:
             total = 0
             print('\n--- O SEU EXTRATO ---')
         
             for item in gasto:
                 subtotal = item[0] * item[2]
                 print(f'{item[0]} - {item[1]}: R$ {item[2]:.2f} subtotal: R$ {subtotal:.2f} ') 
                 total = total + subtotal
          
             print(f'\n O total gasto foi: R$ {total:.2f}')
          
    elif opcao == '3':
        sair = input('Você quer sair: S/N ? ').upper()
        if sair == 'S':
            break
        else:
            print('Você voltou ao MENU!')
       
    else:
        print('Opção inválida')
        