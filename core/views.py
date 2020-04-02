from django.shortcuts import render, HttpResponse

# Create your views here.

#O HttpResponse vai interpretar o que colocar como parâmetro e vai jogar na resposta http
def hello(request):
    return HttpResponse('<h1>Hello World</h1>')
#por causa do HttpResponse, ele vai interpretar que aqui tem um html e o navegador vai conseguir entender

def hello_two(request, nome, idade):
    return HttpResponse('<h1>Hello {} de {} anos</h1>'.format(nome,idade))