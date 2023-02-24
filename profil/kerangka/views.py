#from turtle import title
from django.shortcuts import render,HttpResponse

# Create your views here.
def awal(request):
    return HttpResponse('Berhasil Diinstall')

def home(request):
    return render(request,'home.html')

def profil(request):
    return render(request,'profil.html')

def kontak(request):
    return render(request,'kontak.html')