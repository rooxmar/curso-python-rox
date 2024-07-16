#Reto semana 5
current_year = int(input("Introduce el año actual: "))
another_year = int(input("Introduce un año distinto al actual: "))
difference = current_year - another_year 
difference_positive = difference * -1


if difference ==1:# <- condicion estricta siempre van arriba para que cumpla primero
    print(f"Desde el año {another_year} ha pasado un año")
elif difference_positive ==1:
    print(f"Para llegar al año {current_year} hace falto 1 año")
elif current_year < another_year:
    print(f"Faltan por pasar {difference_positive} años para llegar al año que has introducido")
elif current_year > another_year:
    print(f"Han pasado {difference} años desde el año que introduciste")
elif current_year == another_year:
    print(f"Has introducido el mismo año que el actual") 