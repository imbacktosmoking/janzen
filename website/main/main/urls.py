from django.contrib import admin
from django.urls import path, include
from hanashiai_web.views import Homepage 
from hanashiai_web.views import Submit_post
from hanashiai_web.views import Post_details 
from hanashiai_web.views import Post_comments, About
from django.conf import settings
from django.conf.urls.static import static 



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Homepage.as_view(), name="homepage"),
    path('submit_post/', Submit_post.as_view(), name="submit_post"),
    path('post_details/<int:pk>', Post_details.as_view(), name="post_details"),
    #path('post_comment/<int:pk>',  Post_comments.as_view(), name="post_comments"),
    path('post_comments/<int:pk>/', Post_comments.as_view(), name="post_comments"),
    path('about/', About.as_view(), name="about"),
    path('users/', include('django.contrib.auth.urls')),
    path('users', include('users.urls')), 
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
