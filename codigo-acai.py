from time import sleep
print('    \033[1;30;45mMONTE SEU COPO!\033[m')
print('  \033[1;30;45mESCOLHA UM TAMANHO\033[m')
print(' 200ml    500ml    750ml')
tamanho = '', '10', '15', '18'
print('R$10.00  R$15.00  R$18,00 ')
n1 = int(input('  [1]      [2]      [3] : '))
print('   \033[1;30;45mESCOLHA 1 SORVETE:\033[m')
sabores = '', 'Açai', 'Ninho', 'Brigadeiro'
print('', 'Açai, Ninho, Brigadeiro ')
sorvete = int(input(' [1]    [2]     [3]   : '))
print('\033[1;30;45mESCOLHA 3 ACOMPANHAMENTOS:\033[m ')
acom = '', 'Paçoca', 'Mms', 'Leite em pó', 'Leite Con', 'Chocobol', 'Bis'
print('''Paçoca   Mms   Leite em pó   Leite Con   Chocobol   Bis
  [1]    [2]       [3]          [4]        [5]      [6]: ''')
acompanhamento1 = int(input('Primeira opçao: '))
acompanhamento2 = int(input('Segunda opçao: '))
acompanhamento3 = int(input('Terceira opçao: '))
print('   \033[1;30;45mESCOLHA 2 FRUTAS\033[m')
frut = '', 'Banana', 'Morango', 'Kiwi', 'Manga'
print('''Banana, Morango, Kiwi, Manga:
  [1]      [2]    [3]    [4]''')
fruta1 = int(input('Primeira fruta: '))
fruta2 = int(input('Segunda fruta: '))
pergunta1 = str(input('\033[1;30;43mGostaria de 2 ADICIONAIS por só mais R$2,00?\033[m ')).lower().strip()[0]
if pergunta1 == 's':
    print('\033[1;30;45m2 ADICIONAIS R$2.00:\033[m ')
    adi = '', 'Bis', 'Rolinho', 'Nutella', 'Leite con', 'Granulado'
    print('''Bis, Rolinho, Nutella, Leite con, Granulado:
[1]    [2]      [3]       [4]        [5]''')
    adicionais1 = int(input('Primeiro Adicional: '))
    adicionais2 = int(input('Segundo Adicional: '))
    print('\033[1;30;43m=======PEDIDO=======\033[m')
    print('\033[1;30;43mCOPO:\033[m \033[1;30;42mR${}.00\033[m'.format(tamanho[n1]))
    print('\033[1;30;43mSORVETE:\033[m \033[1;30;42m{}\033[m'.format(sabores[sorvete]))
    print(f'\033[1;30;43mACOMPANHAMENTO:\033[m \033[1;30;42m{acom[acompanhamento1]}, {acom[acompanhamento2]}, {acom[acompanhamento3]}\033[m')
    print(f'\033[1;30;43mFRUTAS:\033[m \033[1;30;42m{frut[fruta1]},{frut[fruta2]}\033[m')
    print('\033[1;30;43mADICIONAIS:\033[m \033[1;30;42m{}, {}\033[m'.format(adi[adicionais1], adi[adicionais2]))
    s = int(tamanho[n1]) + 2
    print('\033[1;30;43mTOTAL:\033[m \033[1;30;42mR${:.2f}\033[m'.format(s))
    print('\033[1;30;45m=== FORMA DE PAGAMENTO ===\033[m')
    print('DINHEIRO    DEBITO    CREDITO')
    print('  [1]        [2]        [3]')
    pagamento = int(input('Opçao: '))
    while pagamento <= 3 and pagamento > 0:
        if pagamento > 3:
            print('Opçao digitada invalida! ')
        if pagamento == 2:
            print('   \033[1;30;45m==== DEBITO ====\033[m')
            sleep(1)
            senha = str(input('Pode digitar a senha...')).strip()
            print('    ...\033[1;30;43mPROCESSADO\033[m...')
            sleep(3)
            print('\033[1;30;42m=====COMPRA APROVADA=====\033[m')
            print('\033[1;30;45mMUITO OBRIGADO! ATÉ MAIS!\033[m')
            break
        elif pagamento == 3:
            print('   \033[1;30;45m==== CREDITO ====\033[m')
            sleep(1)
            senha = str(input('Pode digitar a senha...')).strip()
            print('    ...\033[1;30;43mPROCESSADO\033[m...')
            sleep(3)
            print('\033[1;30;42m=====COMPRA APROVADA=====\033[m')
            print('\033[1;30;45mMUITO OBRIGADO! ATÉ MAIS!\033[m')
            break
        else:
            print('   \033[1;30;45m==== DINHEIRO ====\033[m')
            dinheiro = float(input('\033[1;30;43mDIGITE UM VALOR ACIMA DO "TOTAL":\033[m R$ '))
            print('Seu troco é \033[1;30;45mR${:.2f}\033[m'.format(dinheiro - s))
            print('\033[1;30;45mMUITO OBRIGADO! ATÉ MAIS!\033[m')
            break
