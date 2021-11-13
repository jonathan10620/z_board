from django.shortcuts import render, redirect
from django.contrib import messages
from datetime import datetime
from .forms import BMForm
from .models import BM

# Create your views here.
def bm(request):
    today = datetime.today()
    form = BMForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.success(request, "BM entry added")
            return redirect("bm")


    results = BM.objects.filter(date__month=today.month)

    context = {
        'form': form,
        'month': today.strftime('%B'),
        'results': results,
    }
    return render(request, 'bm/bm.html', context)