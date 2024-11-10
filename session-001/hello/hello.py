# importar depencias externas
# análogo al 
#    import de java / javascript
#     #include en C/C++
#     include/require de PHP
from print_color import print

a = 5
b = 2
c = a + b
name = "Result"
# interpolación de variables agregar f
print (f"Hello c = {c}")

# sustitución tipo las funciones printf
print ("Hello %s = %d" % (name, c))

# imprimir en color
# requiere la lib color
print("Hello world", color='red', background='green')
