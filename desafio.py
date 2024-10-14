

nome = input("Digite seu nome: ")

if nome.isdigit():
    print('Você digitou seu nome errado')
    exit()
elif len(nome) == 0:
    print('Voce não digitou nada')
    exit()
elif nome.isspace():
    print('Voce digitou só espaço')
    exit()
salario = float(input("Digite o valor do seu salário mensal: "))

bonus = float(input("Digite a porcentagem do bônus que você recebeu: "))


valor_do_bonus = float(1000 + salario*bonus)


print(f'Olá {nome}! O valor do seu bonus é de {valor_do_bonus} ')