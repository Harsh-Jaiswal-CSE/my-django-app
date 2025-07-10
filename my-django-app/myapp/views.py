from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, World! Django is running on Kubernetes.")