else:
    adicionais = 0
    print('\033[1;30;43m=======PEDIDO=======\033[m')
    print('\033[1;30;43mCOPO:\033[m \033[1;30;42mR${}.00\033[m'.format(tamanho[n1]))
    print('\033[1;30;43mSORVETE:\033[m \033[1;30;42m{}\033[m'.format(sabores[sorvete]))
    print(f'\033[1;30;43mACOMPANHAMENTO:\033[m \033[1;30;42m{acom[acompanhamento1]}, {acom[acompanhamento2]}, {acom[acompanhamento3]}\033[m')
    print(f'\033[1;30;43mFRUTAS:\033[m \033[1;30;42m{frut[fruta1]},{frut[fruta2]}\033[m')
    print('\033[1;30;43mADICIONAIS:\033[m \033[1;30;42m{}\033[m'.format(0))
    soma = tamanho[n1]
    print('\033[1;30;43mTOTAl:\033[m \033[1;30;42mR${}.00\033[m'.format(soma))
    print('\033[1;30;45m=== FORMA DE PAGAMENTO ===\033[m')
    print('DINHEIRO    DEBITO    CREDITO')
    print('  [1]        [2]        [3]')
    pagamento = int(input('Opçao: '))
    while pagamento <= 3 and pagamento > 0:
        if pagamento > 3:
            print('Opçao digitada invalida! ')
        if pagamento == 2:
            print('   \033[1;30;45m==== DEBITO ====\033[m')
            sleep(1)
            senha = str(input('Pode digitar a senha...')).strip()
            print('    ...\033[1;30;43mPROCESSADO\033[m...')
            sleep(3)
            print('\033[1;30;42m=====COMPRA APROVADA=====\033[m')
            print('\033[1;30;45mMUITO OBRIGADO! ATÉ MAIS!\033[m')
            break
        elif pagamento == 3:
            print('   \033[1;30;45m==== CREDITO ====\033[m')
            sleep(1)
            senha = str(input('Pode digitar a senha...')).strip()
            print('    ...\033[1;30;43mPROCESSADO\033[m...')
            sleep(3)
            print('\033[1;30;42m=====COMPRA APROVADA=====\033[m')
            print('\033[1;30;45mMUITO OBRIGADO! ATÉ MAIS!\033[m')
            break
        else:
            print('   \033[1;30;45m==== DINHEIRO ====\033[m')
            dinheiro = float(input('\033[1;30;43mDIGITE UM VALOR ACIMA DO "TOTAL":\033[m R$ '))
            print('Seu troco é \033[1;30;45mR${:.2f}\033[m'.format(dinheiro - int(tamanho[n1])))
            print('\033[1;30;45mMUITO OBRIGADO! ATÉ MAIS!\033[m')
            break
