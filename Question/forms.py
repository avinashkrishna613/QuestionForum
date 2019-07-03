from .models import Ques
from django import forms

class QuestionForm(forms.Form):
    user = forms.CharField(label = 'your name', max_length = 20 ,disabled = True)
    ques = forms.CharField(help_text= "enter the question")
    
    
class AnswerSubForm(forms.Form):
    answeredby = forms.CharField(max_length = 20, disabled = True)
    ans = forms.CharField(max_length = 1000)

    

