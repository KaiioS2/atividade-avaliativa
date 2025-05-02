import os
os.system("cls || clear")


def calcular_inss(salario):
    if salario <= 1518.00:
        return salario * 0.075
    elif salario <= 2793.88:
        return salario * 0.09 - 113.85
    elif salario <= 4190.83:
        return salario * 0.12 - 189.54
    elif salario <= 8157.41:
        return salario * 0.14 - 318.38
    else:
        return 1142.04  # desconto máximo

def calcular_irrf(salario, dependentes):
    deducao_dependentes = dependentes * 189.59
    base_calculo = salario - deducao_dependentes

    if base_calculo <= 2259.20:
        return 0
    elif base_calculo <= 2826.65:
        return base_calculo * 0.075 - 169.44
    elif base_calculo <= 3751.05:
        return base_calculo * 0.15 - 381.44
    elif base_calculo <= 4664.68:
        return base_calculo * 0.225 - 662.77
    else:
        return base_calculo * 0.275 - 896.00

def main():
    # Autenticação
    matricula = input("Digite a matrícula do funcionário: ")
    senha = input("Digite a senha: ")

    # Dados de entrada
    salario_base = float(input("Digite o salário base (R$): "))
    vt_opcao = input("Deseja receber vale transporte? (s/n): ").strip().lower() == 's'
    vale_refeicao = float(input("Digite o valor do vale refeição fornecido pela empresa (R$): "))
    dependentes = int(input("Digite a quantidade de dependentes: "))

    # Cálculo dos descontos
    inss = calcular_inss(salario_base)
    irrf = calcular_irrf(salario_base - inss, dependentes)
    vt = salario_base * 0.06 if vt_opcao else 0
    vr = vale_refeicao * 0.20
    plano_saude = dependentes * 150.00

    # Salário líquido
    salario_liquido = salario_base - inss - irrf - vt - vr - plano_saude

    # Resultado
    print("\nResumo da Folha de Pagamento:")
    print(f"Matrícula: {matricula}")
    print(f"Salário Base: R$ {salario_base:.2f}")
    print(f"Desconto INSS: R$ {inss:.2f}")
    print(f"Desconto IRRF: R$ {irrf:.2f}")
    print(f"Desconto Vale Transporte: R$ {vt:.2f}")
    print(f"Desconto Vale Refeição: R$ {vr:.2f}")
    print(f"Desconto Plano de Saúde: R$ {plano_saude:.2f}")
    print(f"Salário Líquido: R$ {salario_liquido:.2f}")

if __name__ == "__main__":
    main()