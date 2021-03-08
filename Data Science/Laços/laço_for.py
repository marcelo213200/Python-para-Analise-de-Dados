# Servem para iterar(visualizar item a item) por uma coleção ( como uma lista ou uma tupla)


#soma inteiros em uma lista e ignora valores None
'''sequence = [1, 2, None, 4, None, 5]
total = 0
for value in sequence:
    if value is None:
        continue
    total += value'''


#soma elementos da lista até que um 5 seja alcançado
'''sequence = [1,2,0,4,6,5,2,1]
total5 = 0
for value in sequence:
    if value == 5:
        print('STOP',value)
        break
    else:
        total5 += value
        print(total5)'''
    

'''Função range() - range(inicio(opcional), fim, salto(opcional))
Exemplos:   range(11) - valores de 0 a 10
            range(5,11) - valores de 5 a 10
            range(2,50,2) - valores de 2 a 50 saltando de 2 em 2'''


'''for i in range(4):
    for j in range(4):
        if j > i:
            break
        print((i,j))'''

#list(range(11))
#list(range(0,20,2))


'''seq = [1,2,3,4]
for i in range(len(seq)):
    val = seq[i]'''

'''sum = 0
for i in range(100000):
    if i % 3 == 0 or i % 5 == 0
        sum += i'''
    
    
list(range(5,0,-1))