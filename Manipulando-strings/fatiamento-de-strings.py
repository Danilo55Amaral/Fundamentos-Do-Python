# Fatiamento de Strings.

# Fatiamento de strings é uma técnica utilizada para retornar substrings 
# partes da string original, informando inicio (start), fim (stop) e 
# intervalo (step):[start: stop[, step]].

# Exemplo
# Para acessar a string utilizamos o índice, 

nome = "Danilo Gabriel Amaral Ferreira"

nome[0]
# Se antes do : eu não passar nada ele irá iniciar do índice 0, após o : é o índice de onde ele termina.
nome[:9]
# Passando o ínicio e não passando o fim, ele vai pegar a partir do índice que estou informando e vai até o ultimo índice.
nome[10:]
# Pegando um pedaço da string(substring) ==> informamos o início e o fim.
nome[10:16]
# Também podemos passar o step ao final, que no caso aqui ele vai pegar de 2 em 2 entre esse início e final que passei.
nome[10:16:2]
# Retorna uma cópia da string completa.
nome[:]
# Espelhando uma string, passa sem ínicio e sem final, e step -1, ele faz o espalhamento da strind e exibe uma cópia invertida. 
nome[ ::-1]

# Maisn alguns exemplos.
nome = "Danilo Gabriel Amaral Ferreira"

print(nome[0])
print(nome[-1])
print(nome[:9])
print(nome[10:])
print(nome[10:16])
print(nome[10:16:2])
print(nome[:])
print(nome[ ::-1])