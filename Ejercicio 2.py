# Escribir una función que lea dos ficheros csv con una lista larga de datos de personas (50
# personas y 1000 personas) y llame a dos funciones que pongan su nombre en formato capitalizado
# y calculen la letra de DNI correspondiente. Realiza la comprobación de rendimiento con la
# librería cProfile y muestra los datos. Describe que indica cada dato que nos proporciona cProfile.

import cProfile

nif_dict = {"0": "T", "1": "R", "2": "W", "3": "A",
           "4": "G", "5": "M", "6": "Y", "7": "F",
           "8": "P", "9": "D", "10": "X", "11": "B",
           "12": "N", "13": "J", "14": "Z", "15": "S",
           "16": "Q", "17": "V", "18": "H", "19": "L",
           "20": "C", "21": "K", "22": "E"}

def check_DGT(ruta):
    """Esta función es un fichero sobre usuarios que corrije y sobrescribe en el
    mismo fichero todos los datos correjidos de los usuarios y con multas de tráfico
    por sumar.
    Parámetros:
    ruta: un archivo con datos sin corregir y sin las multas sumadas
    Salida:
    """

   file = open(ruta, "r", encoding="utf-8")
   lineas = file.readlines()
   lista = []
   for linea in lineas:
       lista1 = []
       datos = linea.split(",")
       nombre = check_username(datos[0])
       nif = check_nif(datos[1])
       lista1.append(nombre)
       lista1.append(nif)
       lista.append(lista1)
   print(lista)
   return

def check_username(usuario_nombre):

   """Función que corrige el nombre de cada usuario, poniendo la primera letra en mayuscula.
   Parámetros:
   usuario_nombre: un str que contendrá en cada caso el nombre o los apellidos.
   Salida: Proporciona un str con los datos corregidos.
   """
   return usuario_nombre.title()

def check_nif(usuario_nif):
   """Función que calcula y corrige la letra erronea de cada DNI.
   Parámetros:
   usuario_nif: Un str que contendrá el nif del usuario/a en el formato de 8 números y una letra.
   Salida: Proporciona un str con el nif corregido.
   """
   nif_numero = usuario_nif[0:8]
   letra_correcta = nif_dict[str(int(nif_numero) % 23)]
   return nif_numero + letra_correcta

check_DGT("A50.csv")
cProfile.run("[(a, b) for a in (1, 3, 5) for b in (2, 4, 6)]")


