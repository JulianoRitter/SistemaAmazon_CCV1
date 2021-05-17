
index = 0
#CADASTRO DE CLIENTES
cliente_username = []
cliente_cpf = []
cliente_senha = []
cliente_email = []
cliente_limitecredito = []

# Lista de produtos
#produtos_carrinho = []
#produtos_total = [{'Pasta de dente': '500.00'}, {'Arroz 5 kg': '100.00'}, {'Feijão 1 kg': '500.00'}, {'Açucar 1 kg': '50.00'}]
#produtos_nome = ['Pasta de dente', 'Arroz 5 kg', 'Feijão 1 kg', 'Açucar 1 kg']
#produtos_preco = [5.00, 10.00, 4.00, 2.00]
#print (produtos_nome)

def cpf_validate(numbers):
    #  Obtém os números do CPF e ignora outros caracteres
    cpf = [int(char) for char in numbers if char.isdigit()]

    #  Verifica se o CPF tem 11 dígitos
    if len(cpf) != 11:
        return False

    #  Verifica se o CPF tem todos os números iguais, ex: 111.111.111-11
    #  Esses CPFs são considerados inválidos mas passam na validação dos dígitos
    #  Antigo código para referência: if all(cpf[i] == cpf[i+1] for i in range (0, len(cpf)-1))
    if cpf == cpf[::-1]:
        return False

    #  Valida os dois dígitos verificadores
    for i in range(9, 11):
        value = sum((cpf[num] * ((i+1) - num) for num in range(0, i)))
        digit = ((value * 10) % 11) % 10
        if digit != cpf[i]:
            return False
    return True

def cadastro (cpf):
    #Caso o cliente não esteja cadastrado solicita os dados e armazena
    if not cpf in cliente_cpf:
        cliente_cpf.append(cpf)
        nome = input("Digite seu Nome: ")
        cliente_username.append(nome)

        #inicia uma verificação de senha de 6 digitos
        while True:
            senha = input("Digite sua senha: ")
            tamanho_senha = len(list(senha))
            if tamanho_senha == 6:
                cliente_senha.append(senha)
                break
            else:
                print("Senha não corresponde aos requisitos \n")

        email = input("Digite seu email: ")
        cliente_email.append(email)
        cliente_limitecredito.append(1000.00) 
        
        print ("Parabéns, Cadastro concluido com sucesso! \n")
        return True

#verificar se o cliente já existe a partir do cpf
    else:    
        for cpf in cliente_cpf:
            print("Cliente já cadastrado com o nome de: ", cliente_username)
        return True
        
#Verificando o parametro senhas


def menu():
    opcao = "-1"

    while opcao != "0":
        print("""Menu: \n
1 - Cadastro
2 - Comprar
3 - Mostrar carrinho
4 - Pagar conta
5 - Consultar cliente
6 - Mostrar produtos
0 - Sair""")
        opcao = input("\nSelecione uma opção: ")

        #cadastro de novos clientes
        if opcao == "1":
            print("Opção selecionada: Cadastro \n")
            cpf = input("Digite seu CPF: ")
            #Verificar CPF se é valido ou não
            if cpf_validate(cpf):
                print('CPF válido.')
                cadastro(cpf)
            else:
                print('CPF inválido.')
        
        elif opcao == "2":
            print("Opção selecionada: Comprar \n")
            #print (produtos_nome)

        elif opcao == "3":
            print("Opção selecionada: Mostrar carrinho \n")

        elif opcao == "4":
            print("Opção selecionada: Pagar conta \n")

            #Confirmação de compra
            cpf=input("Digite  o cpf: ")
            if cpf in cliente_cpf:
                
                senha = input("Digite  a senha: ")
                if senha in cliente_senha:
                    print ("Pagamento efutado com sucesso! \n")
                    cliente_limitecredito.clear()
                    
                else:
                        print ("Senha incorreta. \n")

            #Verificação de CPF
            if not cpf in cliente_cpf:
                    print("CPF incorreto.")

        elif opcao == "5":
            print("Opção selecionada: Consultar cliente \n")            
            #consulta_cliente()

        elif opcao == "6":
            print("Opção selecionada: Mostrar produtos na prateleira \n")            
            #print (type(produtos_total))

        elif opcao == "0":
            print("Bye...")
            
        else:
            print("Opção inválida! Tente novamente. \n")

menu()
def produtos_total():
        escolha=6
        lista=[]

while escolha !="0":
  print("Menu")
  print("0 - Fim")
  print("1 - Cadastra Produtos")
  print("2 - Confere Lista de Produtos")
  print("3 - Confirma Produto")
  print("4 - Mostra Total")
  escolha=input("Escolha uma opção:")
  if escolha =="0":
    escolha=input("Tem certeza que quer sair? 0 - Sim , 5 - Não")
  if escolha =="1":
    print("Cadastrando produto...")
    produto=input("Escolha o nome do produto:")
    quantidade=input("Escolha a quantidade do produto:")
    preco=input("Escola um preço para o produto")
    lista.append(["",produto,quantidade,0,preco])
  if escolha=="2":
    print("Exibindo produtos...")
    contador=0
    for produto in lista:

      print(contador,"#",produto[0]," ",produto[1],"-",produto[2])
      contador=contador+1
  if escolha=="3":
    print("Confirmando produto...")
    posicao=input("Digite a posição do produto:")
    posicao_int=int(posicao)
    preco=input("Digite o preco do "+lista[posicao_int][1] +":")
    lista[posicao_int][0]="OK"
    lista[posicao_int][3]=preco
  if escolha=="4":
    print("Mostrando Todos Produtos...")
    print("Produtos que não foram comprados...")
    contador=0
    for produto in lista:
      if produto[0]=="":
        print(contador,"#",produto[0]," ",produto[1],"-",produto[2], "R$", produto[3])
        contador=contador+1
    print("Produtos que foram comprados...")
    contador=0
    precototal=0
    for produto in lista:
      if produto[0]=="OK":
        print(contador,"#",produto[0]," ",produto[1],"-",produto[2], "R$", produto[3])
        contador=contador+1
        precototal=precototal+int(produto[2])*float(produto[3])
    print("Preco Total: R$",precototal)


print("Fim do programa!")
