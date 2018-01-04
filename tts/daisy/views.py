from django.shortcuts import render
from django.http import HttpResponse
from daisy.models import Upload

# Create your views here.
def index(request):
    return HttpResponse('Welcome to daisy project. ')

def xonomy(request):
    text_data = Upload.objects.get(text_id=1)
    data_dict = {'insert_here': text_data}
    return render(request, 'xonomy/editor.html', context=data_dict)

def ace(request):
    text_data = Upload.objects.get(text_id=2)
    data_dict = {'insert_here': text_data}
    return render(request, 'ace/editor.html', context=data_dict)
