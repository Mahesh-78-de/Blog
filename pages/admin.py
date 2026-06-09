# Register your models here.
from django.contrib import admin
from .models import About, Social_links

admin.site.register(Social_links)


class AboutAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        # Allow adding only if there are no existing About instances
        if About.objects.count() == 0:
            return True
        return False
    

admin.site.register(About, AboutAdmin)

