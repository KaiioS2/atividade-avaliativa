import os
os.system("cls || clear")
salario_bruto = 1518
vale_refeiçao = int(input("Quanto voçe recebe de vale refeiçao: "))
result_vale = vale_refeiçao * 0.20
result_vale_refeiçao = salario_bruto - result_vale

print(result_vale)