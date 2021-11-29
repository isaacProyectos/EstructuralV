from homes.models import tessiu
from django.shortcuts import render
import math

distancias = []

def creaMatriz(n,m):
    matriz = []
    for i in range(n):
        a = [0]*m
        matriz.append(a)
    return matriz

def calculaGrafo(request):
    tejidos = []
    

    Lista = tessiu.objects.get_queryset()
    for elemento in Lista:
        tejidos.append([elemento.temperature, elemento.color, elemento.inflamation])

    global distancias 
    distancias = creaMatriz(len(tejidos), len(tejidos))
    for i in range(len(tejidos)):
        for j in range(i, len(tejidos)):         
            distan = math.dist(tejidos[i], tejidos[j])
            distancias[i][j] = distan
            distancias[j][i] = distan

    diccionario={"distancias": distancias}
    return render(request,"grafo.html",diccionario)


def umbral(request):
    umbral = request.POST['umbral']
    print(umbral)
    procesado = []
    for i in range(len(distancias)):
        for j in range(i, len(distancias)):
            if distancias[i][j] == 0:
                procesado.append([i,j,distancias[i][j], "Si"])
            elif distancias[i][j] > float(umbral):
                procesado.append([i,j,distancias[i][j], "No"])
            else:
                procesado.append([i,j,distancias[i][j], "Si"])
    #print("procesado es: ",procesado)

    diccionario = {"umbrales" : procesado}
    return render(request, "umbral.html", diccionario)

def procesamiento(request):
    print(request.POST['umbral'])
    diccionario = {"umbrales" : umbral}
    return render(request, "umbral.html", diccionario)
    