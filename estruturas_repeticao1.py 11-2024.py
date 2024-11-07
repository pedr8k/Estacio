# 1. Criação da variável 'entrada_idade' com valor inicial ''
entrada_idade = ''

# 2. Estrutura 'while' que verifica se o valor da variável é diferente de '0'
while str(entrada_idade) != '0':
    # 3. Solicitação de entrada do usuário
    entrada_idade = input("Digite um número qualquer ou 0 para sair: ")
    
    # 4. Exibição do número digitado pelo usuário
    print("Número digitado:", entrada_idade)