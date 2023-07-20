# Operadores de identidade 

# Esses operadores comparam se os dois objetos testados 
# ocupam a mesma posição na memória.

# O operador de identidade (is) e o contrário (is not)

# Exemplo
curso = "Curso de Python"
nome_curso = curso 
saldo, limite = 200, 200 

curso is nome_curso 
curso is not nome_curso
saldo is limite

# Mais alguns exemplos 
saldo = 1000 
limite = 500 

# Testanto de saldo e limite ocupam a mesma região na memória.
print(saldo is limite)
# Testando se saldo e limite não ocupam o mesmo espaço na memória.
print(saldo is not limite)