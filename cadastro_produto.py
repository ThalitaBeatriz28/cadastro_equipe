import os     
def cadastroPROD():
    try:
        with open ("dados_prod.txt", "x", encoding="UTF-8") as arquivo:
            pass
    except:
        pass
    
    print("\nRegistro do produto\n")

    while True:
        nome_prod = input("Digite o nome do produto: ").strip().title()
        if nome_prod == "":
            print("\nO produto precisa ser nomeado\n")
        elif nome_prod.replace(" ", "").isalpha():
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
            quantidade = int(input("Digite a quantidade: ").strip())
            if quantidade < 0:
                print("\nDigite apenas quantidades válidos\n")
            else:
                break
        except ValueError:
            print("\nDigite apenas quantidades válidas\n")

    try:
        with open ("dados_prod.txt", "a", encoding="UTF-8") as arquivo:
            arquivo.write(f"{nome_prod};{valor:.2f};{quantidade}\n")
            
        print ("\nProduto cadastrado com sucesso!\n")
    except:
        print ("ERRO")


cadastroPROD()

