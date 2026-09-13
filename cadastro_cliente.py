clientes = [] 
def cadastro_cliente():
    while True:
            nome = input("Digite o nome: ").strip().title()
            if nome == "":
                print("\nO nome não pode ser vazio\n")
            elif nome.replace(" ", "").isalpha():
                break
            else:
                print("\nDigite somente texto\n")
                
    while True:
        
        email = input("Digite o email: ")
        
        if email != "" and email.endswith("@gmail.com") and " " not in email and len(email) > 10 and "-" not in email:
            break
        else:
            print("\nDigite um e-mail válido!!\n")
            
    while True:
                telefone = input("digite o telefone:")
                
                telefone_certo = telefone.replace("-","")
                
                if telefone_certo.isdigit() and len(telefone_certo) in (9,11):
                    break
                else:
                    print("Erro: digite um número de telefone")
                
    cliente = {
        "nome": nome,
        "email": email,
        "telefone": telefone_certo
    }

    clientes.append(cliente)
    print("\n Cliente cadastrado com sucesso!!\n")

def listagem_cliente():
    if not clientes:
        print("\n Nenhum cliente cadastrado.\n")
        
    else:
    
        for cliente in clientes:
            print(f"Nome: {cliente["nome"]} | E-mail: {cliente["email"]} | Telefone: {cliente["telefone"]}\n")  

                  



         