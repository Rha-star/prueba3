print ('Hola, debes adivinar el numero oculto, tienes tres intentos')


#se declara i "contador en 0" y un "acumulador para la cantidad de intentos"
i=0
acum=0
#Se crea el ciclo FOR
numero_secreto=3
acertado = False

for i in range(3):
    numero=int(input('Ingresa un número '))
    if numero == numero_secreto:
        print('FELICIDADES! el numero es correcto')
        acertado = True
        break  #esto se usa para cerrar un ciclo
else:
    print('Lo siento, no acertaste ')
#Si no acerta el numero se muestra el siguiente mensaje

if not acertado:
    print(f'Lo siento, el numero era, {numero_secreto}.')