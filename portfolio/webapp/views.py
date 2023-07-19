from webapp.models import Webapp
from django.shortcuts import render

# Create your views here.
def index(request):
    webapp = Webapp.objects.all()
    context = {
        'webapp': webapp,
    }
    return render(request, 'index.html', context)
