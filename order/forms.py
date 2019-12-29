from django import forms
from django.forms import modelformset_factory

from .models import OrderPoAndPurchaser, OrderDetails


class OrderPoAndPurchaserModelForm(forms.ModelForm):
    class Meta:
        model = OrderPoAndPurchaser
        fields = '__all__'
        labels = {
            'po_no': 'Po No', 'Purchaser' : 'Purchaser'
        }
        widgets = {
            'po_no': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter Po No'
                }
            ),
            'Purchaser':forms.TextInput(attrs={
                'placeholder':"Enter Purchaser name"
            }),
            'po_date': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'size': 10, 'required': '',
                    'type': 'date',

                    'placeholder': 'Enter po date here'
                }
            ),
        }


OrderDetailsFormset = modelformset_factory(
    OrderDetails,
    fields=('po_date','items','items_types','quality','qty','unit','rate_per_unit','value','dispatcher',
            ),
    extra=1,
    widgets={

        'items': forms.TextInput(
            attrs={
                'class': 'form-control',
                'size': 10,'required':'',

                'placeholder': 'Enter items here'
            }
        ),
        'items_types': forms.TextInput(
            attrs={
                'class': 'form-control',
                'size': 10,'required':'',
                'placeholder': 'Enter items types here'
            }
        ),
        'quality': forms.TextInput(
            attrs={
                'class': 'form-control',
                'size': 10,'required':'',

                'placeholder': 'Enter quality here'
            }
        ),
        'qty': forms.TextInput(
            attrs={
                'class': 'form-control',
                'size': 10,'required':'',

                'placeholder': 'Enter qty here'

            }
        ),
        'unit': forms.TextInput(
            attrs={
                'class': 'form-control',
                'size': 10,'required':'',
                'placeholder': 'Enter unit here'
            }
        ),
        'rate_per_unit': forms.TextInput(
            attrs={
                'class': 'form-control',
                'size': 10,'required':'',
                'placeholder': 'Enter rate/unit here'
            }
        ),
        'value': forms.TextInput(
            attrs={
                'class': 'form-control',
                'size': 10,'required':'',
                'placeholder': 'Enter value here'
            }
        ),

        'dispatcher': forms.TextInput(
            attrs={
                'class': 'form-control',
                'size': 10,'required':'',
                'placeholder': 'Enter rate_per_unit here'
            }
        )



    }
)