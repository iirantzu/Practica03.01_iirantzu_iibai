# Escribir dos funciones, una función que reciba un número entero positivo n y calcule el número de
# fibonacci asociado a ese número de manera recursiva y otra función que haga la misma operación pero
# con bucles. Con ambas funciones, calcular y comparar el tiempo de ejecución para n = (1, 10, 20, 30
# y 40) por fuerza bruta.

import datetime

def fibonacci(n):
   num_1 = 0
   num_2 = 1
   for i in range(0, n):
       temp = num_1
       num_1 = num_2
       num_2 = temp + num_2
   return num_1

start_time = datetime.datetime.now()

(fibonacci(10))

end_time = datetime.datetime.now()
print("El tiempo de ejecucción es: ", end_time - start_time)