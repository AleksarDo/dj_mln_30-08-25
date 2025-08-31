from django.http import HttpResponse
from django.shortcuts import render
from . form_calc import CalcForm



def index(request):
    return render(request, 'calc/index.html')

def about(request):
    return render(request, 'calc/about.html')


def calculate(request):
    
    output = "Заполните поля формыoutput"
    if request.method == "POST":
        calc_form_Ng = CalcForm(request.POST)
        
        if calc_form_Ng.is_valid():
            Lb = float(request.POST.get("Lb"))
            Wb = float(request.POST.get("Wb"))
            Hb = float(request.POST.get("Hb"))
            Cdb = float(request.POST.get("Cdb"))
            
            Adb = (Lb * Wb)+(6 * Hb)+(9*3.14*Hb*Hb)
            output = f"Adb = {Lb} * {Wb} + 6 * {Hb} + {9*3.14} * {Hb*Hb} = {Adb} Cdb  = {Cdb}"
            #return HttpResponse(output)
            print(output)
            context = {'form': calc_form_Ng, 'out': output}            
            return render(request, "calc/calculate.html", context)

            return render(request, "calc/calculate.html", context)

    calc_form_Ng = CalcForm()
    context = {'form': calc_form_Ng, 'out': output}
    
    return render(request, "calc/calculate.html", context)

