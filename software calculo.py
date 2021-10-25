

cadena='MOTOR DE HERON: Aplasta latas'
print(cadena.center(70, "="))

vr1=input('¿Qué desea averiguar? Ingrese el número de la operación indicada\n\n1-Cuantas latas puedo aplastar con una cantidad de Litros conocida\n2-Cuanta agua requiero para aplastar una cantidad de Latas conocida\nIngrese aquí la opcion: ')
print('======================================================================')

while vr1=='1' or vr1=='2':
    if vr1=='1':
        Agua=float(input('Ingrese la cantidad de agua que desee añadir al motor. El máximo a añadir es de 4 Litros: '))

        while Agua>4:
            print('Usted ha ingresado una cantidad de agua que sobrepasa el límite')
            Agua=float(input('Por favor, ingrese nuevamente la cantidad de agua que quiere ingresar al motor: '))

        latas=(Agua*50)
        tiempo=(latas/50)*60
        cadena='RESULTADO'
        print(cadena.center(70, "="))
        print(f'Con un total de {Agua}litros, la cantidad de latas que serán aplastadas es de un total de {latas}, y esto será en un tiempo de {tiempo} minutos')
        print('======================================================================')

    if vr1=='2':
        latas=int(input('Ingrese la cantidad de latas que quiere aplastar: '))
        Agua=latas/50
        tiempo=Agua*60
        cadena='RESULTADO'
        print(cadena.center(70, "="))
        print(f'La cantidad de agua que se requiere para aplastar {latas} cantidad de latas es de {Agua} litros. Esto tomará un total de {tiempo} minutos.')
        print('======================================================================')
    
    vr1=input('¿Desea volver a realizar el proceso? En el caso de ser así, ingrese la modalidad que quiera ejecutar. Recuerde que:\n0-Deseo terminar el proceso\n1-Cuantas latas se aplastan con una cantidad de Litros conocida\n2-Cuanta agua requiere el motor para aplastar una cantidad de Latas conocida\nIngrese aquí la opcion:  ')

if vr1==0 or vr1.lower=='salir':
    print('El programa ha finalizado exitosamente')
else:
    print('Usted ha ingresado una opción que no es válida. Por favor, ejecute nuevamente el programa')