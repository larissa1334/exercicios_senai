nome=input('qual e o seu nome?')
idade=int (input('qual e a sua idade?'))
if idade >= 18:
    print('maior de idade')
else :
    print ('menor de idade')


carteira=(input('possui carteiera de motorista? (1-sim,/ 2-não)'))
if carteira == 1:
    idade=(input('maior de idade'))
if idade>= 18:
   print('pode dirigir...')
else:
    print('nao pode dirigir!')

    