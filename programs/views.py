from django.shortcuts import render

from programs.models import Program
from programs.models import CorrelationScore

def index(request):
  return render(request, 'programs/index.html')

def matrix(request):
  return render(request, 'programs/matrix.html')

def finder(request):
  return render(request, 'programs/finder.html')

def hypothetical(request):
  return render(request, 'programs/request.html')
