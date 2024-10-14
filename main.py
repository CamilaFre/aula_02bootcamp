#try:
#    resultado = len("Camila")
#   print(resultado)
#except TypeError as e:
#    print(e)
#else:
#    print('tudo certo')
#finally:
#    print('o importante é tentar')

numero = int(input("Insira um numero: "))

if isinstance (numero, int):
    print("A variável é um inteiro")
else:
    print("A variável não é um inteiro")

