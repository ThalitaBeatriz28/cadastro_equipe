from colorama import init, Fore, Style

init()

ARQUIVO = "dados_prod.txt"

COL_PRODUTO = 25
COL_VALOR = 15
COL_QUANTIDADE = 15


def cadastro_prod():
    print(Fore.MAGENTA + "==⚝= Cadastro de produto =⚝==" + Style.RESET_ALL)
    try:
        with open(ARQUIVO, "x", encoding="UTF-8") as arquivo:
            pass
    except FileExistsError:
        pass

    print("\nRegistro do produto\n")

    while True:
        nome_prod = input("Digite o nome do produto: ").strip().title()

        if nome_prod == "":
            print("\nO produto precisa ser nomeado.\n")
        elif nome_prod.replace(" ", "").isalpha():
            break
        else:
            print("\nDigite APENAS texto!\n")

    while True:
        try:
            valor = float(input("Digite o valor unitário: ").strip().replace(",", "."))
            if valor <= 0:
                print("\nDigite apenas valores positivos e válidos.\n")
            else:
                break
        except ValueError:
            print("\nDigite apenas números.\n")

    while True:
        try:
            quantidade = int(input("Digite a quantidade: ").strip())
            if quantidade <= 0:
                print("\nDigite apenas quantidades válidas.\n")
            else:
                break
        except ValueError:
            print("\nDigite apenas quantidades válidas.\n")
    try:
        with open(ARQUIVO, "a", encoding="UTF-8") as arquivo:
            arquivo.write(f"{nome_prod};{valor:.2f};{quantidade}\n")
        print(Fore.LIGHTGREEN_EX + "\nProduto cadastrado com sucesso!\n" + Style.RESET_ALL)
    except OSError:
        print(Fore.RED + "\nErro ao salvar o produto.\n" + Style.RESET_ALL)


def listar_produtos():
    print(Fore.MAGENTA + "==⚝= Lista de produtos =⚝==" + Style.RESET_ALL)

    try:
        with open(ARQUIVO, "r", encoding="UTF-8") as arquivo:
            conteudo = arquivo.readlines()
    except FileNotFoundError:
        print(Fore.YELLOW + "\nNenhum produto cadastrado ainda!\n" + Style.RESET_ALL)
        return
    if not conteudo:
        print(Fore.YELLOW + "\nNenhum produto cadastrado ainda!\n" + Style.RESET_ALL)
        return

    topo = "╔" + "═" * (COL_PRODUTO + 2) + "╦" + "═" * (COL_VALOR + 2) + "╦" + "═" * (COL_QUANTIDADE + 2) + "╗"
    meio = "╠" + "═" * (COL_PRODUTO + 2) + "╬" + "═" * (COL_VALOR + 2) + "╬" + "═" * (COL_QUANTIDADE + 2) + "╣"
    fim = "╚" + "═" * (COL_PRODUTO + 2) + "╩" + "═" * (COL_VALOR + 2) + "╩" + "═" * (COL_QUANTIDADE + 2) + "╝"

    print(Fore.CYAN + topo)
    print(
        Fore.CYAN + "║ " +
        Style.BRIGHT + Fore.WHITE + "PRODUTO".ljust(COL_PRODUTO) +
        Style.RESET_ALL + Fore.CYAN + " ║ " +
        Style.BRIGHT + Fore.WHITE + "VALOR".center(COL_VALOR) +
        Style.RESET_ALL + Fore.CYAN + " ║ " +
        Style.BRIGHT + Fore.WHITE + "QUANTIDADE".center(COL_QUANTIDADE) +
        Style.RESET_ALL + Fore.CYAN + " ║"
    )
    print(Fore.CYAN + meio)
    try:
        for linha in conteudo:
            linha = linha.strip()
            if not linha:
                continue
            partes = linha.split(";")
            nome = partes[0].strip()
            valor = float(partes[1].strip())
            quantidade = int(partes[2].strip())
            print(
                Fore.CYAN + "║ " +
                Fore.WHITE + nome.ljust(COL_PRODUTO) +
                Fore.CYAN + " ║ " +
                Fore.WHITE + f"R$ {valor:.2f}".center(COL_VALOR) +
                Fore.CYAN + " ║ " +
                Fore.WHITE + str(quantidade).center(COL_QUANTIDADE) +
                Fore.CYAN + " ║"
            )
        print(Fore.CYAN + fim + Style.RESET_ALL)
    except (ValueError, IndexError):
        print(Fore.RED + "\nErro na listagem dos produtos!\n" + Style.RESET_ALL)


