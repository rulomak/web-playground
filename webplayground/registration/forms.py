
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile

# extendiendo el formulario de registro  

class UserCreationFormWithEmail(UserCreationForm):
    email = forms.EmailField(required=True, help_text="Requerido, 254 caracteres maximo y debe ser valido")

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")    # redefino los campos en el orden 
        # email ya existe dentro del modelo de User   de lo contrario no funcionaria

      # funcion para validar el email como unico 
    def clean_email(self):
        email = self.cleaned_data.get("email")   # recuperando el valor de email 
        if User.objects.filter(email=email).exists():   # comprovara si el email ya existe 
            raise forms.ValidationError("El email ya esta registrado")     # si el email ya existe,  lansamos un error  
        
        return email


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['avatar', 'bio', 'link']
        widgets = {
            'avatar': forms.ClearableFileInput(attrs={'class':'form-control-file mt-3'}),
            'bio': forms.Textarea(attrs={'class':'form-control mt-3', 'rows':3, 'placeholder':'Biografia'}),
            'link': forms.URLInput(attrs={'class':'form-control mt-3', 'placeholder':'Enlace'}),

        }


class EmailForm(forms.ModelForm):
    email = forms.EmailField(required=True, help_text="Requerido, 254 caracteres maximo y debe ser valido")

    class Meta:
        model = User
        fields = ['email']

    # funcion para validar el email como unico 
    def clean_email(self):
        email = self.cleaned_data.get("email")   # recuperando el valor de email 
        if 'email' in self.changed_data:
            if User.objects.filter(email=email).exists():   # comprovara si el email ya existe 
                raise forms.ValidationError("El email ya esta registrado")     # si el email ya existe,  lansamos un error  
            
        return email