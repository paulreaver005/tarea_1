#se crearon dos variables de tipo string, una con el numero pi y otra con los asteriscos.
#se itera un rango por medio de un for loop y se utiliza el % para imprimir en pantalla el formato
#el for loop itera normal para el numero pi a la inversa para los asteriscos así se logra dar con el formato requerido


pi = "3.14159265359"
ast = "************"

for x in range(4,11):
     print("%s" % ast[:x.__invert__()],pi[:x])

