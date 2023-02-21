from django.contrib import admin
from django.urls import path
from .import views
app_name="myapp"
urlpatterns=[
    path('',views.index,name="index"),
    path('create_acnt/',views.create_acnt,name='create_acnt'),
    path('homepage/<int:usr_id>/',views.homepage,name='homepage'),
    path('purchase_premium/<int:usr_id>/',views.purchase_premium,name='purchase_premium'),
    path('remove/<int:post_id>/',views.remove,name='remove'),
    path('remove_audio/<int:audio_id>/',views.remove_audio,name='remove_audio'),
    path('audio_page/<int:usr_id>/',views.audio_page,name='audio_page'),
    path('profile/<int:usr_id>/',views.profile,name='profile'),
    path('common_profile/<int:usr_id>/',views.common_profile,name='common_profile'),
    path('upload_pictures/<int:usr_id>/',views.upload_pictures,name='upload_pictures'),
    path('homepage/<int:usr_id>/like/<int:post_id>/<int:us_id>/',views.like,name='like'),
    path('comment/<int:usr_id>/<int:post_id>/',views.comment,name='comment'),
    path('homepage/<int:usr_id>/comment_upload/<int:post_id>/<int:us_id>/',views.comment_upload,name='comment_upload'),
    path('upload_audio/<int:usr_id>/',views.upload_audio,name='upload_audio'),
    path('audio_comment/<int:usr_id>/<int:audio_id>/',views.audio_comment,name='audio_comment'),
    path('myuploads/<int:usr_id>/',views.myuploads,name='myuploads'),
    
    
]