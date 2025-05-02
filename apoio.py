import os
os.system("cls || clear")

def calcular_inss(salario_bruto):
    if salario_bruto <= 1518.00:
        return salario_bruto * 0.075
    elif salario_bruto >= 1518.01:
        return salario_bruto * 0.09
    elif salario_bruto >= 2793.89:
        return salario_bruto * 0.12
    elif salario_bruto >= 4190.84:
        return salario_bruto * 0.14
    else:
        resultado_inss = 0
    return ()

def calcular_irrf(salario_bruto, dependentes):
    deducao_dependentes = dependentes * 189.59
    base_calculo = salario_bruto - deducao_dependentes

    if base_calculo <= 2259.20:
        return 0
    elif base_calculo >= 2826.65:
        return base_calculo * 0.075 - 169.44
    elif base_calculo >= 3751.05:
        return base_calculo * 0.15 - 381.44
    elif base_calculo >= 4664.68:
        return base_calculo * 0.225 - 662.77
    else:
        return base_calculo * 0.275 - 896.00


Usuario = "Kaiio"
senha = 1221

Matricula = input("Digite o seu Usuario: ")
Matricula_senha = int(input("Digite sua senha: "))
salario_bruto = float(input("Digite seu salario: "))
quant_dependentes = int(input("Digite a quantidade de dependentes: "))
desejo_vale_transporte = str(input("Deseja add vale transporte S ou N ? ")).strip().lower() == "s"
vale_refeiçao = int(input("Quanto voçe recebe de vale refeiçao: "))

inss = calcular_inss(salario_bruto)
irrf = calcular_irrf(salario_bruto - inss, quant_dependentes)
resultado_vale_transporte = salario_bruto * 0.06 if desejo_vale_transporte else 0
result_vale = vale_refeiçao * 0.20

salario_liquido = salario_bruto - inss - irrf - result_vale - resultado_vale_transporte

print("\nResumo da Folha de Pagamento:")
print(f"Matrícula: {Usuario}")
print(f"Salário Base: R$ {salario_bruto:.2f}")
print(f"Desconto INSS: R$ {inss:.2f}")
print(f"Desconto IRRF: R$ {irrf:.2f}")
print(f"Desconto Vale Transporte: R$ {resultado_vale_transporte:.2f}")
print(f"Desconto Vale Refeição: R$ {result_vale:.2f}")
print(f"Salário Líquido: R$ {salario_liquido:.2f}")