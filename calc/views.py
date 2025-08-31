from django.http import HttpResponse
from django.shortcuts import render
from . form_calc import CalcForm



def index(request):
    return render(request, 'calc/index.html')

def about(request):        
              
                
    return render(request, 'calc/about.html')


def calculate(request):
    
    output = "Заполните поля формы"
    if request.method == "POST":
        calc_form_Ng = CalcForm(request.POST)
        
        if calc_form_Ng.is_valid():
            Lb = float(request.POST.get("Lb"))
            Wb = float(request.POST.get("Wb"))
            Hb = float(request.POST.get("Hb"))
            Cdb = request.POST.get("Cdb")
            Td = request.POST.get("Td")
            
            
            Adb = round((Lb * Wb)+(6 * Hb)+(9*3.14*Hb*Hb), 1)
            output = f"Adb = {Lb} * {Wb} + 6 * {Hb} + {9*3.14} * {Hb*Hb} = {Adb} м.кв.; Cdb  = {Cdb}; Td = {Td}."
            #return HttpResponse(output)
            print(output)
            context = {'form': calc_form_Ng, 'out': output}            
            return render(request, "calc/calculate.html", context)


    calc_form_Ng = CalcForm()
    context = {'form': calc_form_Ng, 'out': output}    
    return render(request, "calc/calculate.html", context)

def thunmap(request):
     return render(request, 'calc/thundemap.html')
    




