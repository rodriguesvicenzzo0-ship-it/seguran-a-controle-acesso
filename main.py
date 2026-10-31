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

# Dados institucionais - Aluno 1
empresa = {
    "nome": "Tech Estoque",
    "ramo": "Controle de Estoque",
    "responsavel": "Equipe de Desenvolvimento"
}

# Matriz 2D do estoque - Aluno 2
# Cada linha representa um setor e cada coluna um produto.
estoque = [
    ["Teclado", "Mouse", "Monitor"],
    [10, 15, 5],
    ["Gabinete", "Headset", "Webcam"],
    [8, 12, 7]
]


def validar_texto(mensagem):
    """Impede que o usuário digite um texto vazio."""
    while True:
        texto = input(mensagem).strip()

        if texto:
            return texto

        print("Erro: o campo não pode ficar vazio!")


def validar_opcao():
    """Valida a opção digitada no menu."""
    while True:
        opcao = input("Escolha uma opção: ").strip()

        if not opcao:
            print("Erro: digite uma opção!")
            continue

        if opcao.isdigit():
            opcao = int(opcao)

            if 1 <= opcao <= 4:
                return opcao

        print("Opção inválida! Digite um número de 1 a 4.")


def mostrar_empresa():
    """Exibe os dados cadastrados pelo Aluno 1."""
    print("\n--- DADOS DA EMPRESA ---")
    print("Nome:", empresa["nome"])
    print("Ramo:", empresa["ramo"])
    print("Responsável:", empresa["responsavel"])


def mostrar_estoque():
    """Exibe os produtos e suas quantidades."""
    print("\n--- ESTOQUE DISPONÍVEL ---")

    for setor_idx in range(0, len(estoque), 2):
        produtos = estoque[setor_idx]
        quantidades = estoque[setor_idx + 1]

        print(f"\nSetor {(setor_idx // 2) + 1}:")

    for de in range(len(produtos)):
        print(f"{produtos[i]}: {quantidades[i]} unidades")


def consultar_produto():
    """Procura um produto na matriz 2D."""
    nome = validar_texto(
        "\nDigite o nome do produto que deseja consultar: "
    ).lower()

    for setor_idx in range(0, len(estoque), 2):
        produtos = estoque[setor_idx]
        quantidades = estoque[setor_idx + 1]

        for indice, produto in enumerate(produtos):
            if produto.lower() == nome:
                print("\nProduto encontrado!")
                print("Nome:", produto)
                print("Quantidade:", quantidades[indice])
                return

    print("Produto não encontrado no estoque.")


def menu():
    """Menu principal do sistema."""
    while True:
        print("\n==============================")
        print(" TECH ESTOQUE")
        print("==============================")
        print("1 - Ver dados da empresa")
        print("2 - Listar estoque")
        print("3 - Consultar produto")
        print("4 - Sair")
        print("==============================")

        opcao = validar_opcao()

        if opcao == 1:
            mostrar_empresa()

        elif opcao == 2:
            mostrar_estoque()

        elif opcao == 3:
            consultar_produto()

        elif opcao == 4:
            print("\nSistema encerrado. Obrigado!")
            break


# Início do programa
menu()