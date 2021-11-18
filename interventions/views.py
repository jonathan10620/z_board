from django.shortcuts import render

# Create your views here.
def interventions(request):
    return render(request, 'interventions/interventions.html')