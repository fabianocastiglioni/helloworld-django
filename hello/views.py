from django.http import HttpResponse

def home(request):
    return HttpResponse("Cloud Computing & Site Reliability Engineering - Anderson Cruz Fernandes")
