from django.shortcuts import render


# Create your views here.

rooms= [
    {'id': 1, 'name': 'Lets run python '},
    {'id': 2, 'name': 'Design with me'},
    {'id': 3, 'name': 'Frontend developer'},
]

def home(request):
    context= {'rooms' : rooms}
    return render(request, 'base/home.html', context)

def room(request,pk):
    return render(request, 'base/room.html')