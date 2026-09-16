from colorama import init, Fore, Back, Style
init()

clientes = [] 

def cadastro_cliente():
    while True:
        print(Fore.MAGENTA +"==⚝= Cadastro de cliente =⚝==" + Style.RESET_ALL)
        nome = input("Digite o nome: ").strip().title()
        if nome == "":
            print(Fore.RED +"\nO nome não pode ser vazio\n"+ Style.RESET_ALL)
        elif nome.replace(" ", "").isalpha():
            break
        else:
            print(Fore.RED +"\nDigite somente texto!!\n"+ Style.RESET_ALL)
                
    while True:
        email = input("Digite o Email(Gmail): ")
        if email != "" and email.isascii() and email.endswith("@gmail.com") and " " not in email and len(email) > 10 and "-" not in email:
            break
        else:
            print(Fore.RED + "\nDigite um e-mail válido!!\n" + Style.RESET_ALL)

    while True:
        telefone = input("digite o telefone(celular):")
        telefone_certo = telefone.replace("-","")
        if telefone_certo.isdigit() and len(telefone_certo) in (9,11):
            break
        else:
            print(Fore.RED + "Erro: digite um número de telefone"+ Style.RESET_ALL)
            
    cliente = {
            "nome": nome,
            "email": email,
            "telefone": telefone_certo
        }
    clientes.append(cliente)
    
    with open("clientes.txt", "a", encoding="utf-8") as arquivo:
        arquivo.write(f"Nome: {cliente['nome']} | E-mail: {cliente['email']} | Telefone: {cliente['telefone']}\n")
    
    print(Fore.LIGHTGREEN_EX + "\n Cliente cadastrado com sucesso e salvo em TXT!!\n"+ Style.RESET_ALL)

