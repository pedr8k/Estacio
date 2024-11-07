def adicao(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    if b == 0:
        return "Não foi possível realizar a divisão por 0"
    else:
        return a / b

# Função calculadora
def calculadora(num1, num2, operacao):
    if operacao == '+' or operacao.lower() == 'adicao':
        resultado = adicao(num1, num2)
    elif operacao == '-' or operacao.lower() == 'subtracao':
        resultado = subtracao(num1, num2)
    elif operacao == '*' or operacao.lower() == 'multiplicacao':
        resultado = multiplicacao(num1, num2)
    elif operacao == '/' or operacao.lower() == 'divisao':
        resultado = divisao(num1, num2)
    else:
        return "Operação inválida"
    
    return resultado

# Laço while para interagir com o usuário
saida = ''
while saida.lower() != 'n':
    # Solicitar os dois números e a operação ao usuário
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    operacao = input("Digite a operação (+, -, *, / ou nome da operação): ")

    # Chama a função calculadora
    resultado = calculadora(num1, num2, operacao)
    
    # Exibe o resultado
    print("Resultado da operação: " + str(resultado))
    
    # Pergunta ao usuário se ele deseja continuar
    saida = input("Deseja continuar? (S/N): ")
    # Verifica se a entrada do usuário é diferente de 'N' ou 'n' para continuar
    if saida.lower() == 'n':
        print("Encerrando o programa.")
        break