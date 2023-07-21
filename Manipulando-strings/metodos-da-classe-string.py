# Métodos úteis da classe string 

# String e fatiamento. 

# Conhecendo métodos úteis da classe String. 

# A Classe String do Python é famosa por ser rica em métodos e possuir 
# uma interface muito fácil de trabalhar.
# Em algumas linguagens manipular sequências de caracteres não é um 
# trabalho trivial, porém, em Python esse trabalho é muito simples.

# Maiúscula, minúscula e título.
curso = "pYtHon"

print(curso.upper()) # converte para maiúsculo. 
print(curso.lower()) # Converte para minúsculo. 
print(curso.title()) # Converte para minúsculo exceto o primeiro caractere.

# Eliminando espaços em branco / cortando os espaços em branco na String.
curso = "     Python " 

print(curso.strip()) # Remove os espaços em branco da esquerda e da direita.
print(curso.lstrip()) # Remove apenas o espaço da esquerda.
print(curso.rstrip()) # Remove apenas o espaço da direita.

# Junções e centralização.
curso = "Python"

# O método center possue dois argumentos, o número de caracteres que ele irá 
# ocupar(ele conta quantos caracteres a string possue e adiciona o restante de acordo do que foi passado),
# o segundo argumento é opcional e ele é o caractere que se quer colocar nesses espaços, se caso 
# não for informado nenhum caractere será preenchido o espaço em branco.
print(curso.center(10, "#"))

# A junção é feita utilizando o join, no primeiro argumento é o que queremos juntar na string 
# em seguida passa o método join com a string. Ele passa em cada elemento da string e adiciona 
# o elemento que foi passado no primeiro argumento.
print(".".join(curso))

# Mais exemplos 
nome = "dAnIlO"

print(nome.upper())
print(nome.lower())
print(nome.title())

texto = " olá mundo!    "

print(texto)
print(texto.strip() + ".")
print(texto.rstrip() + ".")
print(texto.lstrip() + ".")

menu = "Python"

print("###" + menu + "###")
print(menu.center(14))
print(menu.center(14, "#"))
print("P-y-t-h-o-n")
print("-".join(menu))