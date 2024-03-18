#Vai receber os dados que foi inputado pelo usuário

num1 = int(input("Digite um numero:" ))
num2 = int(input("Digite um numero:" ))

#realizará as operações conforme o escolhido
operacao = input("Digite a operação que deseja realizar (+, -, *, /): ")

if operacao == '+':
    print(num1 + num2)
elif operacao == '-':
    print(abs(num1 - num2))    
elif operacao == '*':
    print(num1 * num2)    
elif operacao == '/':
    print(num1 / num2)

else:
    print("Operação inválida")        