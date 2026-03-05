from django.shortcuts import render
from .models import Leader
# Create your views here.

def leadership_list(request):
    leaders = Leader.objects.all()
    return render(request, 'leadership/list.html', {'leaders': leaders})
    