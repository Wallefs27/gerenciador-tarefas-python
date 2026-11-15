
import json


def salvar_tarefas(tarefas):
    with open("tarefas.json", "w", encoding="utf-8") as arquivo:
        json.dump(tarefas, arquivo, ensure_ascii=False, indent=4)


def carregar_tarefas():
    try:
        with open("tarefas.json", "r", encoding="utf-8") as arquivo:
            return json.load(arquivo)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        print("Erro: o arquivo de tarefas contém dados inválidos.")
        raise


def listar_tarefas(tarefas):
    if not tarefas:
        print("Nenhuma tarefa cadastrada!")

    for indice, tarefa in enumerate(tarefas, start=1):
        if tarefa["concluida"]:
            status = "[X]"
        else:
            status = "[ ]"

        print(indice, "-", status, tarefa["descricao"])


def adicionar_tarefa(tarefas):
    nova_tarefa = input("Digite uma nova tarefa: ").strip()

    if not nova_tarefa:
        print("Erro! A descrição não pode ser vazia.")
        return

    tarefas.append({
        "descricao": nova_tarefa,
        "concluida": False
    })

    salvar_tarefas(tarefas)
    print("Tarefa adicionada!")


def concluir_tarefa(tarefas):
    if not tarefas:
        print("Nenhuma tarefa cadastrada!")
        return

    listar_tarefas(tarefas)

    try:
        numero = int(input("Número da tarefa para concluir: "))
    except ValueError:
        print("Digite um número válido!")
        return

    if 1 <= numero <= len(tarefas):
        tarefa = tarefas[numero - 1]

        if tarefa["concluida"]:
            print("essa tarefa já foi concluída!")

        else:
            tarefa["concluida"] = True
            salvar_tarefas(tarefas)
            print("Tarefa concluída!")


    else:
        print("Tarefa inexistente!")


def excluir_tarefa(tarefas):
    if not tarefas:
        print("Nenhuma tarefa cadastrada!")
        return

    listar_tarefas(tarefas)

    try:
        numero = int(input("Número da tarefa para excluir: "))
    except ValueError:
        print("Digite um número válido!")
        return

    if 1 <= numero <= len(tarefas):
        tarefa_excluida = tarefas.pop(numero - 1)
        salvar_tarefas(tarefas)
        print("Tarefa excluída:", tarefa_excluida["descricao"])
    else:
        print("Tarefa inexistente!")

def editar_tarefa(tarefas):
    if not tarefas:
        print("Nenhuma tarefa cadastrada!")
        return

    listar_tarefas(tarefas)

    try:
        numero = int(input("Digite o numero da tarefa a editar?"))
    except ValueError:
        print("Digite um número válido!")
        return

    if 1 <= numero <= len(tarefas):

        nova_tarefa = input("Digite o nome da nova tarefa: ").strip()

        if not nova_tarefa:
            print("Erro! Digite uma nova tarefa")
            return

        tarefas[numero - 1]["descricao"] = nova_tarefa

        salvar_tarefas(tarefas)
        print("Tarefa edida com sucesso!")


    else:
        print("Tarefa não encontrada!")


tarefas = carregar_tarefas()
opcao = 0

while opcao != 5:
    print("\n===== GERENCIADOR DE TAREFAS =====")
    print("1 - Adicionar tarefa")
    print("2 - Listar tarefas")
    print("3 - Concluir tarefa")
    print("4 - Excluir tarefa")
    print("5 - Sair")
    print("6 - Editar tarefa")

    try:
        opcao = int(input("Digite sua opção: "))
    except ValueError:
        print("Erro! Digite uma opção numérica.")
        continue

    if opcao == 1:
        adicionar_tarefa(tarefas)

    elif opcao == 2:
        print("===== MINHAS TAREFAS =====")
        listar_tarefas(tarefas)

    elif opcao == 3:
        concluir_tarefa(tarefas)

    elif opcao == 4:
        excluir_tarefa(tarefas)

    elif opcao == 5:
        print("Encerrando programa!")

    elif opcao == 6:
        editar_tarefa(tarefas)

    else:
        print("Opção inválida!")
