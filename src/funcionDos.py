# Crear una funcion que cree una lista de notas
import random
def crear_lista_notas(cantidad_notas):
    lista_notas=[]
    for _ in range (cantidad_notas):
        nota=random.randint(1,5)
        lista_notas.append(nota)
    return lista_notas
