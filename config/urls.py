from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from django.views import defaults as default_views
from django.views.generic import TemplateView
from wagtail.admin import urls as wagtailadmin_urls
from wagtail import urls as wagtail_urls

from expocic.courses.views import CursoView

urlpatterns = [
              path("accounts/", include("allauth.urls")),
              path("", TemplateView.as_view(template_name="pages/home.html"), name="home"),
              path('curso/<slug:curso_slug>/', CursoView.as_view(), name='curso_detail'),

              # User management
              path("users/", include("expocic.users.urls", namespace="users")),
              path(settings.ADMIN_URL, include(wagtailadmin_urls)),
              path('django-admin/', admin.site.urls),
              path('', include(wagtail_urls)),
          ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    # This allows the error pages to be debugged during development, just visit
    # these url in browser to see how these error pages look like.
    urlpatterns += [
        path(
            "400/",
            default_views.bad_request,
            kwargs={"exception": Exception("Bad Request!")},
        ),
        path(
            "403/",
            default_views.permission_denied,
            kwargs={"exception": Exception("Permission Denied")},
        ),
        path(
            "404/",
            default_views.page_not_found,
            kwargs={"exception": Exception("Page not Found")},
        ),
        path("500/", default_views.server_error),
    ]
    if "debug_toolbar" in settings.INSTALLED_APPS:
        import debug_toolbar

        urlpatterns = [path("__debug__/", include(debug_toolbar.urls))] + urlpatterns
