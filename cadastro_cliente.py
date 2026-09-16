from colorama import Fore, Style, init

init()

ARQUIVO = "dados_clientes.txt"
COL_NOME = 25
COL_EMAIL = 50
COL_TELEFONE = 15


def cadastro_cliente():
    print(Fore.MAGENTA + "==⚝= Cadastro de cliente =⚝==" + Style.RESET_ALL)

    while True:
        nome = input("Digite o nome: ").strip().title()

        if nome == "":
            print(Fore.RED + "\nO nome não pode ser vazio\n" + Style.RESET_ALL)
        elif nome.replace(" ", "").isalpha():
            break
        else:
            print(Fore.RED + "\nDigite somente texto!!\n" + Style.RESET_ALL)

    while True:
        email = input("Digite o Email(Gmail): ")

        if (
            email != ""
            and email.isascii()
            and email.endswith("@gmail.com")
            and " " not in email
            and len(email) > 10
            and "-" not in email
        ):
            break
        else:
            print(Fore.RED + "\nDigite um e-mail válido!!\n" + Style.RESET_ALL)

    while True:
        telefone = input("Digite o telefone(celular): ")
        telefone_certo = telefone.replace("-", "")

        if telefone_certo.isdigit() and len(telefone_certo) in (9, 11):
            break
        else:
            print(
                Fore.RED
                + "Erro: digite um número de telefone celular"
                + Style.RESET_ALL
            )

    cliente = {"nome": nome, "email": email, "telefone": telefone_certo}

    try:
        with open(ARQUIVO, "a", encoding="UTF-8") as arquivo:
            arquivo.write(f"{nome};{email};{telefone_certo}\n")

        print(
            Fore.LIGHTGREEN_EX
            + "\nCliente cadastrado com sucesso!!\n"
            + Style.RESET_ALL
        )
    except OSError:
        print(Fore.RED + "\nErro ao salvar o cliente.\n" + Style.RESET_ALL)


def listagem_cliente():
    print(Fore.MAGENTA + "==⚝= Lista de clientes =⚝==" + Style.RESET_ALL)

    try:
        with open(ARQUIVO, "r", encoding="UTF-8") as arquivo:
            conteudo = arquivo.readlines()

    except FileNotFoundError:
        print(Fore.YELLOW + "\nNenhum cliente cadastrado.\n" + Style.RESET_ALL)
        return

    if not conteudo:
        print(Fore.YELLOW + "\nNenhum cliente cadastrado.\n" + Style.RESET_ALL)
        return

    topo = (
        "╔"
        + "═" * (COL_NOME + 2)
        + "╦"
        + "═" * (COL_EMAIL + 2)
        + "╦"
        + "═" * (COL_TELEFONE + 2)
        + "╗"
    )
    meio = (
        "╠"
        + "═" * (COL_NOME + 2)
        + "╬"
        + "═" * (COL_EMAIL + 2)
        + "╬"
        + "═" * (COL_TELEFONE + 2)
        + "╣"
    )
    fim = (
        "╚"
        + "═" * (COL_NOME + 2)
        + "╩"
        + "═" * (COL_EMAIL + 2)
        + "╩"
        + "═" * (COL_TELEFONE + 2)
        + "╝"
    )

    print(Fore.CYAN + topo)

    print(
        Fore.CYAN
        + "║ "
        + Style.BRIGHT
        + Fore.WHITE
        + "NOME".ljust(COL_NOME)
        + Style.RESET_ALL
        + Fore.CYAN
        + " ║ "
        + Style.BRIGHT
        + Fore.WHITE
        + "E-MAIL".ljust(COL_EMAIL)
        + Style.RESET_ALL
        + Fore.CYAN
        + " ║ "
        + Style.BRIGHT
        + Fore.WHITE
        + "TELEFONE".center(COL_TELEFONE)
        + Style.RESET_ALL
        + Fore.CYAN
        + " ║"
    )

    print(Fore.CYAN + meio)

    try:
        for linha in conteudo:
            linha = linha.strip()

            if not linha:
                continue

            partes = linha.split(";")

            nome = partes[0].strip()
            email = partes[1].strip()
            telefone = partes[2].strip()

            print(
                Fore.CYAN
                + "║ "
                + Fore.WHITE
                + nome.ljust(COL_NOME)
                + Fore.CYAN
                + " ║ "
                + Fore.WHITE
                + email.ljust(COL_EMAIL)
                + Fore.CYAN
                + " ║ "
                + Fore.WHITE
                + telefone.center(COL_TELEFONE)
                + Fore.CYAN
                + " ║"
            )

        print(Fore.CYAN + fim)

    except (ValueError, IndexError):
        print(
            Fore.RED + "\nErro na listagem dos clientes!\n" + Style.RESET_ALL
        )


