# Como regra geral, se você prevê que precisará repetir o mesmo código muito semelhante mais de uma vez, talvez valha a pena escrever uma função reutilizável. As funções também podem ajudar você a deixar o seu código mais legível ao dar um nome a um grupo de instruções Python.
# As funções são declaradas com a palavra def, e o retorno é feito com a palavra reservada return:

def my_function(x, y, z = 1.5):      # x e y são argumentos posicionais (positional arguments), enquanto z é um argumento nomeado (keyword arguments)
    if z > 1:                        # argumentos nomeados devem vir depois dos argumentos posicionais (se houver), se não ocorre SyntaxError: non-default argument follows default argument.
        return z * (x + y)
    else:
        return z / (x + y)
    
print(my_function(3,5,2))            # Ou print(my_function(x = 3, y = 5, z = 2)) -> a ordem naõ importa desde que seja especificado




