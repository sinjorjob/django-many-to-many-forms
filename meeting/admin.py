from django.contrib import admin

from .models import Agenda, Member

class  MemberAdmin(admin.ModelAdmin):
    list_display=('pk','user', 'member_name', 'email')

class AgendaAdmin(admin.ModelAdmin):
    list_display=('pk','title', 'contents', 'date')


admin.site.register( Member,  MemberAdmin)
admin.site.register(Agenda, AgendaAdmin)
