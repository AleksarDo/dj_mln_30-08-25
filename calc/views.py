from django.http import HttpResponse
from django.shortcuts import render
from . form_calc import CalcForm



def index(request):
    return render(request, 'calc/index.html')

def about(request):
    return render(request, 'calc/about.html')

# def calculate(request):
#     return render(request, 'calc/calculate.html', calc_form(request))


def calculate(request):
        if request.method == "POST":
            calc_form = CalcForm(request.POST)
            if calc_form.is_valid():
                Lb = request.POST.get("Lb")
                Wb = request.POST.get("Wb")
                Hb = request.POST.get("Hb")
                output = f"<p> параметры: Lb = {Lb} x {Wb} x {Hb}</p>"
                #return HttpResponse(output)
            return render(request, 'calc/calculate.html', {'form': calc_form, 'out': output})

        calc_form = CalcForm()
        return render(request, 'calc/calculate.html', {'form': calc_form})


