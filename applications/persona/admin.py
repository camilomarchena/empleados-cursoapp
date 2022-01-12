from django.contrib import admin

from applications.persona.models import Habilidades, empleado

# Register your models here.

admin.site.register(Habilidades)


class empleadoAdmin(admin.ModelAdmin):
    list_display = ('id', 'firstname', 'lastname',
                    'departamento', 'job', 'fullname',)

    def full_name(self, obj):
        return obj.firstname + ' ' + obj.lastname

    search_fields = ('firstname',)
    list_filter = ('job', 'habilidades')
    filter_horizontal = ('habilidades',)


admin.site.register(empleado, empleadoAdmin)
