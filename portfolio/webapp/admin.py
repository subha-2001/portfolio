from webapp.models import Webapp
from django.contrib import admin
 
 
@admin.register(Webapp)
class WebappAdmin(admin.ModelAdmin):
 
    class Meta:
       model = Webapp
 