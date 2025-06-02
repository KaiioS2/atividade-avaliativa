# Aluno Kaio
import os


biblioteca = []

def adicionar_livro():
    titulo = input("Digite o título do livro: ")
    autor = input("Digite o autor do livro: ")
    livro = {'titulo': titulo, 'autor': autor}
    biblioteca.append(livro)
    print(f'Livro "{titulo}" adicionado.')

def remover_livro():
    titulo = input("Digite o título do livro a remover: ")
    global biblioteca
    biblioteca = [livro for livro in biblioteca if livro['titulo'].lower() != titulo.lower()]
    print(f'Livro "{titulo}" removido, se estava na biblioteca.')

def listar_livros():
    if not biblioteca:
        print("A biblioteca está vazia.")
    else:
        print("Livros na biblioteca:")
        for i, livro in enumerate(biblioteca, 1):
            print(f"{i}. {livro['titulo']} - {livro['autor']}")

def salvar_em_txt():
    nome_arquivo = input("Digite o nome do arquivo para salvar (ex: biblioteca.txt): ")
    with open(nome_arquivo, 'w', encoding='utf-8') as arquivo:
        for livro in biblioteca:
            arquivo.write(f"{livro['titulo']} - {livro['autor']}\n")
    print(f'Biblioteca salva em "{nome_arquivo}".')

def menu():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("\nMenu Biblioteca:")
        print("1. Adicionar livro")
        print("2. Remover livro")
        print("3. Listar livros")
        print("4. Salvar biblioteca em arquivo txt")
        print("5. Sair")
        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            adicionar_livro()
        elif escolha == '2':
            remover_livro()
        elif escolha == '3':
            listar_livros()
        elif escolha == '4':
            salvar_em_txt()
        elif escolha == '5':
            print("Saindo...")
            break
        else:
            print("Opção inválida, tente novamente.")
        input("\nPressione Enter para continuar...")

menu()