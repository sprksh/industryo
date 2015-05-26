from django import forms
from workplaceprofile.models import *
from workplace.models import *


class EditTeamForm(forms.ModelForm):
    city = forms.CharField(max_length=50, required=False)          ## later change it to queryset
    address = forms.CharField(max_length=255, required=False)
    contact = forms.CharField(max_length=255, required=False)
    about = forms.CharField(widget=forms.Textarea, max_length=5000, required=False)
    institution_name = forms.CharField(max_length=50, required=False)        ## later change it to queryset
    participation = forms.CharField(max_length=255, required=False)
    logo = forms.ImageField(required=False)

    # def dude

    class Meta:
        model = WorkplaceProfile
        exclude = ['workplace', 'points', 'materials', 'area', 'institution', '']
        fields = ['city', 'institution_name', 'address', 'contact', 'about', 'participation']


class EditSMEForm(forms.ModelForm):
    city = forms.CharField(max_length=50)          ## later change it to queryset
    address = forms.CharField(max_length=255, required=False)
    contact = forms.CharField(max_length=255, required=False)
    about = forms.CharField(widget=forms.Textarea, max_length=5000, required=False)

    materials = forms.CharField(max_length=255, required=False)
    assets = forms.CharField(max_length=255, required=False)
    operations = forms.CharField(max_length=255, required=False)
    capabilities = forms.CharField(widget=forms.Textarea, max_length=5000, required=False)
    product_details = forms.CharField(widget=forms.Textarea, max_length=5000, required=False)

    class Meta:
        model = WorkplaceProfile
        exclude = ['workplace', 'points', 'logo', 'area', 'institution', 'participation']
        fields = ['city', 'assets', 'operations', 'materials', 'address', 'contact', 'about', 'capabilities', 'participation', 'materials', 'product_details']


## class Edit LSI form


class SetMaterialForm(forms.ModelForm):
    materials = forms.CharField(max_length=50)

    class Meta:
        model = WorkplaceProfile
        exclude = ['workplace', 'points', 'logo', 'area', 'institution', 'participation', 'assets', 'operations',
                   'address', 'contact', 'about', 'capabilities', 'product_details']
        fields = ['materials']


class SetOperationForm(forms.ModelForm):
    operations = forms.CharField(max_length=50)

    class Meta:
        model = WorkplaceProfile
        exclude = ['workplace', 'points', 'logo', 'area', 'institution', 'participation', 'assets', 'materials',
                   'address', 'contact', 'about', 'capabilities', 'product_details']
        fields = ['operations']


class SetAssetForm(forms.ModelForm):
    assets = forms.CharField(max_length=50)

    class Meta:
        model = WorkplaceProfile
        exclude = ['workplace', 'points', 'logo', 'area', 'institution', 'participation', 'materials', 'operations',
                   'address', 'contact', 'about', 'capabilities', 'product_details']
        fields = [ 'assets',]