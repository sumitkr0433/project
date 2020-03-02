from django import forms
from .models import som,clustering,Upload_Swigy_Files


class Upload_Swigy_Files(forms.ModelForm):
    class Meta:
        model = Upload_Swigy_Files
        fields = '__all__'


class som(forms.ModelForm):
    class Meta:
        model = som
        fields = '__all__'


     
class clustering(forms.ModelForm):
    class Meta:
        model = clustering
        fields = '__all__'


# class plot(forms.ModelForm):
#     class Meta:
#         model = clustering
#         fields = ('Number_of_chunks', 'Max_iteration', 'state','Som_map_column','Som_map_rows')




