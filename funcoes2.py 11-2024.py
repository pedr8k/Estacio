# Definindo a função loginUsuario
def loginUsuario(perfil):
    # Verificando se o valor de 'perfil' é igual a 'admin', considerando maiúsculas e minúsculas
    if perfil.lower() == 'admin':
        print('Bem-vindo, Administrador')
    else:
        print('Bem-vindo, Usuário')

# Chamando a função com diferentes valores como parâmetro
loginUsuario('Admin')   # Exemplo 1
loginUsuario('admin')   # Exemplo 2
loginUsuario('User')    # Exemplo 3
loginUsuario('usuário') # Exemplo 4