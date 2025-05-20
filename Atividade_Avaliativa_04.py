
# A dupla sao <Kaio Brandao || Edson Abade>

import os
import time
from dataclasses import dataclass

os.system("cls" if os.name == "nt" else "clear")

@dataclass
class Funcionario:
    nome: str
    cpf: str
    data_nascimento: str
    funcao: str

def verificar_lista_vazia(lista):
    if not lista:
        print("\nA lista está vazia.")
        return True
    return False

def adicionar(lista):
    print("= Digite os dados do funcionário = ")
    funcionario = Funcionario(
        nome=input("Nome: "),
        cpf=input("CPF: "),
        data_nascimento=input("Data de nascimento: "),
        funcao=input("Função: ")
    )
    lista.append(funcionario)
    print("Funcionário adicionado com sucesso.")

def mostrar(lista):
    if verificar_lista_vazia(lista):
        return

    print("\n = Lista de Funcionários =")
    for i, funcionario in enumerate(lista, 1):
        print(f"{i}. Nome: {funcionario.nome}, CPF: {funcionario.cpf}, Nascimento: {funcionario.data_nascimento}, Função: {funcionario.funcao}")

def atualizar(lista):
    if verificar_lista_vazia(lista):
        return

    mostrar(lista)
    cpf_alvo = input("Digite o CPF do funcionário a ser atualizado: ")

    for i, funcionario in enumerate(lista):
        if funcionario.cpf == cpf_alvo:
            print(f"Atualizando dados de {funcionario.nome}")
            lista[i] = Funcionario(
                nome=input("Novo nome: "),
                cpf=cpf_alvo,  # Mantém o mesmo CPF
                data_nascimento=input("Nova data de nascimento: "),
                funcao=input("Nova função: ")
            )
            print("Funcionário atualizado com sucesso!")
            return

    print("Funcionário com o CPF informado não foi encontrado.")

def excluir(lista):
    if verificar_lista_vazia(lista):
        return

    mostrar(lista)
    cpf_remover = input("Digite o CPF do funcionário que deseja remover: ")

    for funcionario in lista:
        if funcionario.cpf == cpf_remover:
            lista.remove(funcionario)
            print(f"Funcionário {funcionario.nome} removido com sucesso!")
            return

    print("Funcionário com o CPF informado não foi encontrado.")

# Lista principal
lista_funcionarios = []

while True:
    print("= Gerenciador de Funcionários =")
    print("1 - Adicionar")
    print("2 - Listar Funcionários")
    print("3 - Atualizar")
    print("4 - Excluir")
    print("5 - Sair")

    try:
        opcao = int(input("Digite uma das opções: "))
    except ValueError:
        print("Por favor, digite um número válido.")
        time.sleep(2)
        os.system("cls" if os.name == "nt" else "clear")
        continue

    match opcao:
        case 1:
            adicionar(lista_funcionarios)
        case 2:
            mostrar(lista_funcionarios)
        case 3:
            atualizar(lista_funcionarios)
        case 4:
            excluir(lista_funcionarios)
        case 5:
            print("\nSaindo do programa...")
            break
        case _:
            print("\nOpção inválida. Tente novamente.")
    
    if opcao != 5:
        time.sleep(2)
        os.system("cls" if os.name == "nt" else "clear")