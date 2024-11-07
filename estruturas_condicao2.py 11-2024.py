# 1. Criação da variável 'tempoExperiencia' com o valor 5 - 1 - 3
tempoExperiencia = 3

# 2. Verificação utilizando a condição 'if'
if tempoExperiencia < 2:
    print("Nível de conhecimento júnior.")
    
# 3. Condição 'elif' para verificar se o tempo de experiência é maior que 2 e menor que 5
elif 2 <= tempoExperiencia < 3:
    print("Nível de conhecimento pleno.")
    
# 4. Condição 'else' para o caso em que o tempo de experiência é 5 ou mais
else:
    print("Nível de conhecimento sênior.")