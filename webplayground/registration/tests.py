from django.test import TestCase
from .models import Profile
from django.contrib.auth.models import User


# modelo de prueba unitaria     1 importo los modelos a probar  
class ProfileTestCase(TestCase):     # el metodo setUP que se esta heredando de TestCase es donde tenemos que preparar la prueba 
    def setUp(self):
        User.objects.create_user('test', 'test@test.com', 'test1470')  # le paso los parametros username, email, contraseña 
                                    # y luego tenemos la prueba  el nombre puede ser cualquiera pero tiene que comensar por test_ 
    def test_profile_exists(self):
        exists = Profile.objects.filter(user__username= 'test').exists()     # existe un usuario con el nombre test? 
        self.assertEqual(exists, True)

        