from django.shortcuts import render
from leadership.models import Leader
from members.models import Member

# Create your views here.

def home(request):
    leaders = Leader.objects.all()
    members = Member.objects.all()[:5]

    context = {
        'leaders' : leaders,
        'members' : members
    }

    return render(request, 'pages/home.html', context)