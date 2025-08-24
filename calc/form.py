from django import forms

class UserForm(forms.Form):
    intval=forms.IntegerField(max_value=9, min_value=1,
                                label="Ваш вариант", help_text="ваш вариант числа",)

    