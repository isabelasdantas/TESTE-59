import time
n1 = int(input('Escolha um número: '))
n2 = int(input('Escolha outro número: '))
opção = 0
while opção != 5:
    print('''    [ 1 ] Somar.
    [ 2 ] Multiplicar.
    [ 3 ] Maior.
    [ 4 ] Novos números.
    [ 5 ] Fechar o programa.''')
    opção = int(input('Qual é a sua escolha? '))
    if opção == 1:
        soma = n1 + n2
        print('A soma entre os números é {}.'.format(soma))
    elif opção == 2:
        soma = n1 * n2
        print('A multiplicação entre os números é {}.'.format(soma))
    elif opção == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print('Entre {} e {} o maior número é {}.'.format(n1, n2, maior))
    elif opção == 4:
        print('Informe os números novamente!')
        n1 = int(input('Escolha um número: '))
        n2 = int(input('Escolha outro número: '))
    elif opção == 5:
        time.sleep(0.9)
        print('Finalizando...')
        time.sleep(1.5)
    else:
        print('Número inválido. Tente novamente.')
    print('=-=' * 10)
print('Fim do programa. Volte sempre!')
