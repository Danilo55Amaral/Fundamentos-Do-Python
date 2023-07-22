# Interpolação de variáveis. 

# Em Python temos 3 formas de interpolar variáveis em strings, a primeira
# é utilizando o sinal %, a segunda é utilizando o método format e a última
# é utilizando f strings.
# A primeira forma não é atualmente recomendada e seu uso em Python 3 é raro,
# por esse motivo iremos focar nas 2 últimas.

# Exemplos
# Old style %
# %s ==> Valores do tipo String
# %d ==> Valores inteiros 
# %f ==> Valores de ponto flutuante
# As variáveis precisam ser passadas em ordem após o % ==>  % (nome, idade, profissao, linguagem)
nome = "Danilo"
idade = 27
profissao = "Progamador"
linguagem = "Python"

print("Olá, me chamo %s. Eu tenho %d anos de idade, trabalho como %s e estou matriculado no curso de %s." % (nome, idade, profissao, linguagem))

# Métdodo format 
# Esse método possue várias formas de se formatar strings uma delas é colocar {} onde será colocada a variável 
# e funciona semelhante ao método anterior, porém ao final da string é utilizado .format passando as variáveis.
# Outra forma também é colocar entre as {} qual a posição das variáveis que vão ser colocadas dentro da string.

print("Olá, me chamo {}. Eu tenho {} anos de idade, trabalho como {} e estou matriculado no curso de {}.".format(nome, idade, profissao, linguagem))
print("Olá, me chamo {3}. Eu tenho {2} anos de idade, trabalho como {1} e estou matriculado no curso de {0}.".format(linguagem, profissao, idade, nome))
# Também podemos fazer passando o nome da variável 
print("Olá, me chamo {nome}. Eu tenho {idade} anos de idade, trabalho como {profissao} e estou matriculado no curso de {linguagem}.".format(nome=nome, idade=idade, profissao=profissao, linguagem=linguagem))
# Também podemos resumir a passagem de variáveis criando um dicionário de dados no Python, dentro do dicionário pessoa contém todas essas variáveis declaradas.

# print("Olá, me chamo {nome}. Eu tenho {idade} anos de idade, trabalho como {profissao} e estou matriculado no curso de {linguagem}.".format(**pessoa))

# Método f-string 
# Uma maneira mais resumida e limpa é utilizando o f-string 
print(f"Olá, me chamo {nome}. Eu tenho {idade} anos de idade, trabalho como {profissao} e estou matriculado no curso de {linguagem}.")

# Formatando strings com f-strings 
# Quando temos um valor grande e queremos exibir apenas duas casas por exemplo 
# Para fazer essa formatação com f-strings utilzamos : em seguida . passando o 
# numero de casas que queremos exibir após a virgula, seguido de f para simbolizar float.
# O outro exemplo é o mesmo porém foi passado uma quantidade de espaços que no exemplo foi 10.

PI = 3.14159

print(f"Valor de PI: {PI: .2f}")
print(f"Valor de PI: {PI: 10.2f}")


# Mais alguns exemplos 

saldo = 52.562

# Dicionário 
dados = {"nome": "Danilo", "idade": 27}

print("Nome: %s Idade: %d" % (nome, idade))
print("Nome: {} Idade: {}".format(nome, idade))
print("Nome: {1} Idade: {0}".format(idade, nome))
print("Nome: {1} Idade: {0} Nome: {1} {1}".format(idade, nome))
print("Nome: {nome} Idade: {idade}".format(nome=nome, idade=idade))
print("Nome: {name} Idade: {age}".format(age=idade, name=nome))
print("Nome: {nome} Idade: {idade}".format(**dados))
print(f"Nome: {nome} Idade: {idade}")
print(f"Nome: {nome} Idade: {idade} Saldo: {saldo}")
print(f"Nome: {nome} Idade: {idade} Saldo: {saldo:10.2f}")
print(f"Nome: {nome} Idade: {idade} Saldo: {saldo:.2f}")