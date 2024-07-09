#PEDIR DATOS AL USUARIO

nombre = input("Introduce nombre: ")
apellido = input("Introduce apellido paterno: ")
apellido = input("Introduce apellido materno:")
edad = int(input("Introduce tu edad en años: "))
altura = float(input("Introduce tu altura en metros: "))
masa = float(input("Introduce tu masa en kilogramos: "))
IMC = masa/altura **2
print("IMC:" + str(IMC))

if IMC >= 0 and IMC <= 15.99 :
    print("Bajo de peso severo")
elif IMC >= 16.00 and IMC <18.00:
     print("Bajo de peso")
elif IMC >=18.1 and IMC <24.99:
      print("Peso normal")
elif IMC >=25.00 and IMC <29.99:
      print("Sobrepeso")
elif IMC >=30.00 and IMC <34.99:
     print("Obesidad clase 1")
elif IMC >= 35.00 and IMC <39.99:
     print("Obesidad clase 2")
elif IMC >=40.00 and IMC :
     print("Obesidad clase 2")