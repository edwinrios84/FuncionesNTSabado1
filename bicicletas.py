#crear una funcion en python para crear una lista de n estudiantes que son diccionarios


#crear una lista de 20 notas asociadas a la eficiencia
#crear una lista de 20 notas asociadas al parecido
#crear una lista de 20 notas asociadas a la estabilidad
#crear una rutina para obtener el promedio de esas notas
#crear una rutina para calcular el ganador

from funcionUno import crear_lista_estudiantes
from funcionDos import crear_lista_notas
from funcionTres import calcularPromedioNotas2
from funcionCuatro import evaluarBicicleta

#Paso 1: Creo el equipo:
equipoUno=crear_lista_estudiantes(4)

# Paso 2: Creo las notas de eficiencia, parecido y estabilidad, de la bicicleta
notasEficiencia=crear_lista_notas(50)
notasParecido=crear_lista_notas(50)
notasEstabilidad=crear_lista_notas(50)

# Paso 3: Calculo el promedio de cada una de las notas (componente):
promedioEficiencia=calcularPromedioNotas2(notasEficiencia)
promedioParecido=calcularPromedioNotas2(notasParecido)
promedioEstabilidad=calcularPromedioNotas2(notasEstabilidad)

# Paso 4: Calculo la nota final de la bicicleta:
evaluacionFinal=evaluarBicicleta(promedioEficiencia,promedioEstabilidad,promedioParecido)

# Paso 5: Imprimo el resultado:
for i in range(4):    
    print(f"El resultado del equipo {i+1} es:{evaluacionFinal}")
