from django import forms

class AddProductForm(forms.Form):
    products_file = forms.FileField(widget=forms.FileInput(
        attrs={'class': 'form-control'}
    ), required=True)