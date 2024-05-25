from django import forms
from .models import MediaFile

class MediaFileForm(forms.ModelForm):
    class Meta:
        model = MediaFile
        fields = ['title', 'file', 'profile', 'display_photo1', 'display_photo2', 'display_photo3' ]

