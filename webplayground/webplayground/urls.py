
from django.contrib import admin
from django.urls import path, include
from pages.urls import pages_patterns
from django.conf import settings
from profiles.urls import profiles_patterns
from messenger.urls import messenger_patterns

urlpatterns = [
    path('', include('core.urls')),
    path('pages/', include(pages_patterns)),
    path('admin/', admin.site.urls),
    #paths de autentificacion 
    path('accounts/', include('django.contrib.auth.urls')), # haciendo esto django nos proveera de urls para la autentificacion  
    path('accounts/', include('registration.urls')),
    path('profiles/', include(profiles_patterns)),
    # path de messenger
    path('messenger/', include(messenger_patterns)),
]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    

