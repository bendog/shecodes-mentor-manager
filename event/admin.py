from django.contrib import admin

from .models import Event, EventModule, EventModuleRole, Module, Role

# Register your models here.

admin.site.register(Event)
admin.site.register(Role)
admin.site.register(Module)
admin.site.register(EventModule)


@admin.register(EventModuleRole)
class EventModuleRoleAdmin(admin.ModelAdmin):
    list_display = (
        "event_module",
        "role",
        "mentor",
        "gift_back",
    )
    list_filter = (
        "gift_back",
        ("mentor", admin.EmptyFieldListFilter),
    )
