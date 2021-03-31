from modulos import Deposito, Saque, Consult

print("-=+=-"*8)
print("Bem vindo ao Banco Blue !")
print("-=+=-"*8)
nome = input("Digite seu nome:\n")
print("-=+=-"*8)
senha = input("Digite sua senha:\n")
while len(senha) < 6:
    senha = input("Digite uma senha com no mínimo 6 digitos:\n")
endereco = input("Digite seu endereço:\n")
idade = int(input("Digite sua idade:\n"))
saldo = 1000.0

opcao = 0

while True:
    opcao = int(input("Digite [1] para DEPÓSITO, [2] para SAQUE, [3] para CONSULTA DE SALDO e [4] para SAIR:\n"))
    print("-=+=-"*8)
    if opcao == 1:
        deposito = float(input("Digite o valor para depósito:\n"))
        saldo = Deposito(saldo, deposito) #Chamando modulo Depósito
        print("-=+=-"*8)
    elif opcao == 2 and saldo > 1:
        saque = float(input("Digite o valor para saque:\n"))
        print("-=+=-"*8)
        if saque > saldo:
            print("Saldo insuficiente para saque, saldo atual é : {}".format(saldo))
            print("-=+=-"*8)
        else: saldo = Saque(saldo, saque) #Chamando modulo Saque
    elif opcao == 3:
        Consult(saldo) #Chamando modulo Consulta
        print("-=+=-"*8)
    elif opcao == 4:
        print("Okay, saindo desta tela.")
        print("-=+=-"*8)
        break
    else: print("Digite um comando correto.\n ", "-=+=-"*8)

cadUser = [nome, endereco, idade, saldo, senha]
opcao = int(input("Deseja continuar? Sim [1] ou Não [2]\n"))
print("-=+=-"*8)
if opcao == 1:
    print("Certo, vamos imprimir seus dados:")
    print("-=+=-"*8)        
    print(cadUser[:2])
    print("-=+=-"*8)
    opcao = int(input("Deseja continuar? Não[1], Sim [2]\n"))
    print("-=+=-"*8)
if opcao == 2:
    opcao = int(input("Deseja alterar seus dados? Sim [1] ou Não [2]\n"))
    print("-=+=-"*8)
    if opcao == 1:
        while True:
            opcao = int(input("Qual dado alterar? [0] Nome, [1] Endereço, [2] Idade?, [99] SAIR\n"))
            if opcao == 99:
                print("Certinho, finalizando o programa. O Blue Bank te deseja um ótimo dia !")
                print("-=+=-"*8)
                break
            print("-=+=-"*8)
            cadUser[opcao] = input("Digite o dado para alteração.\n")
            print("-=+=-"*8)
            print(cadUser[:2])
            print("-=+=-"*8)
    elif opcao == 2:
        print("Certinho, finalizando o programa. O Blue Bank te deseja um ótimo dia !")
        print("-=+=-"*8)
    else: print("Programa sendo finalizado, uma opção desconhecida foi teclada. O Blue Bank te deseja um ótimo dia !")




    