from django.contrib import admin
from .models import tessiu,paciente

# Register your models here.
class pacienteAdmin(admin.ModelAdmin):
    list_display = ('nombre',)

admin.site.register(paciente, pacienteAdmin)


class tessiuAdmin(admin.ModelAdmin):
    list_display = ('temperature','color','inflamation')
    search_fields = ('temperature',)
admin.site.register(tessiu, tessiuAdmin)

#admin.site.register(tessiu)