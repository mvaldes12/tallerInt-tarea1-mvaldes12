from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
import requests


def index(request):
    #response = requests.get('https://tarea-1-breaking-bad.herokuapp.com/api/characters').json
    bb = "bb"
    bcs = "bcs"
    context = {'bb': bb, 'bcs': bcs}
    return render(request, 'tarea1/index.html', context)

def temporadas(request, serie):
    r = requests.get('https://tarea-1-breaking-bad.herokuapp.com/api/episodes')
    error = 0
    if r.status_code == 429:
        error = '429'
    if serie == "bb":
        response = requests.get('https://tarea-1-breaking-bad.herokuapp.com/api/episodes?series=Breaking+Bad').json()
        temp = []
        for cap in response:
            if cap["season"] not in temp:
                temp.append(cap["season"])
    elif serie == "bcs":
        response = requests.get('https://tarea-1-breaking-bad.herokuapp.com/api/episodes?series=Better+Call+Saul').json()
        temp = []
        for cap in response:
            if cap["season"] not in temp:
                temp.append(cap["season"])
    else:
        temp = 0
        serie = 0
    context = {'temp': temp, 'serie': serie, 'error': error}
    return render(request, 'tarea1/temporadas.html', context)

def capitulos(request, serie, num_temp):
    r = requests.get('https://tarea-1-breaking-bad.herokuapp.com/api/episodes')
    error = 0
    if r.status_code == 429:
        error = '429'
    if serie == "bb":
        response = requests.get('https://tarea-1-breaking-bad.herokuapp.com/api/episodes?series=Breaking+Bad').json()
        capitulos = []
        t = []
        for cap in response:
            if int(cap["season"]) == num_temp:
                capitulos.append([cap["title"], cap["episode"]])
            if cap["season"] not in t:
                t.append(cap["season"])
    else:
        response = requests.get('https://tarea-1-breaking-bad.herokuapp.com/api/episodes?series=Better+Call+Saul').json()
        capitulos = []
        t = []
        for cap in response:
            if int(cap["season"]) == num_temp:
                capitulos.append([cap["title"], cap["episode"]])
            if cap["season"] not in t:
                t.append(cap["season"])
    if str(num_temp) not in t:
        num_temp = 0
    context = {'cap': capitulos, 'temp': num_temp, 'serie': serie, 'error': error}
    return render(request, 'tarea1/capitulos.html', context)

def episodio(request, serie, num_temp, num_cap):
    r = requests.get('https://tarea-1-breaking-bad.herokuapp.com/api/episodes')
    error = 0
    if r.status_code == 429:
        error = '429'
    if serie == "bb":
        response = requests.get('https://tarea-1-breaking-bad.herokuapp.com/api/episodes?series=Breaking+Bad').json()
        info_episodio = []
        c = []
        for cap in response:
            if int(cap["season"]) == num_temp:
                if int(cap["episode"]) == num_cap:
                    fecha = cap["air_date"][0:10]
                    info_episodio.append([cap["title"], fecha, cap["characters"]])
                if cap["episode"] not in c:
                    c.append(cap["episode"])
    else:
        response = requests.get('https://tarea-1-breaking-bad.herokuapp.com/api/episodes?series=Better+Call+Saul').json()
        info_episodio = []
        c = []
        for cap in response:
            if int(cap["season"]) == num_temp:
                if int(cap["episode"]) == num_cap:
                    info_episodio.append([cap["title"], cap["air_date"], cap["characters"]])
                if cap["episode"] not in c:
                    c.append(cap["episode"])
    if num_cap not in c:
        num_cap = 0
    context = {'episodio': info_episodio,'cap': num_cap, 'temp': num_temp, 'serie': serie, 'error': error}
    return render(request, 'tarea1/episodio.html', context)

def personaje(request, p):
    r = requests.get('https://tarea-1-breaking-bad.herokuapp.com/api/episodes')
    error = 0
    if r.status_code == 429:
        error = '429'
    nombre = p.replace(" ", "+")
    url = 'https://tarea-1-breaking-bad.herokuapp.com/api/characters?name=' + nombre
    response = requests.get(url).json()
    if response == []:
        response = 0
    url_citas = 'https://tarea-1-breaking-bad.herokuapp.com/api/quote?author=' + nombre
    citas = requests.get(url_citas).json()
    context = {'personaje': response, 'citas': citas, 'error': error}
    return render(request, 'tarea1/personaje.html', context)

def busqueda(request):
    r = requests.get('https://tarea-1-breaking-bad.herokuapp.com/api/episodes')
    error = 0
    if r.status_code == 429:
        error = '429'
    response = request.POST.get('gsearch')
    if response == None:
        response = ""
    offset = 0
    todas = []
    b = True
    while b:
        url = 'https://tarea-1-breaking-bad.herokuapp.com/api/characters?limit=10&offset=' + str(
            offset) + '&name=' + response
        buscador = requests.get(url).json()
        todas.append(buscador)
        print(len(buscador))
        if len(buscador) < 10:
            b = False
        else:
            offset += 10
    print(todas)
    if todas == [[]]:
        todas = 0
    context = {'todas': todas, 'error': error}
    return render(request, 'tarea1/busqueda.html', context)



