#Reto Semana 6
contador= 0
while contador < 3: 
    pass_word = input("Ingrese una contraseña: ")
    primer_caracter = pass_word[0]
    if not primer_caracter.isnumeric():
        print("La contraseña debe ingresar con un número ")

        contador += 1
    else:
         break   
while contador < 3 :
        pass_word_2 = input("Ingrese la contraseña nuevamente: ")
        if pass_word == pass_word_2:
            print("Contraseña correcta ")
            exit()
else:
        print("Las contraseñas no coinciden ")
        contador += 1

