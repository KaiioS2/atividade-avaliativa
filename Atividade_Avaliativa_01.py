"""
Informe o número da turma: 
Turma - 97744

Nome completo dos componentes.
1 - Kaio Pinto Brandao
2 - Edson Abade Fiuza Neto
"""


import os
import time
# Limpa o terminal.
os.system("cls || clear")

valores_pratos = 0
pedido = []
total = 0
while True:
    print("""
\n========> Seja bem vindo ao Gourmet Tech <======== 
\ncodigo do prato     |     nome do prato      |     Preço 
\n      1             |  Moqueca de ovos       | 25R$
\n      2             |  Ovo pochê             | 30R$
\n      3             |  Omelete recheado      | 40R$
\n      4             |  Carbonara Tradicional | 35R$
\n      5             |  Shakshuka             | 50R$
\n      6             |  Ovo Mole              | 60R$
\n      7             |  Arroz Frito com Ovo   | 70R$
\n      0             |  ENCERRAR PEDIDO  
    """)
 
    opcao = int(input("Digite o codigo do prato: "))

    if opcao == 0:
        break   
    
    if opcao == 1:
         pedido.append("Moqueca de ovos")
         total += 25
    elif opcao == 2:
         pedido.append("Ovo pochê")
         total += 30
    elif opcao == 3:
         pedido.append("Omelete recheado")
         total += 40
    elif opcao == 4:
         pedido.append("Carbonara Tradicional")
         total += 35
    elif opcao == 5:
         pedido.append("Shakshuka")
         total += 50
    elif opcao == 6:
         pedido.append("Ovo Mole")
         total += 60
    elif opcao == 7:
         pedido.append("Arroz Frito com Ovo")
         total += 70
    else:
        print("Codigo invalido, favor solicitar outro codigo: ")
    time.sleep(0.01)
    os.system("cls || clear")

while True:
     pagamento = int(input("Pagamento ('1' A vista  ,  '2' a Cartao: "))
     if pagamento == 1:
          final_preco = total * 0.90
          break
     elif pagamento == 2:
          final_preco = total * 1.10
          break
     else:
          print("Opçao errada! escolha a forma de pagamento certo.")   



print("""
=======( Nota fiscao )=======
""")
for i in pedido:
     print(f"{i}")
print(f"Subtotal:  R${total:.2f}")
print(f"Forma de pagamento: {'A vista' if pagamento == '1' else 'Cartao'}")
print(f"Total a pagar: R${final_preco:.2f}")
print("Obrigado por escolher esse restaurante, volte sempre!")
