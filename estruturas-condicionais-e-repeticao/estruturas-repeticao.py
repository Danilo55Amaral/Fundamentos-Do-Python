# Estruturas de Repetição 

# São estruturas utilizadas para repetir um trecho de código um 
# determinado número de vezes. Esse número pode ser conhecido 
# previamente ou determinado através de uma expressão lógica.

# Exemplo sem repetição 
a = int(input("Informe um número inteiro: "))
print(a) 

a += 1 
print(a) 

a += 1 
print(a)

a += 1 
print(a) 

a += 1 
print(a)

# Note que existe muita repetição de código. em códigos com milhares de linhas fica complicado.

# for 
# O comando for é usado para percorrer um objeto iterável. Faz sentido usar 
# for quando sabemos o número exato de vezes que nosso bloco de código deve 
# ser executado, ou quando queremos percorrer um objeto iterável.

# Exemplo  
texto = input("Informe um texto: ")
VOGAIS = "AEIOU" 

for letra in texto:
    if letra.upper() in VOGAIS:
        print(letra, end="")

print()

# O código a cima percorrre o texto que o usuário informou, uma string em python 
# é um objeto iteravel, cada posição dentro da string pode ser percorrida pelo 
# laço for, o for possue duas partes, a primeira parte é qual objeto iterável será 
# percorrido, a segunda parte representa o item que está sendo iterado no momento.
# nessa primeira parte do for eu utilizei letra porém podemos nomear com qualquer nome.
# o upper é um método que utilizei nesse exemplo para transformar as letras para maiúsculo.
# Em seguida eu utilizei o in para verficar se está entre a Variavel VOGAIS, ou seja se a letra
# está dentro da sequência de vogais.

# Esse código a cima pega um texto e separa as vogais desse texto.

# O for também pode ser usado com else ==> for/else ele vai executar ao final do laço.
# Exemplo 
texto = input("Informe um texto: ")
VOGAIS = "AEIOU" 

for letra in texto:
    if letra.upper() in VOGAIS:
        print(letra, end="")
else:
    print() # esse print adiciona uma quebra de linha 
    print("Executa no final do laço")

# Função range 
# Range é uma função built-in do Python, ela é usada para produzir uma sequência de números 
# inteiros a partir de um ínicio (inclusivo) para um fim (exclusivo). Se usarmos range(i,j)
# será produzido:
# i, i+1, i+2, i+3, ..., j-1. 
# Ela recebe 3 argumentos: stop (obrigatório), start (opcional) e step opcional.

# Exemplo range
# range(stop) -> range object 
# range(start, stop[, step]) -> range object
list(range(4))
# resultado ==> [0, 1, 2, 3, 3] note que ele percorre todos os elementos da minha lista.

# Utilizando o range com for.
for numero in range(0, 11):
    print(numero, end=" ")
    print() # quebrando uma linha

# Note que o resultado a cima vai parar em 10 por que o ultimo elemento que informamos o 11 sempre
# será exclusivo, por isso sempre vai ser o ultimo elemento menos 1.

# outro exemplo 
# Observe que nos argumentos do range tesmo o start que é o 5 é onde inicia, em seguida o final 
# que é o 51, e por ultimo o step que é de quanto em quanto vai ser no exemplo aqui foi o 5 ou seja
# de 5 em 5 ele vai percorrendo. PS- o end está sendo usado apenas para a contagem ser exibida um ao 
# lado do outro, se utilizarmos print(numero) será exibido um abaixo do outro.
for numero in range(0, 51, 5):
    print(numero, end=" ") 

# while 
# O comando while é usado para repetir um bloco de código várias vezes. Faz sentido usar while 
# quando não sabemos o número exato de vezes que o nosso bloco de código deve ser executado.

# Note que o while é muito semelhante ao if ele tem uma condição e atende essa condição 
# a diferença entre eles é que o if testa e executa uma única vez, o while ele vai executar 
# toda vez que a condição for atendida.

# Exemplo
opcao = -1 
while opcao !=0:
    opcao = int(input("[1] Sacar \n[2] Estrado \n[0] Sair \n: "))

    if opcao == 1:
        print("Sacando ... ")
    elif opcao == 2:
        print("Exibindo o extrato ... ")


# while/else 
# Assim como o for também pode ser utilizado o else.

opcao = -1 
while opcao !=0:
    opcao = int(input("[1] Sacar \n[2] Estrado \n[0] Sair \n: "))

    if opcao == 1:
        print("Sacando ... ")
    elif opcao == 2:
        print("Exibindo o extrato ... ")
else:
    print("Obrigado por usar nosso sistema bancário, até logo!")


# Break 
# O Break serve para cortar o laço de repetição.

# Nesse exemplo eu criei um programa que pede um número para o usuário 
# se esse número for par o código continuará sendo executado, se o número 
# for impar a execução será cortada. Eu também nesse exemplo crio um loping 
# infinito que vai continuar executando enquando a condição for verdadeira.
# Nesse exemplo temos uma estrutura que se repete para sempre até que determinada 
# condição seja atendida que no caso é o número sendo igual a 10.
# Aqui temos um laço infinito com uma condição de parada.
while True: 
    numero = int(input("Informe um número: "))

    if numero == 10:
        break 

    print(numero)

# Utilizando o for
for numero in range(100):

    if numero == 10:
        break 

    print(numero)

# Também podemos utilizar o continue quando for necesário desviar de alguma 
# situação especifica dentro do laço. Nesse caso abaixo ele vai exibir todos os 
# números menos o 12.
for numero in range(100):

    if numero == 10:
        continue

    print(numero, end=" ")

# Exibindo apenas números ímpares
for numero in range(100):

    if numero % 2 == 0:
        continue

    print(numero, end=" ")