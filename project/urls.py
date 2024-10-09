from django.contrib import admin
from django.urls import path, include
from django.conf import settings  # Чтобы была возможность подгрузить файл с настройками
from django.conf.urls.static import static  # Чтобы подгрузить обработчик статических файлов

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('apps.app.urls')),
    path('train/', include('apps.db_train.urls')),
    path('tinymce/', include('tinymce.urls')),
    path('api_alter/', include('apps.db_train_alternative.urls')),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api/', include('apps.api.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)  # Добавление путей для обработки
    # медиафайлов в Django(по умолчанию не обрабатывается, поэтому пишем, чтобы обрабатывалась как статика). Для режима
    # продакшн (Debug=False) нужно использовать другие сервисы (не Django) для обработки медиафайлов.

    urlpatterns += [
        path("__debug__/", include("debug_toolbar.urls")),
    ]