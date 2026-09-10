def cadastro():
    print("\nRegistro do produto:")
    while True:
        produto = input("Digite o nome do produto: ").strip().title()
        if produto.replace(" ", "").isalpha():
            break
        else:
            print("\nDigite APENAS texto!")
