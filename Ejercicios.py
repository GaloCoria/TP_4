#Ejercicio 1
#for  x in range(1,101):
  #  print(x)
   # x=x+1

#Ejercicio 2
''' numero=int(input("Ingrese un numero entero:"))
digito=0

if numero ==0:
     digito=1

while  numero>0 :
     
     numero=numero//10
    
     digito=digito+1

print(digito)  ''' 

#Ejercicio 3
'''numero1=int(input("Ingrese un numero entero:"))
numero2=int(input("Ingrese otro numero:"))
suma=0
if numero1 > numero2:
    numero1, numero2 = numero2, numero1

while numero1 < numero2 - 1:
    numero1 += 1
    suma += numero1

print(suma) ''' 

#Ejercicio 4
''' numero=int(input("Ingrese un numero:"))
suma=numero
while numero!=0:
    numero=int(input("Ingrese un numero:"))
    suma+=numero

print(suma)'''

#Ejercicio 5
''' from random import *
random=randint(0,9)
numero=int(input("Ingrese un numero del 0 a 9:"))
intentos=1
while numero!= random :
    numero=int(input("Ingrese un numero:"))
    intentos=intentos+1

print(f"Antes de adivinar el numero lo intento:{intentos} ") '''
#Ejercicio 6
'''for x in range(100,-1,-2):
    print(x) '''

#Ejercicio 7
'''numero=int(input("Ingrese un numero entero positivo:"))
suma=numero
for x in range(0,numero):
    suma+=x
print(suma) '''
#Ejercicio 8
'''cantidad=0
numpar=0
numimpar=0
numpositivo=0
numnegativo=0
while cantidad!=100:
    numero=int(input("Ingresa un Numero Entero:"))
    cantidad+=1
    if numero %2==0:
        numpar+=1
    else: 
        numimpar+=1
    if numero >= 0 :
        numpositivo+=1
    else:
        numnegativo+=1

print(f"La cantidad de numeros pares es : {numpar}, la cantidad de numeros impares son : {numimpar}, la cantidad de numeros positivos son : {numpositivo} y la cantidad de numeros negativos son: {numnegativo}")'''

#Ejercicio 9
'''cantidad=0
suma=0
while cantidad !=2 :
    numero=int(input("Ingresa un Numero Entero:"))
    cantidad+=1
    suma+=numero
promedio=suma/cantidad
print(f"El promedio de todos los numeros es: {promedio}") '''
#Ejercicio 10
numero = int(input("Ingresa un número entero: "))
invertido = 0

while numero > 0:
    digito = numero % 10
    invertido = invertido * 10 + digito
    numero //= 10

print("El número invertido es:", invertido)

