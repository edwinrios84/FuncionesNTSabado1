# Crear una funcion que calcule el promedio de una lista de notas
def calcularPromedioNotas(listaNotas):
    # Recorrer una lista o arreglo:
    acumularNotas=0
    for nota in listaNotas:
        acumularNotas+=nota
    #print("Nota promedio es: ",acumularNotas/len(listaNotas))
    return (acumularNotas/len(listaNotas))

def calcularPromedioNotas2(listaNotas):    
    return (sum(listaNotas)/len(listaNotas))
    
#print(calcularPromedioNotas2([1,2,3,4,5]))

