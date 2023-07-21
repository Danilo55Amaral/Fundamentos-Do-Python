# Indentação e Blocos 

# Sobre Indentação 
# Identar o código mantém o código fonte mais legível e manutenível.
# Porém no Python a identação possue mais um outro papel, utilizando a 
# indentação o interpretador consegue determinar onde um bloco se inicia 
# e onde ele termina.  

# Bloco de comando 
# As linguagens de programção costumam utilizar caracteres ou palavras reservadas
# para determinar o início e o fim do bloco. Em Java e C por exemplo, utilizamos chaves.

# Bloco em Java 
# void sacar(double valor) { // início do bloco do método
#     if (this.saldo >= valor) { // início do bloco do if
#         this.saldo -= valor;
#     } // fim do bloco do if  
# } // fim do bloco do método 

# No Python 
# Existe uma convenção em Python, que define as boas práticas 
# para a escrita de código na linguagem. Nesse documento é indicado 
# utilizar 4 espaços em branco por nível de indentação, ou seja, a cada
# novo bloco adicionamos 4 novos espaços em branco.
# PS- o Python utiliza : para iniciar o bloco porém o Python não tem um caractere 
# ou simbolo para delimitar o final do bloco e para isso utilizamos a própria indentação.
# Por isso que no Python é obrigatório a indentação.

# Exemplo de Bloco em Python 
def sacar(self, valor: float) -> None: # início do bloco do método  
    if self.saldo >= valor:    # início do bloco if 
        self.saldo -= valor
    # fim do bloco if 
# fim do bloco do método

# Alguns exemplos

def sacar(valor):
    saldo = 500

    if saldo >= valor:
        print("valor sacado!")  # está dentro do bloco if
        print("retire o seu dinheiro na boca do caixa.") # está dentro do bloco if
    
    print("Obrigado por ser nosso cliente, tenha um bom dia!") # está dentro do método e fora do if 


def depositar(valor):
    saldo = 500 
    saldo += valor 

    
sacar(100)