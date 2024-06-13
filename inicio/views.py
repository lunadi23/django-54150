from django.shortcuts import render
from datetime import datetime

from django.http import HttpResponse
from django.template import Template, Context, loader

from inicio.models import Cliente

import random

def inicio(request):
    #v1
    #return HttpResponse('Bienvenidos a mi INICIO!!!')
    
    return render(request,'inicio/index.html')

def template1(request, nombre, apellido):
    fecha = datetime.now()
    return HttpResponse(f'<h1>Mi Template 1</h1> -- Fecha: {fecha} -- Buenas {nombre} {apellido}')

def template2(request, nombre, apellido):
    
    archivo_abierto = open(r'C:\Phyton\DiegoLuna-3erTP\templates\template2.html')
    # archivo_abierto = open('templates\template2.html')
    
    template = Template(archivo_abierto.read())
    
    
    fecha = datetime.now()
    
    datos = {
        'fecha': fecha,
        'nombre': nombre,
        'apellido': apellido,
    }
    
    archivo_abierto.close()
    
    contexto = Context(datos)
    
    template_renderizado = template.render(contexto)
    
    return HttpResponse(template_renderizado)

def template3(request, nombre, apellido):
     
    template = loader.get_template('template3.html')
    
    
    fecha = datetime.now()
    
    datos = {
        'fecha': fecha,
        'nombre': nombre,
        'apellido': apellido,
    }
    
      
    template_renderizado = template.render(datos)
    
    return HttpResponse(template_renderizado)


def template4(request, nombre, apellido):
          
    fecha = datetime.now()
    
    datos = {
        'fecha': fecha,
        'nombre': nombre,
        'apellido': apellido,
    }
       
    return render(request,'template4.html', datos)

def probando(request):
    
    lista = list(range(500))
    
    numeros = random.choices(lista, k=50)
    
    return render(request,'probando_if_for.html', {'numeros': numeros})

def crear_cliente(request, apno, email):
    cliente = Cliente(apno=apno, email=email)
    cliente.save()
    return render(request,'cliente_templates/creacion.html', {"cliente":cliente})