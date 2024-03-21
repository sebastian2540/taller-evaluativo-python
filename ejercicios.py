#Ejercicio 1
#Solicitar al usuario las horas trabajadas, teniendo en cuenta que la jornada es de 42 horas y valor hora es de 33000. Calcular el salario del trabajador teniendo en cuenta si este excede la jornada y trabaja horas extras o si por el contrario no excede la jornada de trabajo.

horas_trabajadas = float(input("Ingresa las horas trababajas: "))
jornada = 42
valor_hora = 33000


salario_normal = min(horas_trabajadas, jornada) * valor_hora #Calculo del salario normal del trabajador

if horas_trabajadas > jornada:
    horas_extras = horas_trabajadas - jornada #Calculo de horas extras
    pago_horas_extras = horas_extras * valor_hora * 1.5 #Calculo del pago de las horas extras
    salario_total = salario_normal + pago_horas_extras #Sumar el pago por hora extras al salario normal
else:
    salario_total = salario_normal

print(f"El salario del trabajador es: {salario_total}")

#Ejercicio 2
#Solicitar al usuario un número y validar si este es número primo. (usar ciclos si es necesario)

numero = int(input("Ingresar un numero: "))

if numero <= 1:
    print("Ingrese un número mayor que 1")
else:
    primo = True
    for i in range(2, numero):
        if numero % i == 0:
            primo = False
            break
    
    if primo:
        print(f"{numero} es un número primo")
    else:
        print(f"{numero} no es un número primo")

#Ejercicio 3
#Solicitar el ingreso de 2 nombres, validar si los nombres ingresados tienen la misma longitud, comienzan con la misma letra si es así el programa debe mostrar los nombres comienzan con la misma letra y la longitud de estos. De lo contrario debe mostrar un mensaje indicando que no coinciden.

nombre_uno = input("1. Ingrese un nombre: ")
nombre_dos = input("2. Ingrese un nombre: ")

if len(nombre_uno) == len(nombre_dos):
    if nombre_uno[0] == nombre_dos[0]:
        print(f"Los nombre {nombre_uno} y {nombre_dos} tienen la misma longitud y comienzan con la letra {nombre_uno[0]}")
    else:
        print(f"Los nombre {nombre_uno} y {nombre_dos} tienen la misma longitud pero no comienza con la misma letra {nombre_uno[0]}")
else:
    print(f"Los nombre {nombre_uno} y {nombre_dos} no coinciden")
         
#Ejercicio 4
#Adivina el número: Escribe un programa que genere un número aleatorio entre 1 y 100(importar librería random), y que le pida al usuario adivinarlo. El programa debe indicar si el número ingresado por el usuario es mayor, menor o igual al número generado. El usuario debe tener 3 intentos para adivinar el número. Ejem: aleatorio = random.randint(1,100)

import random
numero_aleatorio = random.randint(1,100)
print(numero_aleatorio)
contador_intentos = 3

while contador_intentos > 0:
    adivina_numero = int(input("Adivina el número entre el 1 y 100: "))

    if adivina_numero == numero_aleatorio:
        print(f"Has adivinado el número {numero_aleatorio}")
        break
    elif adivina_numero < numero_aleatorio:
        print("Demaciado bajo, intenta nuevamente")
    else:
        print("Demaciado alto, intenta nuevamente")

    contador_intentos -= 1

if contador_intentos == 0:
    print(f"Intentos terminados, el numero aleatorio era {numero_aleatorio}")

#Ejercicio 5
#Solicitar al usuario cuánto dinero quiere ingresar al CDT y cuánto tiempo (este debe ser mayor a 3 meses (90 días) y menor a 2 años (720 días)). Si el ahorro es por 90 días los intereses serán 3.14% de lo ahorrado, si esta entre 91 y 180 días el interés es 4.85% y si es entre 181 a 360 días los intereses son de 5.75%. mostrar cuanto ganaría el usuario según el plazo aplicado al CDT.

continuar = 's'
while continuar.lower() == 's':
    dinero = float(input("Ingrese la cantidad de dinero a invertir en el CDT: "))
    tiempo_dias = int(input("Ingrese el tiempo de inversión en días (mayor a 90 días y menor a 720 días): "))

    if 90 <= tiempo_dias <= 180:
        tasa_interes = 0.0314
    elif 181 <= tiempo_dias <= 360:
        tasa_interes = 0.0485
    else:
        tasa_interes = 0.0575

    interes_ganado = dinero * tiempo_dias * tasa_interes / 360
    print(f"El interés ganado en el CDR sería de: {interes_ganado}")

    continuar = input("¿Desea continuar? (s/n): ")

#Ejericicio 6
#Crea una lista vacía llamada departamentos Colombia, pida al usuario la cantidad de departamentos a ingresar, a través de un ciclo for pida al usuario que ingrese el departamento de Colombia que desee, agregue esta información a la lista y luego esta sea ordenada en orden descendente. a. Se debe imprimir la lista con los valores organizados de forma descendentes. b. Debe imprimir además los 2 últimos departamentos ingresados

departamentos_colombia = []
cantidad_departamentos = int(input("Ingrese la cantidad de departamentos a ingresar: "))

for i in range (cantidad_departamentos):
    departamento = input(f"Ingrese el nombre del departamento {i + 1} de Colombia: ")
    departamentos_colombia.append(departamento)

print("\nLos 2 ultimos departamentos ingresados son: ", departamentos_colombia[-2:])
for departamento in departamentos_colombia[-2:]:
    print(departamento)

departamentos_colombia.sort(reverse=True)

print("\nLista de departamentos de Colombia en orden descendente: ") 
for departamento in departamentos_colombia:
    print(departamento)