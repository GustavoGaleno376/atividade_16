# Crie um programa que receba o peso e a altura de uma pessoa e calcule o Índice de Massa Corporal (IMC). O programa deve classificar o IMC da pessoa de acordo com a tabela a seguir:
altura=float(input("escreva seu altura"))
peso=float(input("escreva seu peso"))
# Abaixo do peso: IMC < 18.5
imc = peso / (altura ** 2)

# Peso normal: 18.5 ≤ IMC < 25
if(18.5 <= imc < 25):
    print("você está no peso normal")
# Sobrepeso: 25 ≤ IMC < 30
elif(  25 <= imc < 30):
    print("você esta sobrepeso")
# Obesidade: IMC ≥ 30
elif(imc >= 30):
    print("você é obeso")