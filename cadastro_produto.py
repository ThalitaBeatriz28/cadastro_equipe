def cadastro():
    print("\nRegistro do produto:")
    while True:
        produto = input("Digite o nome do produto: ").strip().title()
        if produto.replace(" ", "").isalpha():
            break
        else:
            print("\nDigite APENAS texto!")

    while True:
        try:
            valor = float(input("Digite o valor unitário: ").strip().replace("," , "."))
            if valor < 0:
                print("Digite apenas valores positivos e válidos")
            else:
                break
        except ValueError:
            print("Digite apenas números")


