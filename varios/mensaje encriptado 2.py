mensaje_a_traducir1 = ".... . -- --- ... / . -. -.-. --- -. - .-. .- -.. --- / ..- -. .- / .--. .-.. .- -. - .- / -. ..- -. -.-. .- / .- -. - . ... / ...- .. ... - .-" #Hemos encontrado una planta nunca antes vista
mensaje_a_traducir2 = "-. --- ... / .... .- -. / .--. .. -.-. .- -.. --- / -.. --- ... / -- --- ... --.- ..- .. - --- ..." ##Nos han picado dos mosquitos
mensaje_a_traducir3 = "- . -. . -- --- ... / -.-. --- -- .. -.. .- / .--. .- .-. .- / - .-. . ... / -.. .. .- ... / -- .- ..." ##Tenemos comida para tres dias mas


def traducir_a_espanol(mensaje_a_traducir):

    morse = {'/':' ' ,'.-': 'A', '-...':'B','-.-.': 'C', '-..':'D','.': 'E' ,   ##Diccionario para comparar las letras en codigo morse y en el alfabeto español
         '..-.':'F','--.': 'G', '....':'H', '..':'I','.---': 'J', '-.-':'K',
         '.-..':'L', '--': 'M', '-.':'N','---': 'O', '.--.': 'P','--.-': 'Q',
         '.-.': 'R', '...': 'S','-': 'T' , '..-': 'U','...-': 'V',  '.--':'W',
         '-..-':'X' ,'-.--':'Y' , '--..':'Z' }

    mensaje = mensaje_a_traducir.split()  ##Separamos cada letra de la frase ingresada y las guardamos en una lista, donde cada letra es un elemento de la lista ej: entrada: mensaje = "casa", mensaje.split(); salida: ["c","a","s","a"]
    #for i in range(len(mensaje)): 
        #mensaje_traducido = mensaje_traducido + morse[mensaje[i]]

    mensaje_traducido = "" ##Icializamos un contador con una lista vacía, aquí guardaremos nuestra mensaje traducido
    for j in mensaje: ##ciclo para recorrer cada elemento de la lista y traducirlo al alfabelto español
        mensaje_traducido = mensaje_traducido + morse[j]

    return mensaje_traducido  ##Devuelve el mensaje traducido 

mensaje_traducido1 = traducir_a_espanol(mensaje_a_traducir1)
mensaje_traducido2 = traducir_a_espanol(mensaje_a_traducir2)
mensaje_traducido3 = traducir_a_espanol(mensaje_a_traducir3)

print(mensaje_traducido1)
print(mensaje_traducido2)
print(mensaje_traducido3)
