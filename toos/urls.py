from django.contrib import admin
from django.urls import path, include, re_path
from django.views.generic import TemplateView
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/', include('accounts.urls')),
    path('api/', include('course.urls')),
    path('api/', include('stuff.urls')),
    path('api/', include('utils.urls')),
    # re_path('', TemplateView.as_view(template_name='index.html'), name="main"),
]

# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL,
#     document_root=settings.MEDIA_ROOT)

# asl
# urlpatterns += [re_path('',
#     TemplateView.as_view(template_name='index.html'), name='react')]


# urlpatterns += staticfiles_urlpatterns()
