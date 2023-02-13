from django.urls import path, include

urlpatterns = [
    path('blog/', include(('devopshobbies.blog.urls', 'blog'))),
    path('users/', include(('devopshobbies.users.urls', 'users'))),
    path('auth/', include(('devopshobbies.authentication.urls', 'auth'))),
]
