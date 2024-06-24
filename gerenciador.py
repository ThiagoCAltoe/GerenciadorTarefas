def adicionar_tarefa(tarefas,  nome_tarefa):
    tarefa = {"tarefa": nome_tarefa, "completada": False}
    tarefas.append(tarefa)
    print(f"Tarefa {nome_tarefa} adicionada com sucesso!")
    return

def ver_tarefas(tarefas):
    print("\nLista de Tarefas:")
    for i, tarefa in enumerate(tarefas, start=1):
        status = "✔️  " if tarefa["completada"] else " "
        nome_tarefa = tarefa["tarefa"]
        print(f"{i}. [{status}] {nome_tarefa}")
    return

def atualizar_tarefa(tarefas, indice_tarefa, novo_nome_tarefa):
    if indice_tarefa < 1 or indice_tarefa > len(tarefas):
        print("Tarefa não encontrada!")
        return
    tarefas[indice_tarefa - 1]["tarefa"] = novo_nome_tarefa
    print(f"Tarefa {indice_tarefa} atualizada para {novo_nome_tarefa}!")
    return

def completar_tarefa(tarefas, indice_tarefa):
    if indice_tarefa < 1 or indice_tarefa > len(tarefas):
        print("Tarefa não encontrada!")
        return
    tarefas[indice_tarefa - 1]["completada"] = True
    print(f"Tarefa {indice_tarefa} completada!")
    return

def deletar_tarefas_completadas(tarefas):
    tarefas[:] = [tarefa for tarefa in tarefas if not tarefa["completada"]]
    print("Tarefas completadas deletadas!")
    return

tarefas = []

while True:
    print("\n Menu do Gerenciador de Tarefas:")
    print("1. Adicionar Tarefa")
    print("2. Ver Tarefas")
    print("3. Atualizar Tarefa")
    print("4. Completar Tarefa")
    print("5. Deletar Tarefas Completadas")
    print("6. Sair")

    escolha = input("Escolha uma opção: ")

    if escolha == "1":
        nome_tarefa = input("Digite o nome da tarefa: ")
        adicionar_tarefa(tarefas, nome_tarefa)
    elif escolha == "2":
        ver_tarefas(tarefas)
    elif escolha == "3":
        ver_tarefas(tarefas)
        indice_tarefa = int(input("Digite o número da tarefa que deseja atualizar: "))
        novo_nome_tarefa = input("Digite o novo nome da tarefa: ")
        atualizar_tarefa(tarefas, indice_tarefa, novo_nome_tarefa)
    elif escolha == "4":
        ver_tarefas(tarefas)
        indice_tarefa = int(input("Digite o número da tarefa que deseja completar: "))
        completar_tarefa(tarefas, indice_tarefa)
    elif escolha == "5":
        deletar_tarefas_completadas(tarefas)
        ver_tarefas(tarefas)
    elif escolha == "6":
        break

    print("Programa finalizado.")