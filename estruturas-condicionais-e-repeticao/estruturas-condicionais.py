# Estruturas Condicionais 

# A estrutura condicional permite o desvio de fluxo de controle,
# quando determinadas expressões lógicas são atendidas.
# Se for necessário tomar uma ação dependendo de alguma condição 
# será necessário utilizar estruturas condicionais para que a ação seja realizada.

# if 
# Para criar uma estrutura condicional simples, composta por um único desvio,
# podemos utilizar a palavra reservada if. O comando irá testar a expressão 
# lógica, e em caso de retorno verdadeiro as ações presentes no bloco de código do 
# if serão executadas.

# Exemplo
saldo = 2000.0
saque = float(input("Informe o valor do saque: "))

if saldo >= saque:
    print("Realizando saque!") 

if saldo < saque:
    print("Saldo insuficiente!")

# if/else
# Para criar uma estrutura condicional com dois desvios, podemos utilizar as 
# palavras reservadas if e else. Como sabemos se a expressão lógica testada no
# if for verdadeira, então o bloco de código do if será executado. Caso contrário
# o bloco de código do else será executado.

# Exemplo 
saldo = 2000.0
saque = float(input("Informe o valor do saque: "))

if saldo >= saque:
    print("Realizando saque!")
else:
    print("Saldo insuficiente!")

# if/elif/else 
# Em alguns cenários queremos mais de dois desvios, para isso podemos utilizar 
# a palavra reservada elif. O elif é composto por uma nova expressão lógica, que 
# será testada e caso retorne verdadeiro o bloco de código do elif será executado.
# Não existe um número máximo de elifs que podemos utilizar, porém evite criar 
# grandes estruturas condicionais, pois elas aumentam a complexidade do código.

# Exemplo 
opcao = int(input("Informe uma opção: [1] Sacar /n[2] Extrato: "))

if opcao == 1:
    valor = float(input("Informe a quantia para o saque: "))

elif opcao == 2:
    print("Exibindo o extrado ... ")
else:
    sys.exit("Opção inválida")

# Mais exemplos 
MAIOR_IDADE = 18
IDADE_ESPECIAL = 12

idade = int(input("Informe sua idade: "))

if idade >= MAIOR_IDADE:
    print("Maior de idade, pode tirar a CNH.")

if idade < MAIOR_IDADE:
    print("Ainda não pode tirar a CNH.")

# Com else

if idade >= MAIOR_IDADE:
    print("Maior de idade, pode tirar a CNH.")

else:
    print("Ainda não pode tirar a CNH.")
    
# com elif 
if idade >= MAIOR_IDADE:
    print("Maior de idade, pode tirar a CNH.")
elif idade == IDADE_ESPECIAL:
    print("Pode fazer aulas teóricas, mas não pode fazer aulas práticas.")
else:
    print("Ainda não pode tirar a CNH.")


# if aninhado 
# Podemos criar estruturas condicionais aninhadas, para isso basta adicionar 
# estruturas if/elif/else dentro do bloco de código de estruturas if/elif/else.

# Exemplo 
saldo = 20000
saque = 5000

conta_normal = False
cheque_especial = 500
conta_universitaria = True

if conta_normal:

    if saldo >= saque:
        print("Saque realizado com sucesso!")
    elif saque <= (saldo + cheque_especial):
        print("Saque realizado com uso do cheque especial!")
    else:
        print("Não foi possivel realizar o saque, saldo insuficiente!")

elif conta_universitaria:

    if saldo >= saque:
        print("Saque realizado com sucesso!")
    else:
        print("Saldo insuficiente!")

else:
    print("O Sistema não reconheceu seu tipo de conta, entre em contato com o seu gerente.")


# if ternário 
# O if ternário permite escrever uma condição em uma única linha. Ele é composto por três partes,
# a primeira parte é o retorno caso a expressão retorne verdadeiro, a segunda parte é a expressão 
# lógica e a terceira parte é o retorno caso a expressão não seja atendida.

# Exemplo  
saldo = 3000
saque = 1000 

status = "Sucesso" if saldo >= saque else "Falha"

print(f"{status} ao realizar o saque!")