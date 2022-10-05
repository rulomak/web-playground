
from .forms import UserCreationFormWithEmail, ProfileForm, EmailForm
from django.views.generic import CreateView
from django.views.generic.edit import UpdateView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django import forms
from .models import Profile
# Create your views here.
class SignUpView(CreateView):   # vista de registro 
    form_class = UserCreationFormWithEmail
    template_name = 'registration/signup.html'        # para que carge el template
    """  en lugar de crar un formulacio de 0  lo que hacemos es importar este ( userchangeform) que es generico
    y se lo pasaremos a esta vista (CreateView )  para que lo maneje todo automaticamente    """
    def get_success_url(self):
        return reverse_lazy('login') + '?register'     # para redireccionar a login luego de hacer el registro 

    def get_form(self, form_class=None):
        form = super(SignUpView, self).get_form()
        # modificando el formulario en tiempo real  
        form.fields['username'].widget = forms.TextInput(attrs={'class': 'form-control mb-2', 'placeholder': "Nombre de usuario"})
        form.fields['email'].widget = forms.EmailInput(attrs={'class': 'form-control mb-2', 'placeholder': "Direccion de Email"})
        form.fields['password1'].widget = forms.PasswordInput(attrs={'class': 'form-control mb-2', 'placeholder': "Contraseña"})
        form.fields['password2'].widget = forms.PasswordInput(attrs={'class': 'form-control mb-2', 'placeholder': "Repite la contraseña"})

        return form


@method_decorator(login_required, name='dispatch')                # solo es accesible si el usuario esta registrado 
class ProfileUpdate(UpdateView):
    form_class = ProfileForm
    success_url = reverse_lazy('profile')
    template_name = 'registration/profile_form.html'

    def get_object(self):
        profile, created = Profile.objects.get_or_create(user=self.request.user)
        return profile



@method_decorator(login_required, name='dispatch')                # solo es accesible si el usuario esta registrado 
class EmailUpdate(UpdateView):
    form_class = EmailForm
    success_url = reverse_lazy('profile')
    template_name = 'registration/profile_email_form.html'

    def get_object(self):
        return self.request.user

    
def get_form(self, form_class=None):
    form = super(EmailUpdate, self).get_form()
        # modificando el formulario en tiempo real  
    form.fields['email'].widget = forms.EmailInput(attrs={'class':'form-control mb-2', 'placeholder':"Email"})

    return form

    