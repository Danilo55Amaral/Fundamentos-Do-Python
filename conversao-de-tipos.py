# Conversão de tipos

# Convertendo os tipos das variáveis
# Em alguns casos temos que converter o tipo de uma variável para que 
# possamos manipular essa variável de forma diferente. Um bom exemplo 
# são variáveis do tipo string que armazenam números e é necessário fazer
# alguma operação matemática com esse valor.

# Convertendo de inteiro para float 

# No exemplo eu converto um inteiro para float eu declarei a variável preco 
# com o valor 10 e para fazer a conversão basta passar a variável preco para o 
# construtor float ===> preco = float(preco)

preco = 10 
print(preco)

preco = float(preco)
print(preco)

# Outra forma de fazer essa conversão é utilizando o operador de divisão
preco = 10 / 2 
print(preco)

# Float para inteiro
preco = 10.30
print(preco)

preco = int(preco)
print(preco)

# Também é possivel fazer utilizando operador de / 
preco = 10 
print(preco) 

print(preco / 2)
print(preco // 2)

# Número para string 
# É importante na hora de fazer uma formatação e exibir uma mensagem para o usuário por ex 
# e é necessário juntar uma mensagem com a variável e para fazer isso é necessário concatenar strings
# é necessário ter uma outra string, não tem como colocar um number ali.

preco = 10.50
idade= 28 

print(str(preco))
print(str(idade))

# Outra forma de fazer isso é concatenar uma string com variáveis, para fazer a concatenação 
# basta colocar as variáveis entre {} e iniciar a string após o f 
texto = f"idade {idade} preco {preco}"
print(texto)

# String para número 

preco = "10.50"
idade = "28"

print(float(preco))
print(int(idade))

# Erro de Conversão
# quando uma conversão não for possivel o interpretador vai tentar converter 
# porém se não for possivel ele retorna um erro.
preco = "python"
print(float(preco))

# Outros exemplos 

print(int(1.934333435))
print(int("15"))
print(float("15.15"))
print(float(100))
print(100 / 2)
print(100 // 2)

# Convertendo e checando o tipo 
print(type(str(10.10)))

valor = 15
valor_str = str(valor)
print(type(valor))
print(type(valor_str))