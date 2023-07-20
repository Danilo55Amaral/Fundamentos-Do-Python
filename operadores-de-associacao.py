# Operadores de associação 

# São utilizados para verificar se um objeto está 
# presente em uma sequência. 

# Exemplo 
curso = "Curso de Python"
frutas = [ "laranja", "uva", "limão"]
saques = [1500, 100] 

"Python" in curso 
"maça" not in frutas 
200 in saques 

# Mais exemplos 
frutas = ["limao", "uva", "laranja"]
curso = "curso de Python"

print("laranja" not in frutas)
print("limao" in frutas)
print("Python" in curso)
print("python" in curso)
