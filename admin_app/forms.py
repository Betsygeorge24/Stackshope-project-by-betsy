from django import forms
from seller.models import Attribute, AttributeOption, ProductVariant
from core.models import SubCategory


class AttributeForm(forms.ModelForm):
    """Form for creating and editing Product Attributes"""
    
    subcategory = forms.ModelChoiceField(
        queryset=SubCategory.objects.all(),
        widget=forms.Select(attrs={
            'class': 'w-full px-4 py-2.5 border border-muted/50 rounded-xl text-sm focus:outline-none focus:border-dark bg-white'
        }),
        required=False,
        label="Subcategory (Optional)"
    )
    
    class Meta:
        model = Attribute
        fields = ['name', 'subcategory']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'w-full px-4 py-2.5 border border-muted/50 rounded-xl text-sm focus:outline-none focus:border-dark',
                'placeholder': 'e.g., Color, Size, Material',
                'required': True
            }),
        }
        labels = {
            'name': 'Attribute Name',
        }


class AttributeOptionForm(forms.ModelForm):
    """Form for creating and editing Attribute Options"""
    
    attribute = forms.ModelChoiceField(
        queryset=Attribute.objects.all(),
        widget=forms.Select(attrs={
            'class': 'w-full px-4 py-2.5 border border-muted/50 rounded-xl text-sm focus:outline-none focus:border-dark bg-white'
        }),
        label="Select Attribute"
    )
    
    class Meta:
        model = AttributeOption
        fields = ['attribute', 'value']
        widgets = {
            'value': forms.TextInput(attrs={
                'class': 'w-full px-4 py-2.5 border border-muted/50 rounded-xl text-sm focus:outline-none focus:border-dark',
                'placeholder': 'e.g., Red, XL, Cotton',
                'required': True
            }),
        }
        labels = {
            'value': 'Option Value',
        }



