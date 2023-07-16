# Funções de entrada e saída

# Lendo valores com a função input 

# Função input
# A função builtin input é utilizada quando queremos ler dados da entrada padrão(teclado)
# Essa função recebe um argumento do tipo string, que é exibido para o usuário na saída
# padrão (tela). A função lê a entrada, converte para string e retorna o valor. Essa função 
# é uma função nativa do Python e por isso não é necessária a instalação de nenhum pacote.
# Veja um Exemplo 

# Essa função exibe a mensagem ao usuário, aguarda uma entrada do usuário, quando o usuário 
# informa essa entrada a função input recupera esse valor que foi digitado convertendo para 
# string e atribui esse valor para uma variável, que no caso do exemplo definimos como nome.
nome = input("Informe o seu nome: ")

# Exibindo valores com a função print 
# A função builtin print é utilizada quando queremos exibir dados na saída padrão (tela).
# Ela recebe um argumento obrigatório do tipo varargs de objetos e 4 argumentos opcionais
# (sep, end, file e flush). Todos os objetos são convertidos para string, separados por sep
# e terminados por end. A string final é exibida para o usuário.
# Veja um Exemplo
nome = "Danilo"
sobrenome = "Amaral"

print(nome, sobrenome)
print(nome, sobrenome, end="...\n")
print(nome, sobrenome, sep="#")

# Exemplos no código 

nome = input("Informe o seu nome: ")
idade = input("Informe a sua idade: ")

print(nome,idade)
print(nome,idade, end="...\n")
print(nome,idade, sep="#", end="...\n")
print(nome,idade, sep="#")

# OBS: Ao executar esse código utilizando a função input é necessário ao invés de ctrl + N 
# ir e executar selecionando Run Python File