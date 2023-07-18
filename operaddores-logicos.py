# Operadores Lógicos 

# São operadores utilizados em conjunto com os operadores de comparação,
# para montar uma expressão lógica. Quando um operador de comparação é 
# utilizado, o resultado retornado é um booleano, dessa forma podemos 
# combinar operadores de comparação com os operadores lógicos, exemplo: 
# op_comparacao + op_logico + op_comparacao... N...

# Exemplo utilizando operador de comparação. 
saldo = 1000 
saque = 200 
limite = 100 

saldo >= saque 
saque <= limite

# Operador E 
# Esse operador tem como base que a primeira parte antes do and seja true
# e a segunda parte que é após o and também precisa ser true, se forem ambos 
# verdadeiros a expressão é true.
saldo >= saque and saque <= limite 

# Operador OU (or)
# Para que uma expressão utilizando or seja true só é necessário que apenas uma 
# condição seja True, isso já é o suficiente para que ele retorne true
# para que ele retorne false é necessário que todas as condições sejam false.
# Note que o operador or é o oposto do and.
saldo >= saque or saque <= limite 

# Operador de Negação 
# sempre vamos pensar também no inverso, por exemplo o inverso de falso 
# é verdadeiro, not pode ser pensado como o inverso.
# Podemos comparar uma expressão, ela vai ter um valor booleano e também 
# é possivel negar os valores dentro de uma sequência.
contatos_emergencia = [] 

not 1000 > 1500 
not contatos_emergencia 
not "saque 1500;"
not ""

# Parênteses 
# Assim como nos aritiméticos os parênteses servem para delimitar a precedência.
saldo = 1000
saque = 250 
limite = 200 
contatos_emergencia = True
conta_especial = True

expressao_1 = saldo >= saque and saque <= limite or contatos_emergencia and saldo >= saque 
print(expressao_1)
# fica mais legível. 
expressao_2 = (saldo >= saque and saque <= limite) or (contatos_emergencia and saldo >= saque)
print(expressao_2)
# Praticando com código. 

# AND ===> Para ser True tudo tem que ser True. 
# OR ===> Para ser True apenas um tem que ser True.
print(True and True)
print(True and False)
print(False and False)
print(True or True) 
print(True or False)
print(False or False)
print(True and True and True)
print(True and False and True)
print(False and False and True) 

conta_normal_com_saldo_suficiente = saldo >= saque and saque <= limite 
conta_especial_com_saldo_suficiente = conta_especial and saldo >= saque

expressao_3 = conta_normal_com_saldo_suficiente or conta_especial_com_saldo_suficiente
print(expressao_3)