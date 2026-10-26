# Dicionário com os dados da empresa
empresa = {
    "nome": "TechStore",
    "ramo": "Venda de produtos eletrônicos",
    "cidade": "São Paulo",
    "cnpj": "12.345.678/0001-90"
}

# Lista de itens em estoque
estoque = [
    "Computador",
    "Notebook",
    "Teclado",
    "Mouse",
    "Monitor"
]

# Lista de recursos em operação
recursos = [
    "Funcionários",
    "Computadores",
    "Sistema de vendas",
    "Internet"
]

# Exibindo os dados cadastrados
print("=== CADASTRO DA EMPRESA ===")
print(empresa)

print("\n=== ITENS EM ESTOQUE ===")
print(estoque)

print("\n=== RECURSOS EM OPERAÇÃO ===")
print(recursos)

tarefas = [
    [0, 1],
    [1, 0]
]

pendentes = 0
concluidas = 0

print("Matriz de tarefas:")

for i in range(2):
    for j in range(2):
        print(tarefas[i][j], end=" ")

        if tarefas[i][j] == 0:
            pendentes += 1
        else:
            concluidas += 1

    print()

print("Pendentes:", pendentes)
print("Concluídas:", concluidas)

