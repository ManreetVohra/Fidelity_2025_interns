from django import forms
from app_stocks.models import Stock

class StockForm(forms.ModelForm):
    class Meta:
        model=Stock
        fields='__all__'