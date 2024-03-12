from django.contrib import admin
from . models import Post 
from . models import Comments
from users.models import Student
# Register your models here.

admin.site.register(Post)
admin.site.register(Comments)
admin.site.register(Student)
