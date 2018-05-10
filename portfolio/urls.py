
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
import jobs.views
from producthunt import views
from accounts import views
from products import views
from vuebattlesystem import urls


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', jobs.views.home, name='home'),
    path('blog/', include('blog.urls')),
    path('computer/', jobs.views.computer, name='computer'),
    path('producthunt/', include('producthunt.urls'), name='producthunt'),
    path('vuebattle/', include('vuebattlesystem.urls'), name='vuebattle' )

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
