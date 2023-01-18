# Escribir dos funciones, una función que reciba un número entero positivo n y calcule el número de
# fibonacci asociado a ese número de manera recursiva y otra función que haga la misma operación pero
# con bucles. Con ambas funciones, calcular y comparar el tiempo de ejecución para n = (1, 10, 20, 30
# y 40) por fuerza bruta.

import datetime

def fibonacci(n):
   """Función que recibe un número entero positivo 'n' y calcula el número de fibonacci asociado a ese número de manera
   recursiva
   """
   if n == 0:
       return 0
   elif n == 1:
       return 1
   else:
       return (fibonacci(n-1) + fibonacci(n-2))

start_time = datetime.datetime.now()

fibonacci(n)

end_time = datetime.datetime.now()
print("El tiempo de ejecucción es: ", end_time - start_time)