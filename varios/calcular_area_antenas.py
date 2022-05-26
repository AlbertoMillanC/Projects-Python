
#programa para calcular  antenas en un area establecida, con 5 tipos de antenas en el diccionario y una cifra del area antenas actuales instaladas.
diccionario={'a': 44600,'b': 51800,'c': 9600,'d': 15300,'e': 13900}
antena_instalada= 36900
area_a_calcular=float(input("ingrese el area a calcular en metros: "))
tipo_antena=input("ingrese el tipo de antena: ")
valor = diccionario.get(tipo_antena) 

# se convierte el valor ingresado en metros con una division a numero de antenas. 
# se coloca un error si se ingresa cero, como acotación si se ingresa un cero se le suma 1 pues al convertir en enteros se pierde la fraccion sin antena. 
area_instalada_actual=(int(area_a_calcular/valor+1))
def resultado(): 
    if area_instalada_actual==1:
        print("error en los datos")
    else: 
        print(f"el numero de antenas es: {area_instalada_actual}")
    
    
antenas_final=resultado()
# resultado es el diccionario que se va a imprimir. Actual




