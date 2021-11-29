from django.shortcuts import render
from django.http import HttpResponse
from .models import tessiu
# Create your views here.

def micasa(request):
    Lista=tessiu.objects.get_queryset()

    L1,L2= procesamientoLista(Lista)
    template_name='homes/homes.html'
    mislistas=[Lista,L1,L2]
    diccionario={'l':Lista,"otra":"informacion","Lista1":L1,"Lista2":L2,"mislistas":mislistas}
    return render(request,template_name,diccionario)

def procesamientoLista(L):
    listaColorMayor39=[]
    listaColorMenor39=[]
    for i in L: 
        if i.color > 39:
            listaColorMayor39.append(i)
        else:
            listaColorMenor39.append(i)
    
    return listaColorMayor39,listaColorMenor39

