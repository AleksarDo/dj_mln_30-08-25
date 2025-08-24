from django import forms
from django.shortcuts import render
from django.http import HttpResponse

class CalcForm(forms.Form):
    Lb=forms.DecimalField(label='Lb', initial=5, min_value=1.5, decimal_places=1)
    Wb=forms.DecimalField(label='Wb', initial=3, min_value=1, decimal_places=1)
    Hb=forms.DecimalField(label='Hb', initial=4, min_value=2, decimal_places=1)
    


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