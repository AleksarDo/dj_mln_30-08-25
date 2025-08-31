from django import forms
from django.shortcuts import render
from django.http import HttpResponse

class CalcForm(forms.Form):
    Lb=forms.DecimalField(label='Даўжыня будынка  - Lb, м',
                           initial=5, min_value=1.5, decimal_places=1,
                           widget= forms.NumberInput(attrs={"class": "inpt_ed"}))
    Wb=forms.DecimalField(label='Шырыня будынка - Wb, м', 
                          initial=3, min_value=1, decimal_places=1,
                          widget= forms.NumberInput(attrs={"class": "inpt_ed"}))
    Hb=forms.DecimalField(label='Вышыня будынка  - Hb, м',
                           initial=4, min_value=2, decimal_places=1, 
                           widget= forms.NumberInput(attrs={"class": "inpt_ed"}))
    Cdb=forms.TypedChoiceField(label="Сd - ",
                                empty_value=(3, "Изолированное здание (отсутствуют объекты поблизости от него)-1.0"),
                               choices=((1, "Здание, окруженное более высокими объектами или деревьями - 0.25"),
                                        (2, "Здание, окруженное объектами или деревьями такой же высоты или более низкими - 0.5"),
                                        (3, "Изолированное здание (отсутствуют объекты поблизости от него) - 1.0"),
                                        (4, "Изолированное здание, находящееся на вершине холма или возвышенности - 2.0"),
                                   ),
                               )
    Td=forms.IntegerField(label="Тd — ", max_value=30, min_value=18, widget=forms.NumberInput(attrs={"class": "inpt_ed"}))
                               
    


# зробім аб’ект класа СalcForm

