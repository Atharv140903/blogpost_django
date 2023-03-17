from django import forms 
from froala_editor.widgets import FroalaEditor
from .models import blogPostModel

class blogPostForm(forms.ModelForm):

    class Meta:
        model = blogPostModel
        fields = ['description']
       