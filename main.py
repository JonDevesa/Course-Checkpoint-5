print('Ejercicio 1: Cree un bucle For de Python.')
for numero in range(0, 11):  # El rango va de 0 a 10
    print(numero + 1)  # Imprime el número de la iteración actual más 1
print()

print('Ejercicio 2: Cree una función de Python llamada suma que tome 3 argumentos y devuelva la suma de los 3.')
def suma(x, y, z):
    return x + y + z
resultado = suma(1, 2, 3)
print(resultado)
print()

print('Ejercicio 3: Cree una función lambda con la misma funcionalidad que la función de suma que acaba de crear.')
suma = lambda x, y, z: x + y + z
resultado = suma(33, 67, 0)
print(resultado)
print()

print('Ejercicio 4: Utilizando la siguiente lista y variable, determine si el valor de la variable coincide o no con un valor de la lista. *Sugerencia, si es necesario, utilice un bucle for in y el operador in.')
nombre = 'Enrique'
lista_nombre = 'Jessica', 'Paul', 'George', 'Henry', 'Adán'
if nombre in lista_nombre:
    print('El nombre está en la lista.')
else:
    print('El nombre no está la lista.')
print()