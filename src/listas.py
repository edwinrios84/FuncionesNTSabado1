# Crear una lista de 500 notas (1,5)
# Mock: Simular datos
import random
notas=[]
# Para 500 notas, implementamos ciclo For:
for i in range(5):    
    nota=random.randint(1,5)
    # Llenar una lista:
    notas.append(nota)
#print(notas)
# Manipulando listas con Python:
notas.insert(1,80) # Inserta en una posición indicada el valor deseado
notas.remove(80) # Elimina el registro con valor 80
notas.pop(0) # Elimina posicion del registro
notas.sort() # Ordenar lista de mayor a menor
notas.sort(reverse=True) # Ordenar lista de menor a mayor
notas.clear() # Limpiar la lista de datos
print(notas)
