#bingo crear uun programa para un lugar de azar

import random
def nueva_balota():
    letras = ['B','I','N','G','O']
    randomletras = random.randint(0,4)
    numeros = range(1,51)
    randomnumeros = random.randint(0,49)
    print((letras[randomletras]) + "-" + str(numeros[randomnumeros]))

nueva_balota()#llamamos a la funcion
while True:
   print ("Nueva balota: s/n ?")
   balota = input ("")

   if balota =='s':
     nueva_balota() #se vuelve a llamar 
   else:
     print ('************fin del juego***********') 
     break
