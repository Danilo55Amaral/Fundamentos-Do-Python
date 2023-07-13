# Tipos de dados no Python 

# Os tipos conseguem organizar quais operações podem ser feitas 
# com os dados ou valores informados,os dados podem ser de vários 
# tipos e isso define o que pode ser feito com esses dados, podemos 
# ter números, valores lógicos, inteiros, valores com casas decimais,
# não apenas números mas também os dados podem serem cadeias de caracteres.

# Os Tipos conseguem organizar esses dados nesses tipos e baseado
# nisso conseguimos saber qual tipo de operação pode ser feita. 

# Alguns dos tipos mais comuns na linguagem. 

# Texto ===> str (String) 
# Númerico ===> int, float, complex (Números)
# Sequência ===> list, tuple, range (Números ou Letras) 
# Mapa ===> dict (Chave e Valor) 
# Coleção ===> set, frozenset (Semelhante a lista porém sem repetições de elementos)
# Booleano ==+> bool (true e false)
# Binário ===> bytes, bytearray, memoryview (Binários)

# Números inteiros (int) 
# São definidos pela palavra reservada int e tem precisão ilimitada veja abaixo alguns exemplos. 
1, 10, 100, -1, -10, -100, 990889899 

# Números de ponto flutuante 
# São definidos pela palavra reservada float e representam números racionais veja alguns exemplos.
1.5, -12,876, 0.65, 2233434.009 

# Booleano 
# Assim como em outras linguagens é utilizado para definir verdadeiro(true) e falso(false) esse tipo 
# de dado é definido pela palavra reservada bool, dentro do Python esse tipo é uma subclasse do tipo 
## int isso por que qualquer número diferente de 0 é true e 0 é false.
True, False

# Strings 
# Strings também chamado de cadeia de caracteres definem valores alfanúmericos em Python a palavra 
# reservada para strings é str, veja alguns exemplos de Strings em Python. 
"Danilo", 'Danilo', """Danilo""", '''Danilo''', "D"  

## Alguns exemplos no código 

print(11 + 10)
print(5 + 10)
print(3 + 20 + 2000)

print(1.9 + 2 +  0.5)

print(True)
print(False)

print("Danilo Amaral")
print("""Cientista de Dados""")
print('d') 
print('Danilo')

int()
float()
str()
bool()