from django.contrib import admin
from contact_us.models import contact_us,rajan

# Register your models here.
class contact_us_admin(admin.ModelAdmin):
    list_display = ('fname','lname','email','message')
    
admin.site.register(rajan,contact_us_admin)
