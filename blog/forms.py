from django import forms
from .models import Blog

#class BlogPost(forms.Form): 
# title과 body를 입력하는 공간 만듦, url에도 form을 열 수 있는 url만들어줌
# email = forms.EmailField()
    #files = forms.FileField()
    #url = forms.URLField()
    #words = forms.CharField(max_length=200)
    #max_number = forms.ChoiceField(choices=[('1', 'one'), ('2', 'two'), ('3', 'three')]) #선택 함수

class BlogPost(forms.ModelForm): #모델을 기반으로 한 입력공간 (일반)forms.form (모델기반)forms.ModelForm
    class Meta:  #-> class BlogPost(forms.Modelform)일때
        model = Blog
        fields = ['title', 'body']