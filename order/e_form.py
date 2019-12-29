from django import forms
from . models import OrderDetails

class EditData(forms.ModelForm):
    class Meta:
        model =OrderDetails
        fields ='__all__'
        widgets = {

            'items': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'size': 9, 'required': '',

                    'placeholder': 'Enter items here'
                }
            ),
            'items_types': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'size': 6, 'required': '',
                    'placeholder': 'Enter items types here'
                }
            ),
            'quality': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'size': 5, 'required': '',

                    'placeholder': 'Enter quality here'
                }
            ),
            'qty': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'size': 9, 'required': '',

                    'placeholder': 'Enter qty here'

                }
            ),
            'unit': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'size': 5, 'required': '',
                    'placeholder': 'Enter unit here'
                }
            ),
            'rate_per_unit': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'size': 5, 'required': '',
                    'placeholder': 'Enter rate/unit here'
                }
            ),
            'value': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'size': 7, 'required': '',
                    'placeholder': 'Enter value here'
                }
            ),

            'dispatcher': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'size': 9, 'required': '',
                    'placeholder': 'Enter rate_per_unit here'
                }
            ),
            'dispatch_qty':forms.TextInput(
                attrs={
                    'class':'form-control',
                    'size':9,

                }
            ),
            'dispatch_date':forms.TextInput(
                attrs={
                    'class':'form-control',
                    'size':9,
                    'type':'date',
                }
            ),
            'total_supplied_qty':forms.TextInput(
                attrs={
                    'class':'form-control',
                    'size':9,
                }
            ),
            'balance_qty':forms.TextInput(
                attrs={
                    'class':'form-control',
                    'size':6,
                }
            ),
        }


class EditDispatch(forms.ModelForm):
    class Meta:
        model =OrderDetails
        fields ='dispatch_qty','dispatch_date','total_supplied_qty','balance_qty'
        widgets = {



            'dispatch_qty':forms.TextInput(
                attrs={
                    'class':'form-control',
                    'size':9,

                }
            ),
            'dispatch_date':forms.TextInput(
                attrs={
                    'class':'form-control',
                    'size':9,
                    'type':'date',
                }
            ),
            'total_supplied_qty':forms.TextInput(
                attrs={
                    'class':'form-control',
                    'size':9,
                }
            ),
            'balance_qty':forms.TextInput(
                attrs={
                    'class':'form-control',
                    'size':6,
                }
            ),
        }