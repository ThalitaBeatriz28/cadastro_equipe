def cadastroPROD():
    print("\nRegistro do produto:")
    while True:
        produto = input("Digite o nome do produto: ").strip().title()
        if produto == "":
            print("\nO produto precisa ser nomeado\n")
        elif produto.replace(" ", "").isalpha():
            break
        else:
            print("\nDigite APENAS texto!\n")

    while True:
        try:
            valor = float(input("Digite o valor unitário: ").strip().replace("," , "."))
            if valor < 0:
                print("\nDigite apenas valores positivos e válidos\n")
            else:
                break
        except ValueError:
            print("\nDigite apenas números\n")

    while True:
        try:
            qnt = int(input("Digite a quantidade: ").strip())
            if valor < 0:
                print("\nDigite apenas quantidades válidos\n")
            else:
                break
        except ValueError:
            print("\nDigite apenas quantidades válidas\n")


cadastroPROD()

