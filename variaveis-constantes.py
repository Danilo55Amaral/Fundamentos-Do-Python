# Variáveis e Constantes 

# Variáveis 

# São valores definidos que podem sofrer alterações no decorrer da execução do 
# programa, variáveis são criadas com um valor e esse valor pode mudar durante 
# a execução do programa. Veja o exemplo abaixo:

# eu definir uma variável para minha idade chamada age e outra para meu nome
# chamada name em seguida eu exibir uma mensagem chamando os valores dessas duas
# variáveis.

age = 23
name = 'Danilo'
print(f'Meu nome e {name} e eu tenho {age} anos(s) de idade.')

# No Python eu posso declarar várias variáveis de uma única vez em apenas uma linha
# Note que aqui atribuir novos valores a essas variáveis e os valores mudaram.

age, name = (23, 'Mychele')
print(f'Meu nome e {name} e eu tenho {age} ano(s) de idade.')

# Vale Ressaltar que o Python define automaticamente o tipo de dados da variável por isso 
# náo é necessário definir os tipos. Quando definimos uma variável o Python vai ver qual 
# o tipo de valor está sendo atribuido e vai definir que aquela variável é daquele tipo. 

# Constantes

# Também armazenam valores, porém diferente das variáveis esses valores não podem 
# mudar durante a execução do programa, O valor é imutável.

# PYTHON NÃO TEM CONSTANTES com palavras reservadas.

# Não existe uma palavra reservada para uma constante diferentemente do 
# JavaScript que utilizamos const.
# Em Python existe a convenção que diz ao programador que a variável é uma constante
# Para fazer isso basta criar uma variável com o nome todo em letras maíusculas. Veja alguns exemplos:

ABS_PATH = '/home/danilo/Documents/fundamentos-python'
DEBUG = True 
STATES = [
    'SP',
    'RJ',
    'MG',
]
AMOUNT = 30.5

# Boas práticas 

# 1 - O padrão de nomes deve ser snake case.
# 2 - Escolher nomes sugestivos.
# 3 - Nomes de constantes todo em maiúsculo.

# Exemplificando no código

age, name = (23, 'Mychele')
print(f'Meu nome e {name} e eu tenho {age} ano(s) de idade.')

nome = "Bill Gates"
idade = 28
print(nome, idade)

# Mudando o nome
nome = "Danilo"
print(nome)

# snack Case 
limite_saque_diario = 1000 
print(limite_saque_diario)

# Constante
BRAZILIAN_STATES = ["PE", "CE", "SP","RJ"]
print(BRAZILIAN_STATES)

# Note que para o interpretador Python o valor muda por que a definição de Constante é 
# apenas uma convenção para os desenvolvedores.
BRAZILIAN_STATES = 10 
print(BRAZILIAN_STATES)