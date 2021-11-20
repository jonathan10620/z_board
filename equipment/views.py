from django.shortcuts import redirect, render
from .models import Other, CPAP, Suction
from .forms import EquipmentForm
from django.contrib import messages


# Create your views here.
def equipment(request):
    if not request.session.get("logged_in"):
        messages.add_message(request, messages.INFO, "Please log in first")
        return redirect("login")
    form = EquipmentForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            print(form.cleaned_data.get('equipment'))
            try:
                entry = CPAP.objects.get(equipment=form.cleaned_data.get('equipment'))
            except Exception as e:
                try:
                    entry = Suction.objects.get(equipment=form.cleaned_data.get('equipment'))    
                except Exception as e:
                    entry = Other.objects.get(equipment=form.cleaned_data.get('equipment'))
                
            entry.initials = form.cleaned_data.get('initials')
            entry.date = form.cleaned_data.get('date')
            entry.save()
            messages.success(request, "Equipment updated")

            return redirect('equipment')
    other = Other.objects.all()
    cpap = CPAP.objects.all()
    suction = Suction.objects.all()
    


    context = {
        'cpap_data': cpap,
        'suction_data': suction,
        'other_data': other,
        'form': form,
        

    }
    return render(request, 'equipment/equipment.html', context)