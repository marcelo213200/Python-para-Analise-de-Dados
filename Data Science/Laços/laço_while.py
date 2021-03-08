'''x = 256
total = 0
while x > 0:
    if total > 500:
        break
    total += x
    x=x//2
    print('x = ',x)
    print('total = ', total)'''

# pass -> usada em blocos em que nenhuma ação deva ser executada

x = int(input('Informe x: '))
if x < 0:
    print('negative!')
elif x == 0:
    # TODO: insira algo inteligente aqui
    pass
else:
    print('positive!')