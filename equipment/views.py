from django.shortcuts import redirect, render
from .models import Other, CPAP, Suction
from .forms import EquipmentForm


# Create your views here.
def equipment(request):
    form = EquipmentForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            print(form.cleaned_data.get('equipment'))
            entry = CPAP.objects.get(equipment=form.cleaned_data.get('equipment'))
            print(entry)
            if not entry:
                entry = Suction.objects.get(equipment=request.POST['equipment'])
            if not entry:
                entry = Other.objects.get(equipment=request.POST['equipment'])
                
            entry.initials = form.cleaned_data.get('initials')
            entry.date = form.cleaned_data.get('date')
            entry.save()

            return redirect('equipment')
    other = Other.objects.all()
    cpap = CPAP.objects.all()
    suction = Suction.objects.all()

    context = {
        'cpap_data': cpap,
        'suction_data': suction,
        'other_data': other,
        'form': form
    }
    return render(request, 'equipment/equipment.html', context)