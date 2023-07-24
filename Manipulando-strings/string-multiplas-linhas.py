# String multiplas linhas.

# Strings de múltiplas linhas são definidas informando 3 aspas simples 
# ou duplas durante a atribuição. Elas podem ocupar várias linhas de código,
# e todos os espaços em branco são incluídos na string final.

# Exemplo Strings Triplas.
nome = "Danilo"

mensagem = f""" 
Olá meu nome é {nome},
Eu estou aprendendo Python 
"""

print(mensagem) 

print("""
    ================= MENU ================
      
    1 - Depositar 
    2 - Sacar 
    0 - Sair 
    
    =========================================
      
            Obrigado por usar nosso sistema!!!!
""")