from django import forms
from .models import Course, Materi

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = "__all__"

        widgets = {
            'judul': forms.TextInput(attrs={'class': 'form-control'}),
            'deskripsi': forms.Textarea(attrs={'class': 'form-control','style':'height: 150px;'}),
            'durasi': forms.TextInput(attrs={'class': 'form-control'}),
        }

class MateriForm(forms.ModelForm):
    class Meta:
        model = Materi
        fields = "__all__"

        widgets = {
            'course': forms.Select(attrs={'class': 'form-control'}),
            'judul': forms.TextInput(attrs={'class': 'form-control'}),
            'deskripsi': forms.Textarea(attrs={'class': 'form-control','style':'height: 150px;'}),
            'embed_link': forms.TextInput(attrs={'class': 'form-control'}),
        }
