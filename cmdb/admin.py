#_*_coding:utf-8_*_
from daterange_filter.filter import DateRangeFilter
from models import Server, HostGroup, Record, Blogs, Ticket, Disk, Disk_rec, Nic, Nic_rec, Memery, Memery_rec, Contract, Menber, Ivn_server, Inventory
from django.contrib import admin
from django.contrib import admin
##########
from django.contrib.admin import SimpleListFilter

def make_false(modelAdmin, request, queryset): #queryset：选中的集合；modelAdmin代表BookAdmin类,相当于self
    make_false.short_description = "设置为未完成"
#    print("----->", modelAdmin,request,queryset)
    queryset.update(ticket_state=0) #更改选中的为禁书

def make_ture(modelAdmin, request, queryset): #queryset：选中的集合；modelAdmin代表BookAdmin类,相当于self
    make_ture.short_description = "设置为已完成"
    queryset.update(ticket_state=1) #更改选中的为禁书

def make_on(modelAdmin, request, queryset): #queryset：选中的集合；modelAdmin代表BookAdmin类,相当于self
    make_ture.short_description = "设置为监控"
    queryset.update(check=1) #更改选中的为禁书

def make_off(modelAdmin, request, queryset): #queryset：选中的集合；modelAdmin代表BookAdmin类,相当于self
    make_ture.short_description = "设置为不监控"
    queryset.update(check=0) #更改选中的为禁书
#class RecordInline(admin.StackedInline): //占屏模式
class RecordInline(admin.TabularInline):
    model = Record
    extra = 1
class Disk_recInline(admin.TabularInline):
    model = Disk_rec
    extra = 1
class Memery_recInline(admin.TabularInline):
    model = Memery_rec
    extra = 1
class Nic_recInline(admin.TabularInline):
    model = Nic_rec
    extra = 1

class RecordAdmin(admin.ModelAdmin):
    list_display = [
    'fault_type', 'state', 'discover_time', 'report_time', 'report_person', 'end_time', 'repair_person', 'res', 'memo'
    ]
class MenberAdmin(admin.ModelAdmin):
    list_display = [
    'name', 'phone', 'email'
    ]
class TicketAdmin(admin.ModelAdmin):
    actions = [make_ture, make_false]
    list_display = [
    'ticket_content','ticket_time', 'ticket_type', 'executor', 'get_menber','related_servers','server_number','ticket_state','end_time'
    ]
    search_fields = ['related_servers','remark','ticket_content', 'ticket_type', 'executor', 'menber__name', 'ticket_state']
    list_filter = [('ticket_time', DateRangeFilter),'ticket_type','executor','menber__name']
 
class DiskAdmin(admin.ModelAdmin):
    list_display = [
    'disk_type','disk_rev','disk_size','disk_product','disk_num','create_time','remark'
    ]
    inlines = [Disk_recInline]
class MemeryAdmin(admin.ModelAdmin):
    list_display = [
    'mem_type','mem_size','mem_product','mem_num','mem_create_time','mem_remark'
    ]
    inlines = [Memery_recInline]
class NicAdmin(admin.ModelAdmin):
    list_display = [
    'nic_speed','nic_type','nic_pci','nic_num','nic_create_time','nic_remark'
    ]
    inlines = [Nic_recInline]
class ContractAdmin(admin.ModelAdmin):
    list_display = [
    'cname','csn','jiafang','yifang','producer','conf','price','detail','file','contract_begin_date','contract_end_date','begin_date','end_date'
    ]
#    inlines = [Inline]
class Ivn_serverAdmin(admin.ModelAdmin):
    list_display = [
    'sn',
    'brand',
    'types',
    'change_time',
    'change_stat',
    'rec_person',
    'change_num',
#    'ivn_num',
    'contract',
    'remarks'
    ]
    fieldsets = [
        ('带外信息', { 'fields': ['sn','brand','types','change_time','change_stat','rec_person','change_num','contract', 'remarks' ]}),
    ]
    search_fields = ['sn']

class InventoryAdmin(admin.ModelAdmin):
    list_display = [
    'sn',
    'brand',
    'types',
    'contract',
    'remarks'
    ]
    fieldsets = [
        ('带外信息', { 'fields': ['sn','brand','types','contract', 'remarks' ]}),
    ]
    search_fields = ['sn']

class ServerAdmin(admin.ModelAdmin):
    list_display = [
    'sn',
    'manager_ip',
#    'ip',
#    'ip_2',
    'check',
    'types',
    'idc_mod',
    'cabinet_list',
    'cabinet_number',
    'cabinet_begin',
#    'create_date',
#    'department',
#    'contract',
    'owner',
#    'status',
    'department',
    'business',
#    'remarks'
    ]
    fieldsets = [
        ('带外信息', { 'fields': ['sn', 'manager_ip', 'ip','idc_mod','cabinet_list','cabinet_number', 'cabinet_begin', 'contract', 'remarks' ]}),
        ('详细信息', {'classes' : ('collapse',),'fields': ['check', 'hostname', 'owner', 'department', 'business']}),
    ]
    actions = [make_on, make_off]
    search_fields = ['sn', 'ip', 'manager_ip', 'business', 'remarks']
    list_filter = ['idc_mod', 'cabinet_list','department','owner','business','types']
    inlines = [RecordInline]
#    date_hierarchy = 'create_date'
#    ordering = ('-create_date',)
    
class HostGroupAdmin(admin.ModelAdmin):
    list_display = ['name']

class BlogPostAdmin(admin.ModelAdmin):
    list_display = ['title','timestamp','author']



admin.site.register(Server, ServerAdmin)
admin.site.register(Record, RecordAdmin)
admin.site.register(Contract, ContractAdmin)
admin.site.register(Ticket, TicketAdmin)
admin.site.register(Disk, DiskAdmin)
admin.site.register(Nic, NicAdmin)
admin.site.register(Memery, MemeryAdmin)
admin.site.register(Blogs ,BlogPostAdmin)
admin.site.register(Menber ,MenberAdmin)
admin.site.register(Ivn_server, Ivn_serverAdmin)
admin.site.register(Inventory, InventoryAdmin)
