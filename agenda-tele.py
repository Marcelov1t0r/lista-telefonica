from time import sleep
import os

agenda=[]
sair=False

while(sair==False):
    print("*** Lista de opções ***")
    print("1 - Novo contato")
    print("2 - Exibir contatos")
    print("3 - Editar contato")
    print("4 - Excluir contato\n")
    opcao=int(input("Digite a opção escolhida:"))

    #sleep(1)

    if(opcao==1): # Add contatos
        novo_contato=[]
        nome=input("\nDigite o nome do contato: ")
        novo_contato.append(nome)
        telefone=input("Digite o número do contato: ")
        novo_contato.append(telefone)
        agenda.append(novo_contato)
        os.system('cls')

    if(opcao==2):
        for contato in agenda:
            print("\nNome:",contato[0],"Telefone:",contato[1],"\n")