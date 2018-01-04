from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    my_dict = {'insertme': "Hello template. "}
    return render(request, 'ace_vs_xonomy/index.html', context=my_dict)
