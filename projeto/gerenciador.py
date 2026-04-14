import os 
os.system("cls")

while True:
    print("\nMenu do Gerenciador de Lista de Tarefas: ")
    print("1. Adicionar tarefa")
    print("2. Ver tarefas")
    print("3. Atualizar tarefa")
    print("4. Completar tarefa")
    print("5. Deletar tarefas completadas")
    print("6. Sair")

    print()
    escolha = input("Digite a sua escolha: ")

    if escolha == "6":
        break

print("Programa finalizado!")