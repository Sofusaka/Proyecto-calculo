

cadena='MOTOR DE HERON: Aplasta latas'
print(cadena.center(70, "="))
#En esta seccion se da inico a la simulacion, imprimiendo un titulo por pantalla para mayor comodidad del usuario.
#se define el nombre del programa por medio de la variable cadena, y con ayuda de la funcion center 
# se puede centrar el titulo e imprimir lineas delimitadoras

vr1=input('¿Qué desea averiguar? Ingrese el número de la operación indicada\n\n1-Cuantas latas puedo aplastar con una cantidad de Litros conocida\n\n2-Cuanta agua requiero para aplastar una cantidad de Latas conocida\n\nIngrese aquí la opcion: ')
print('======================================================================')

#En este momento, se crea una variable control para un menú de opciones. Dependiendo de la opcion que escoja el usuario, el programa realizará una serie de operaciones. 
#En esta situación, determinamos el número 1 como la opción para averiguar  la cantidad de latas a partir de ciertos litros de agua
#Por otro lado, el número 2 fue asignado para hallar la cantidad de agua  que requiere el motor 


while vr1=='1' or vr1=='2':
#Por medio de una sentencia while se crea un control, por si el usuario digita un valor diferente a 1 o 2, se le dará un mensaje de error y tendrá que volver a ejecutar el programa
    
    if vr1=='1':
        Agua=float(input('Ingrese la cantidad de agua que desee añadir al motor. El máximo a añadir es de 4 Litros: '))
        #En el caso de que el usuario haya seleccionado la opcion 1, este tendra que digitar la cantidad de agua que desea añadirle al motor
        
        while Agua>4:
            print('Usted ha ingresado una cantidad de agua que sobrepasa el límite')
            Agua=float(input('Por favor, ingrese nuevamente la cantidad de agua que quiere ingresar al motor: '))
        #Si el agua sobrepasa el limite de 4 litros definidos, el programa le pedira que ingrese nuevamente la cantidad de agua.

        latas=(Agua*150)     
        tiempo=(latas/150)*60
    
        #Se realizan las operaciones respectivas para averiguar la cantidad de latas que serán aplastadas, y la cantidad de minutos que esta accion requiere
        cadena='RESULTADO'
        print(cadena.center(70, "="))
        print(f'Con un total de {Agua}litros, la cantidad de latas que serán aplastadas es de un total de {latas}, y esto será en un tiempo de {tiempo} minutos')
        print('======================================================================')
        #se imprime el resultado de esta operación


    if vr1=='2':
        latas=int(input('Ingrese la cantidad de latas que quiere aplastar. El límite es 600: '))
        #En el caso de que el usuario haya seleccionado la opcion 2, este tendra que digitar la cantidad de latas que desea que el motor aplaste
        while latas>600:
            print('Usted ha ingresado una cantidad de latas que sobrepasa el límite')
            Agua=int(input('Por favor, ingrese nuevamente la cantidad de latas que quiere ingresar al motor: '))
        #Si las latas sobrepasan el limite de 200, el programa entrará en un loop hasta que se digite una cantidad aceptada
        Agua=latas/150
        tiempo=Agua*60
        #Se realizan las operaciones respectivas para averiguar la cantidad de litros de agua que se requieren para aplastar 
        #las latas anteriormente definidas, y la cantidad de minutos que esta accion requiere

        cadena='RESULTADO'
        print(cadena.center(70, "="))
        print(f'La cantidad de agua que se requiere para aplastar {latas} latas es de {Agua} litros. Esto tomará un total de {tiempo} minutos.')
        print('======================================================================')
        #se imprime el resultado de esta operación

    vr1=input('¿Desea volver a realizar el proceso? En el caso de ser así, ingrese la modalidad que quiera ejecutar. Recuerde que:\n\n0-Deseo terminar el proceso\n\n1-Cuantas latas se aplastan con una cantidad de Litros conocida\n\n2-Cuanta agua requiere el motor para aplastar una cantidad de Latas conocida\n\n\nIngrese aquí la opcion:  ')
        #En el caso de que el usuario quiera volver a realizar toda la operacion de nuevo,
        #tiene la posibilidad de realizarlo escogiendo una opcion del menu anteriormente definido
        #Si desea salir de la operacion, simplemente escribe la letra 0
        

if vr1=='0' or vr1.lower=='salir':
    print('La simulación del motor HERON ha finalizado exitosamente')
    #Aqui se le da por finalizado al programa
else:
    print('Usted ha ingresado una opción que no es válida. Por favor, ejecute nuevamente el programa')
    #En esta situacion, es el mensaje de error planteado anteriormente