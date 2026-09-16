from colorama import init, Fore, Style

from cadastro_cliente import (
    cadastro_cliente,
    listagem_cliente,
    alterar_cliente,
    excluir_cliente
)

from cadastro_produto import (
    cadastro_prod,
    listar_produtos,
    alterar_produto,
    excluir_produto
)

init()

LARGURA = 42


def exibir_menu():
    print(Fore.CYAN + "╔" + "═" * LARGURA + "╗")
    print(
        Fore.CYAN + "║" +
        Style.BRIGHT + Fore.WHITE +
        "SISTEMA DE CADASTRO".center(LARGURA) +
        Style.RESET_ALL + Fore.CYAN + "║"
    )
    print(Fore.CYAN + "╠" + "═" * LARGURA + "╣")
    print(Fore.CYAN + "║" + Fore.BLUE + "  1 - Clientes".ljust(LARGURA) + Fore.CYAN + "║")
    print(Fore.CYAN + "║" + Fore.BLUE + "  2 - Produtos".ljust(LARGURA) + Fore.CYAN + "║")
    print(Fore.CYAN + "║" + Fore.RED + "  0 - Sair".ljust(LARGURA) + Fore.CYAN + "║")
    print(Fore.CYAN + "╚" + "═" * LARGURA + "╝" + Style.RESET_ALL)


def menu_clientes():
    while True:
        print(Fore.CYAN + "╔" + "═" * LARGURA + "╗")
        print(
            Fore.CYAN + "║" +
            Style.BRIGHT + Fore.WHITE +
            "CADASTRO DE CLIENTES".center(LARGURA) +
            Style.RESET_ALL + Fore.CYAN + "║"
        )
        print(Fore.CYAN + "╠" + "═" * LARGURA + "╣")
        print(Fore.CYAN + "║" + Fore.BLUE + "  1 - Cadastrar cliente".ljust(LARGURA) + Fore.CYAN + "║")
        print(Fore.CYAN + "║" + Fore.BLUE + "  2 - Listar clientes".ljust(LARGURA) + Fore.CYAN + "║")
        print(Fore.CYAN + "║" + Fore.BLUE + "  3 - Alterar cliente".ljust(LARGURA) + Fore.CYAN + "║")
        print(Fore.CYAN + "║" + Fore.BLUE + "  4 - Excluir cliente".ljust(LARGURA) + Fore.CYAN + "║")
        print(Fore.CYAN + "║" + Fore.RED + "  0 - Voltar".ljust(LARGURA) + Fore.CYAN + "║")
        print(Fore.CYAN + "╚" + "═" * LARGURA + "╝" + Style.RESET_ALL)

        opcao = input("Digite uma opção: ").strip()

        if opcao == "1":
            cadastro_cliente()
        elif opcao == "2":
            listagem_cliente()
        elif opcao == "3":
            alterar_cliente()
        elif opcao == "4":
            excluir_cliente()
        elif opcao == "0":
            break
        else:
            print(Fore.RED + "\nOpção inválida!\n" + Style.RESET_ALL)


def menu_produtos():
    while True:
        print(Fore.CYAN + "╔" + "═" * LARGURA + "╗")
        print(
            Fore.CYAN + "║" +
            Style.BRIGHT + Fore.WHITE +
            "CADASTRO DE PRODUTOS".center(LARGURA) +
            Style.RESET_ALL + Fore.CYAN + "║"
        )
        print(Fore.CYAN + "╠" + "═" * LARGURA + "╣")
        print(Fore.CYAN + "║" + Fore.BLUE + "  1 - Cadastrar produto".ljust(LARGURA) + Fore.CYAN + "║")
        print(Fore.CYAN + "║" + Fore.BLUE + "  2 - Listar produtos".ljust(LARGURA) + Fore.CYAN + "║")
        print(Fore.CYAN + "║" + Fore.BLUE + "  3 - Alterar produto".ljust(LARGURA) + Fore.CYAN + "║")
        print(Fore.CYAN + "║" + Fore.BLUE + "  4 - Excluir produto".ljust(LARGURA) + Fore.CYAN + "║")
        print(Fore.CYAN + "║" + Fore.RED + "  0 - Voltar".ljust(LARGURA) + Fore.CYAN + "║")
        print(Fore.CYAN + "╚" + "═" * LARGURA + "╝" + Style.RESET_ALL)

        opcao = input("Digite uma opção: ").strip()

        if opcao == "1":
            cadastro_prod()
        elif opcao == "2":
            listar_produtos()
        elif opcao == "3":
            alterar_produto()
        elif opcao == "4":
            excluir_produto()
        elif opcao == "0":
            break
        else:
            print(Fore.RED + "\nOpção inválida!\n" + Style.RESET_ALL)


def main():
    while True:
        exibir_menu()
        opcao = input("Digite uma opção: ").strip()

        if opcao == "1":
            menu_clientes()
        elif opcao == "2":
            menu_produtos()
        elif opcao == "0":
            print(Fore.LIGHTGREEN_EX + "\nSistema encerrado. Até mais!\n" + Style.RESET_ALL)
            break
        else:
            print(Fore.RED + "\nOpção inválida!\n" + Style.RESET_ALL)


main()