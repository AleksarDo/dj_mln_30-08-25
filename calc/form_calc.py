from django import forms
from django.shortcuts import render
from django.http import HttpResponse

class CalcForm(forms.Form):
    Lb=forms.DecimalField(label='Даўжыня будынка - Lb, м',
                           initial=5, min_value=1.5, decimal_places=1,
                           widget= forms.NumberInput(attrs={"class": "inpt_ed"}))
    Wb=forms.DecimalField(label='Шырыня будынка - Wb, м', 
                          initial=3, min_value=1, decimal_places=1,
                          widget= forms.NumberInput(attrs={"class": "inpt_ed"}))
    Hb=forms.DecimalField(label='Вышыня будынка - Hb, м',
                           initial=4, min_value=2, decimal_places=1, 
                           widget= forms.NumberInput(attrs={"class": "inpt_ed"}))
    


# зробім аб’ект класа СalcForm

# def calc_form(request):

#     if request.method == "POST":
#         calc_form = CalcForm(request.POST)
#         if calc_form.is_valid():
#             Lb = request.POST.get("Lb")
#             Wb = request.POST.get("Wb")
#             Hb = request.request.POST.get("Hb")
#             output = f"<p> параметры: Lb = {Lb} x {Wb} x {Hb}</p>"
#             #return HttpResponse(output)
#         return render(request, {'form': calc_form, 'out': output})

#     calc_form = CalcForm()
#     return {'form': calc_form}