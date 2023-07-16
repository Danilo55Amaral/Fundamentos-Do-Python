# Modo Interativo 

# O interpretador Python possue um modo que é possível escrever o código e 
# ver o resultado em tempo real, nesse modo não é necessário utilizar os 
# comandos de exibição por que ele retorna o resultado em tempo real.

# Entrando em modo interativo 

# Existem duas formas uma delas é utilizando a palavra reservada python no 
# terminal, a outra forma é executar o script com a flag -i utilizando 
# a palavra python em seguida -i e depois o nome do arquivo ==> (python -i app.py).
# ambas as formas são executadas via terminal.

# Note que ao entrar no modo interativo podemos testar fazendo operações 
# matemáticas, note que ele retorna os resultados imediatamente. Note que 
# os códigos são executados sem a necessidade de executar o comando print() 
# por exemplo. Em alguns casos isso é muito util.

# Para sair do modo interativo ===> exit() 

# O modo interativo é bem util na hora de trabalhar com algoritimos mais complexos 
# onde temos variáveis que armazenam alguns valores em memoria e através do modo 
# interativo podemos manipular esses valores em tempo real.

# Função dir 

# Sem argumentos ou parametros ela irá retornar uma lista de nomes do escopo local
# atual. Quando existe um argumento irá retornar uma lista de atributos válidos do 
# objeto. 

# Ao executar por exemplo um script e querendo ver o que tem naquele contexto local
# daquele script utilizamos dir() sem argumento. Se caso for passado um argumento para 
# a função dir ela irá retornar atributos válidos para o objeto.
dir()
dir(100)

# Vamos testar a função dir no modo interativo, entramos no modo interativo e executamos a 
# função dir() e note que será retornado o que temos no escopo local do arquivo.
# outro teste que podemos fazer também é checar todos os elementos que temos no objeto 100
# dir(100)

# Função help 

# Essas duas funções se complementam, o help retorna o sistema de ajuda integrado com isso 
# é possível realizar buscas em modo interativo ou informar por parâmetro qual o nome do 
# módulo, função, classe, método ou variável. Exemplo 
help()
help(100)

# Apertando a letra q ele sai da documentação.

# Podemos executar o script pelo modo interativo e consultar dentro dos objetos daquele script
# quais são os métodos e caso exista um método que não se tenha muita segurança de como utilizar
# podemos executar o modo help. 

