lista = []

alumnos = 0
while alumnos <= 6:
    opción = input("Agregar alumno (1) o terminar (2): ")
    if opción == "1":
        nombre = input ("Ingrese el nombre del alumno: ").capitalize() #-> Para que inicie con mayúscula
        calificación1 = input(f"Ingrese la primera calificación de {nombre}: ")
        calificación2 = input(f"Ingrese la segunda calificación de {nombre}: ")
        calificación3 = input(f"Ingrese la tercera calificación de {nombre}: ")
        promedio = int("calificación1" + "calificación2" + "calificación3 " / 3)
        alumno = [nombre, calificación1, calificación2, calificación3, promedio]
        lista.append(alumno)
        alumnos += 1
    elif opción == "2" :
        print(f"El programa ha terminado con {alumnos} alumnos.")
        break
    else:
        print("Se ha ingresado una opción inválida.")
        continue

print("la lista de alumnos es: ")
print(lista)