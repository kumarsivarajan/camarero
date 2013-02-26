from django.contrib import admin
from inventory.models import Service
from inventory.models import Software
from inventory.models import Network
from inventory.models import Data
from inventory.models import Host
from inventory.models import Server
from inventory.models import Appliance
from inventory.models import SwitchLAN
from inventory.models import Router
from inventory.models import SwitchSAN
from inventory.models import Storage
from inventory.models import Enterprise


class ServerAdmin(admin.ModelAdmin):
    list_display = ('manufacturer', 'model', 'patrimonio')
    fieldsets = (
        ('Hardware', {
            'fields': (
            ('manufacturer', 'model'), 
            ('provider','buy','warranty'),
            ('serial_number', 'patrimonio'),
            ('status', 'local'),
            ('info')
            ) }
        ),
        ('Server', {
            'fields': (
            ('processor_model', 'sockets', 'cores'),
            ('memory_size','memory_unit'),
            ('hd_size','hd_unit'),
            ('hba_speed','hba_unit'),
            ('net_speed','net_unit')
            ) } 
        )
    )

class ApplianceAdmin(admin.ModelAdmin):
    list_display = ('manufacturer', 'model', 'patrimonio')
    fieldsets = (
        ('Hardware', {
            'fields': (
            ('manufacturer', 'model'), 
            ('provider','buy','warranty'),
            ('serial_number', 'patrimonio'),
            ('status', 'local'),
            ('info')
            ) }
        ),
    )

class SwitchLANAdmin(admin.ModelAdmin):
    list_display = ('manufacturer', 'model', 'patrimonio')
    fieldsets = (
        ('Hardware', {
            'fields': (
            ('manufacturer', 'model'), 
            ('provider','buy','warranty'),
            ('serial_number', 'patrimonio'),
            ('status', 'local'),
            ('info')
            ) }
        ),
        ('Switch', {
            'fields' : (
            (('group', 'ports','poe'))
            ) }
        )
    )

class RouterAdmin(admin.ModelAdmin):
    list_display = ('manufacturer', 'model', 'patrimonio')
    fieldsets = (
        ('Hardware', {
            'fields': (
            ('manufacturer', 'model'), 
            ('provider','buy','warranty'),
            ('serial_number', 'patrimonio'),
            ('status', 'local'),
            ('info')
            ) }
        ),
    )

class SwitchSANAdmin(admin.ModelAdmin):
    list_display = ('manufacturer', 'model', 'patrimonio')
    fieldsets = (
        ('Hardware', {
            'fields': (
            ('manufacturer', 'model'), 
            ('provider','buy','warranty'),
            ('serial_number', 'patrimonio'),
            ('status', 'local'),
            ('info')
            ) }
        ),
        ('Switch', {
            'fields' : (
            ('ports','ports_licensed')
            ) }
        )
    )

class StorageAdmin(admin.ModelAdmin):
    list_display = ('manufacturer', 'model', 'patrimonio')
    fieldsets = (
        ('Hardware', {
            'fields': (
            ('manufacturer', 'model'), 
            ('provider','buy','warranty'),
            ('serial_number', 'patrimonio'),
            ('status', 'local'),
            ('info')
            ) }
        ),
        ('Storage', {
            'fields' : (
            ('capacity'),
            ) }
        )
    )


admin.site.register(Service)
admin.site.register(Software)
admin.site.register(Network)
admin.site.register(Data)
admin.site.register(Host)
admin.site.register(Enterprise)
admin.site.register(Server, ServerAdmin)
admin.site.register(Appliance, ApplianceAdmin)
admin.site.register(SwitchLAN, SwitchLANAdmin)
admin.site.register(Router, RouterAdmin)
admin.site.register(SwitchSAN, SwitchSANAdmin)
admin.site.register(Storage, StorageAdmin)
