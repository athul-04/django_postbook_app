from django.contrib import admin
from .models import User,UserBio,Uploads,Like,Comment,Audio_uploads

admin.site.register(User)
admin.site.register(UserBio)
admin.site.register(Uploads)
admin.site.register(Like)
admin.site.register(Comment)
admin.site.register(Audio_uploads)
