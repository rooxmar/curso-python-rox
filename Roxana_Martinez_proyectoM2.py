# Vamos medir la longitud de una frase

word = input("Introduce una palabra: ")
length = len(word)

if length >= 4 and length <= 8:
    print("La palabra es correcta")
elif length < 4:
    print(f"Hacen falta letras. Solo tiene {length} letras")
elif length > 8:
    print(f"Sobran letras. Tiene {length} letras")
 
########################################################################

#Encontrar un numero en el cuadrante 

numero_x = int(input("Ingresa un numero: "))
numero_y = int(input("Ingresa un segundo numero: "))

if numero_x > 0 and numero_y > 0:
    print("El punto esta en el cuadrante 2")
elif numero_x > 0 and numero_y < 0:
    print("El punto esta en el cuadrante 4")
elif numero_x < 0 and numero_y < 0:
    print("El punto esta en el cuadrante 3")
elif numero_x < 0 and numero_y > 0:
    print("El punto esta en el cuadrante 1")
elif numero_x == 0 and numero_y == 0:
    print("El numero x es cero y el numero y tambien es cero")
elif numero_x == 0:
    print("El numero x es cero")
elif numero_y == 0:
    print("El numero y es cero")