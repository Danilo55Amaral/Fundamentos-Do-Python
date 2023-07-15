# Operadores aritméticos

# Conhecendo os operadores aritméticos
# Esses operadores executam operações matemáticas utilizando operandos
## Veja o exemplo de Adição, subtração e multiplicação
# Adição
print(1 + 1)
# subtração
print(10 -5) 
# Multiplicação 
print(4 * 3)
# Divisão
print(12 / 3)
# Divisão inteira
print(12 // 2)
# Módulo 
print(10 % 3)
# Exponenciação
print(2 ** 3)


# Precedência de operadores

# Na matemática existe a regra que indica quais operações vão ser
# executadas primeiro. Isso é útil pois ao analisar uma expressão, 
# dependendo da ordem das operações os valores podem serem diferentes.
# x = 10 - 5 * 2 
# x é igual a 10 ou 0 ?

# Na programação não é diferente ela também segue essa ordem de precedência 
# Temos a seguinte ordem: 
# Parênteses 
# Expoêntes 
# Multiplicações e divisões (da esquerda para a direita)
# Somas e subtrações (da esquerda para a direita)

# Alguns exemplos 
print(10 - 5 * 2) 
print((10 - 5) * 2)
print(10 ** 2 * 2) 
print(10 ** (2 * 2))
print(10 / 2 * 4)

produto_1 = 10
produto_2 = 20
produto_3 = 20
produto_4 = 10

print(produto_1 + produto_2)
print(produto_1 + produto_2 + 3.5) # o Pyton analisa a expressão e identifica a precedencia dos operadores.
print(produto_3 / produto_4)
print(produto_3 // produto_4)
print(produto_3 * produto_4)
print(produto_3 % produto_4)
print(produto_3 ** produto_4)

variavel_x = (10 + 5) * 4 
variavel_y = (10 / 2) + (25 * 2) - (2 ** 2)
print(variavel_x)
print(variavel_y)