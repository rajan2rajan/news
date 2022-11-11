
from django.contrib import admin
from loginform.models import loginform,login_form

# Register your models here.
class loginform_admin(admin.ModelAdmin):
    list_display =('name','create_password','password', 'email','location')

admin.site.register(loginform ,loginform_admin)



# 2nd 
class login_form_admin(admin.ModelAdmin):
    list_display =('name','create_password','password', 'email','location','news_image')

admin.site.register(login_form ,login_form_admin)