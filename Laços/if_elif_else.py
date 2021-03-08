print('Informe o valor de x: ')

x = int(input())

if x < 0:
    print("It's negative")

elif x == 0:
    print('Equal to zero')

elif 0 < x < 5: 
    print('Positive but smaller than 5')

else:
    print('Positive and larger than or equal to 5')
