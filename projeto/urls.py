from django.contrib import admin
from django.urls import path, include
from colaboradores import urls as colaboradores_urls
from homepage import urls as homepage_urls
from django.contrib.auth import views as auth_views

# Gambiarra para o Django exibir os arquivos de mídia (SOMENTE PARA DEV)
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', include(homepage_urls)),
    path('admin/', admin.site.urls),
    path('colaboradores/', include(colaboradores_urls)),
    path('accounts/login/', auth_views.LoginView.as_view(), name="login"),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) # Acessando a URL 'MEDIA_URL' (/media/) e
                                                                  # buscando os arquivos da pasta 'MEDIA_ROOT' (media)
