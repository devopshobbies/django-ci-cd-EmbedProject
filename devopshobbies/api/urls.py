from django.urls import path, include

urlpatterns = [
    path('blog/', include(('devopshobbies.blog.urls', 'blog'))),
]
