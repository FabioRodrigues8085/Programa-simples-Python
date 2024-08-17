valorpedido = 0

#Cabeçalho
print('Bem-vindo a Loja de Gelados do Fabio Braz Rodrigues!!!')

#Tabela de preços e tamanhos
print('-'*23, 'Cardápio','-'*23)
print('------|',' Tamanho ','|',' Cupuaçu (CP) ','|',' Açaí (AC) ','|------')
print('------|','    P    ','|','   R$  9,00   ','|','  R$ 11,00 ','|------')
print('------|','    M    ','|','   R$ 14,00   ','|','  R$ 16,00 ','|------')
print('------|','    G    ','|','   R$ 18,00   ','|','  R$ 20,00 ','|------')
print('-'*56)

#entradas de pedido do usuário
while True:
    sabor = (input('Entre com o sabor desejado (CP/AC): '))
    while (sabor.upper() != 'CP' and sabor.upper() != 'AC'):
        print('Sabor inválido. Tente novamente.')
        sabor = input('Entre com o sabor desejado (CP/AC): ')

    tamanho = (input('Entre com o tamanho desejado (P/M/G): '))
    while (tamanho.upper() != 'P' and tamanho.upper() != 'M' and tamanho.upper() != 'G'):
        print('Tamanho inválido. Tente novamente.')
        sabor = input('Entre com o sabor desejado (CP/AC): ')
        tamanho = input('Entre com o tamanho desejado (P/M/G): ')

    #verificações
    if tamanho.upper() == 'P' and sabor.upper() == 'CP':
        valor = 9
        valorpedido = valorpedido + valor
        print('Você pediu CUPUAÇU no tamanho P: R$ 9,00')

    elif tamanho.upper() == 'P' and sabor.upper() == 'AC':
        valor = 11
        valorpedido = valorpedido + valor
        print('Você pediu AÇAÍ no tamanho P: R$ 11,00')

    elif tamanho.upper() == 'M' and sabor.upper() == 'CP':
        valor = 14
        valorpedido = valorpedido + valor
        print('Você pediu CUPUAÇU no tamanho M: R$ 14,00')

    elif tamanho.upper() == 'M' and sabor.upper() == 'AC':
        valor = 16
        valorpedido = valorpedido + valor
        print('Você pediu AÇAÍ no tamanho M: R$ 16,00')

    elif tamanho.upper() == 'G' and sabor.upper() == 'CP':
        valor = 18
        valorpedido = valorpedido + valor
        print('Você pediu CUPUAÇU no tamanho G: R$ 18,00')

    elif tamanho.upper() == 'G' and sabor.upper() == 'AC':
        valor = 20
        valorpedido = valorpedido + valor
        print('Você pediu AÇAÍ no tamanho G: R$ 20,00')

    #confirmação de pedido do usuário
    maispedidos = input('Deseja pedir mais alguma coisa? Tecle (S) para sim ou digite outra tecla para continuar: ')
    if (maispedidos.upper() == 'S'):
        continue
    else:
        break

#valor total do pedido
print('Valor total a ser pago: R$ {:.2f}'.format(valorpedido))