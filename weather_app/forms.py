from weather_app.models import Todolist,Contact
from django.forms   import ModelForm


class Taskform(ModelForm):
    class Meta:
          model = Todolist
          fields =['task','done']


class Contactform(ModelForm):
    class Meta:
        model= Contact
        fields =['username','email','message']