def alterar_produto():
    print(Fore.MAGENTA + "==⚝= Alterar produto =⚝==" + Style.RESET_ALL)

    try:
        with open(ARQUIVO, "r", encoding="UTF-8") as arquivo:
            produtos = arquivo.readlines()
    except FileNotFoundError:
        print(Fore.YELLOW + "\nNenhum produto cadastrado.\n" + Style.RESET_ALL)
        return
    if not produtos:
        print(Fore.YELLOW + "\nNenhum produto cadastrado.\n" + Style.RESET_ALL)
        return

    nome_busca = input("Digite o nome do produto que deseja alterar: ").strip().title()
    encontrado = False

    for i in range(len(produtos)):
        partes = produtos[i].strip().split(";")
        if len(partes) == 3 and partes[0] == nome_busca:
            novo_nome = input("Digite o nome do produto: ").strip().title()
            if novo_nome == "":
                print("\nO produto precisa ser nomeado.\n")
            elif novo_nome.replace(" ", "").isalpha():
                break
            else:
                print("\nDigite APENAS texto!\n")
            while True:
                try:
                    novo_valor = float(input("Digite o novo valor: ").strip().replace(",", "."))
                    if novo_valor <= 0:
                        print("\nDigite um valor positivo.\n")
                    else:
                        break
                except ValueError:
                    print("\nDigite apenas números.\n")
            while True:
                try:
                    nova_quantidade = int(input("Digite a nova quantidade: ").strip())
                    if nova_quantidade <= 0:
                        print("\nDigite uma quantidade válida.\n")
                    else:
                        break
                except ValueError:
                    print("\nDigite apenas números inteiros.\n")
            produtos[i] = f"{novo_nome};{novo_valor:.2f};{nova_quantidade}\n"
            encontrado = True
            break

    if encontrado:
        with open(ARQUIVO, "w", encoding="UTF-8") as arquivo:
            arquivo.writelines(produtos)
        print(Fore.LIGHTGREEN_EX + "\nProduto alterado com sucesso!\n" + Style.RESET_ALL)
    else:
        print(Fore.RED + "\nProduto não encontrado.\n" + Style.RESET_ALL)


def excluir_produto():
    print(Fore.MAGENTA + "==⚝= Excluir produto =⚝==" + Style.RESET_ALL)
    try:
        with open(ARQUIVO, "r", encoding="UTF-8") as arquivo:
            produtos = arquivo.readlines()
    except FileNotFoundError:
        print(Fore.YELLOW + "\nNenhum produto cadastrado.\n" + Style.RESET_ALL)
        return
    if not produtos:
        print(Fore.YELLOW + "\nNenhum produto cadastrado.\n" + Style.RESET_ALL)
        return

    nome_busca = input("Digite o nome do produto que deseja excluir: ").strip().title()
    novos_produtos = []
    encontrado = False

    for linha in produtos:
        partes = linha.strip().split(";")
        if len(partes) == 3 and partes[0] == nome_busca:
            encontrado = True
        else:
            novos_produtos.append(linha)
    if encontrado:
        with open(ARQUIVO, "w", encoding="UTF-8") as arquivo:
            arquivo.writelines(novos_produtos)
        print(Fore.LIGHTGREEN_EX + "\nProduto excluído com sucesso!\n" + Style.RESET_ALL)
    else:
        print(Fore.RED + "\nProduto não encontrado.\n" + Style.RESET_ALL)