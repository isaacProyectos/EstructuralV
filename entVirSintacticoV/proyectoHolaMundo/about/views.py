#from django.http.response import HttpResponse
from django.shortcuts import render

# Create your views here.
def about(request):
    resultado= mifuncion(request)
    template_name='about/about.html' 
    return render(request,template_name,{"nombreusuario": resultado,"edad":21})

def mifuncion(args):
    return 'isaac'
"""
textHTML=
  
<h1>Hola Mundo</h1>
<ul>
<li>Donde 
<li>La fiesta
</ul>
    
    
"""
    