def alterar_cliente():
    print(Fore.MAGENTA + "==⚝= Alterar cliente =⚝==" + Style.RESET_ALL)
    try:
        with open(ARQUIVO, "r", encoding="UTF-8") as arquivo:
            clientes = arquivo.readlines()

    except FileNotFoundError:
        print(Fore.YELLOW + "\nNenhum cliente cadastrado.\n" + Style.RESET_ALL)
        return

    if not clientes:
        print(Fore.YELLOW + "\nNenhum cliente cadastrado.\n" + Style.RESET_ALL)
        return

    nome_busca = (
        input("Digite o nome do cliente que deseja alterar: ").strip().title()
    )
    encontrado = False

    for i in range(len(clientes)):
        partes = clientes[i].strip().split(";")

        if len(partes) == 3 and partes[0] == nome_busca:
            while True:
                novo_nome = input("Digite o novo nome: ").strip().title()

                if novo_nome == "":
                    print(
                        Fore.RED + "\nO nome não pode ser vazio\n" + Style.RESET_ALL
                    )

                elif novo_nome.replace(" ", "").isalpha():
                    break
                else:
                    print(
                        Fore.RED + "\nDigite somente texto!!\n" + Style.RESET_ALL
                    )

            while True:
                novo_email = input("Digite o novo Email(Gmail): ")
                if (
                    novo_email != ""
                    and novo_email.isascii()
                    and novo_email.endswith("@gmail.com")
                    and " " not in novo_email
                    and len(novo_email) > 10
                    and "-" not in novo_email
                ):
                    break
                else:
                    print(
                        Fore.RED
                        + "\nDigite um e-mail válido!!\n"
                        + Style.RESET_ALL
                    )

            while True:
                novo_telefone = input("Digite o novo telefone(celular): ")

                novo_telefone_certo = novo_telefone.replace("-", "")
                if novo_telefone_certo.isdigit() and len(novo_telefone_certo) in (
                    9,
                    11,
                ):
                    break
                else:
                    print(
                        Fore.RED
                        + "Erro: digite um número de telefone celular"
                        + Style.RESET_ALL
                    )

            clientes[i] = (
                f"{novo_nome};{novo_email};{novo_telefone_certo}\n"
            )
            encontrado = True
            break

    if encontrado:
        try:
            with open(ARQUIVO, "w", encoding="UTF-8") as arquivo:
                arquivo.writelines(clientes)
            print(
                Fore.LIGHTGREEN_EX
                + "\nCliente alterado com sucesso!\n"
                + Style.RESET_ALL
            )
        except OSError:
            print(Fore.RED + "\nErro ao salvar o cliente.\n" + Style.RESET_ALL)

    else:
        print(Fore.RED + "\nCliente não encontrado.\n" + Style.RESET_ALL)


def excluir_cliente():
    print(Fore.MAGENTA + "==⚝= Excluir cliente =⚝==" + Style.RESET_ALL)
    try:
        with open(ARQUIVO, "r", encoding="utf-8") as arquivo:
            linhas = arquivo.readlines()
    except FileNotFoundError:
        print(Fore.YELLOW + "\nNenhum cliente cadastrado.\n" + Style.RESET_ALL)
        return

    nome_busca = (
        input("Digite o nome do cliente que deseja excluir: ").strip().title()
    )
    novas_linhas = []
    encontrado = False

    for linha in linhas:
        dados = linha.strip().split(";")

        if dados[0] == nome_busca and not encontrado:
            encontrado = True
        else:
            novas_linhas.append(linha)

    if encontrado:
        try:
            with open(ARQUIVO, "w", encoding="utf-8") as arquivo:
                arquivo.writelines(novas_linhas)
            print(
                Fore.LIGHTGREEN_EX
                + "\nCliente excluído com sucesso!\n"
                + Style.RESET_ALL
            )

        except OSError:
            print(
                Fore.RED + "\nErro ao excluir o cliente.\n" + Style.RESET_ALL
            )
    else:
        print(Fore.YELLOW + "\nCliente não encontrado.\n" + Style.RESET_ALL)
