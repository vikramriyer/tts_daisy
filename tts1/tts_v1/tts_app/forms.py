'''
from django import forms
from tts_app.models import Books, Editor2, Pages

class AddBookForm(forms.ModelForm):

    class Meta():
        model = Books
        fields = ()

class LoadPageForm(forms.ModelForm):

    class Meta():
        model = Page
        fields = ('text', 'image')
'''
