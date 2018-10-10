#coding:utf-8
from django.db import models
from datetime import date
import datetime

#from django.contrib import admin
#class Question(models.Model):
#    question_text = models.CharField(max_length=200)
#    pub_date = models.DateTimeField('date published')
#    def __unicode__(self):
#        return self.question_text
#    def was_published_recently(self):
#        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

# Create your models here.

class Calendar(models.Model):
    datelist = models.DateField(u'日期')
    duty_day = models.CharField(u'白班',max_length = 20, blank=True, null=True)
    duty_night = models.CharField(u'夜班',max_length = 20, blank=True, null=True)
    class Meta:
        verbose_name = 'datelist'
        verbose_name_plural = 'datelist'
    def __unicode__(self):
        return self.datelist

class Blogs(models.Model):
    reports = (
        (u'苏建', u'苏建'),
        (u'陈桥', u'陈桥'),
        (u'徐松', u'徐松'),
        (u'吴磊', u'吴磊'),
        (u'沈阳', u'沈阳'),
        (u'李君', u'李君'),
        (u'吴祖兵', u'吴祖兵'),
    )
    title = models.CharField(u'标题',max_length = 150)
    body = models.TextField(u'正文')
    timestamp = models.DateTimeField(u'时间')
    author = models.CharField(u'作者',max_length=64, choices=reports, blank=True, null=True)
    class Meta:
        verbose_name = 'blogs'
        verbose_name_plural = 'blogs'
    def __unicode__(self):
        return self.title

#####Disk_record#####
class Disk(models.Model):
    types = (
        ('SAS', 'SAS'),
        ('SATA', 'SATA'),
        ('SSD', 'SSD'),
        ('PCIE', 'PCIE'),
    )
    revs = (
        ('7.2k', '7.2k'),
        ('10k', '10k'),
        ('15k', '15k'),
        ('others', 'others'),
    )
    sizes = (
        ('400G', '400G'),
        ('480G', '480G'),
        ('600G', '600G'),
        ('900G', '900G'),
        ('1T', '1T'),
        ('1.2T', '1.2T'),
        ('1.5T', '1.5T'),
        ('1.8T', '1.8T'),
        ('2T', '2T'),
        ('3.2T', '3.2T'),
        ('4T', '4T'),
        ('6.4T', '6.4T'),
    )

    products = (
        ('dell', 'Dell'),
        ('HP', 'HP'),
        ('huawei', 'Huawei'),
        ('others', 'others'),
    )
    disk_type = models.CharField(u'硬盘类型',max_length = 64, choices=types,blank=True, null=True)
    disk_rev = models.CharField(u'硬盘转速',max_length = 64, choices=revs,blank=True, null=True)
    disk_size = models.CharField(u'磁盘容量',max_length = 12, choices=sizes,blank=True, null=True)
    disk_product = models.CharField(u'厂商',max_length = 64, choices=products,blank=True, null=True)
    disk_num = models.IntegerField(u'总量',blank=True, null=True)
    create_time = models.DateTimeField(u'时间',blank=True, null=True)
    remark = models.TextField(u'备注',blank=True, null=True)
    class Meta:
        verbose_name = '硬盘'
        verbose_name_plural = '硬盘'
    def __unicode__(self):
        return self.disk_size


#####Memery_record#####
class Memery(models.Model):
    mem_types = (
        ('ddr4', 'ddr4'),
    )
    mem_sizes = (
        ('8G', '8G'),
        ('16G', '16G'),
        ('32G', '32G'),
    )

    mem_products = (
        ('dell', 'Dell'),
        ('HP', 'HP'),
        ('huawei', 'Huawei'),
        ('others', 'others'),
    )
    mem_type = models.CharField(u'内存类型',max_length = 64, choices=mem_types,blank=True, null=True)
    mem_size = models.CharField(u'内存容量',max_length = 12, choices=mem_sizes,blank=True, null=True)
    mem_product = models.CharField(u'厂商',max_length = 64, choices=mem_products,blank=True, null=True)
    mem_num = models.IntegerField(u'总量',blank=True, null=True)
    mem_create_time = models.DateTimeField(u'时间',blank=True, null=True)
    mem_remark = models.TextField(u'备注',blank=True, null=True)
    class Meta:
        verbose_name = '内存'
        verbose_name_plural = '内存'
    def __unicode__(self):
        return self.mem_size


#####network_card_record#####
class Nic(models.Model):
    speeds = (
        ('1000Mbps/s', '1000Mbps/s'),
        ('10000Mbps/s', '10000Mbps/s'),
    )
    nic_types = (
        (u'光口', u'光口'),
        (u'电口', u'电口'),
    )
    pcis = (
        (u'PCI-长', u'PCI-长'),
        (u'PCI-短', u'PCI-短'),
    )
    nic_speed = models.CharField(u'网卡速率',max_length = 64, choices=speeds, blank=True, null=True)
    nic_type = models.CharField(u'网卡类型',max_length = 12, choices=nic_types, blank=True, null=True)
    nic_pci = models.CharField(u'PCI卡类型',max_length = 12, choices=pcis,blank=True, null=True)
    nic_num = models.IntegerField(u'网卡总量',blank=True, null=True)
    nic_create_time = models.DateTimeField(u'时间',blank=True, null=True)
    nic_remark = models.TextField(u'备注',blank=True, null=True)
    class Meta:
        verbose_name = '网卡'
        verbose_name_plural = '网卡'
    def __unicode__(self):
        return self.nic_type

class Menber(models.Model):
    name = models.CharField(u'姓名',max_length = 30, blank=True)
    phone = models.CharField(u'电话',max_length = 30, blank=True)
    email = models.EmailField(u'Email',max_length = 64, blank=True)
    class Meta:
        verbose_name = '成员'
        verbose_name_plural = '成员'
    def __unicode__(self):
        return self.name
#    def __str__(self):
#        return "<%s>" % self.name

class Ticket(models.Model):
    menbers = (
        (u'苏建', u'苏建'),
        (u'陈桥', u'陈桥'),
        (u'徐松', u'徐松'),
        (u'吴磊', u'吴磊'),
        (u'沈阳', u'沈阳'),
        (u'李君', u'李君'),
        (u'吴祖兵', u'吴祖兵'),
    )
    ticket_sources = (
        (u'报修跟进', u'报修跟进'),
        (u'客服传达', u'客服传达'),
        (u'上级安排', u'上级安排'),
        (u'客户对接', u'客户对接'),
    )
    ticket_types = (
        (u'定时巡检', u'定时巡检'),
        (u'告警记录', u'告警通报(工单)'),
        (u'系统安装', u'系统安装(工单)'),
        (u'协助处理(工单)', u'协助处理(工单)'),
        (u'设备迁移', u'设备迁移(变更)'),
#        (u'设备报修', u'设备报修(工单)'),
        (u'系统配置', u'系统配置(变更)'),
        (u'设备维修', u'设备维修(变更)'),
        (u'设备上架', u'设备上架(变更)'),
        (u'设备下架', u'设备下架(变更)'),
        (u'增加备件', u'增加备件(变更)'),
        (u'移除备件', u'移除备件(变更)'),
        (u'协助处理(变更)', u'协助处理(变更)'),
        (u'技术研究', u'技术研究'),
    )
    ticket_groups = (
        (u'系统组', u'系统组'),
        (u'网络组', u'网络组'),
    ) 
    ticket_status = (
        (u'处理中', u'处理中'),
        (u'已完成', u'已完成'),
    )
    ticket_content = models.CharField(u'内容描述(注:所有变更单需提交DCIM系统;)',max_length = 300, blank=True, null=True)
    ticket_group = models.CharField(u'工单分组',max_length = 30, choices=ticket_groups, blank=True, default='系统组')
    ticket_source = models.CharField(u'工单来源',max_length = 30, choices=ticket_sources, blank=True, null=True)
    ticket_time = models.DateTimeField(u'开始时间',blank=True, null=True)
    ticket_type = models.CharField(u'工单类型',max_length = 30, choices=ticket_types, blank=True, null=True)
    ticket_id = models.CharField(u'变更单号(DCIM系统上的变更单号)',max_length = 30, blank=True, default='若为变更单，请输入DCIM上的变更单号')
    related_servers = models.CharField(u'涉及设备SN(多台请用空格隔开)',max_length = 300, blank=True, null=True)
    server_number = models.IntegerField(u'涉及设备数量', blank=True, null=True,default= 1)
#    ticket_state = models.CharField(u'工单状态',max_length = 30, choices=ticket_status, blank=True, null=True, default='处理中')
#    menber = models.CharField(u'处理人',max_length=64, blank=True, null=True)
#    menber = models.ManyToManyField('Menber' , blank=True)
    executor = models.CharField(u'执行人',max_length = 30, choices=menbers, blank=True)
    menber = models.ManyToManyField('Menber', verbose_name=u'协助处理人', blank=True)
    ticket_state = models.BooleanField(u'是否完成', default=False,)
    end_time = models.DateTimeField(u'完成时间', blank=True, null=True)
    remark = models.TextField(u'备注', blank=True, null=True)


    def get_menber(self):
        return "\n".join([m.name for m in self.menber.all()])

    class Meta:
        verbose_name = '工单记录'
        verbose_name_plural = '工单记录'
    def __unicode__(self):
        return self.ticket_content

class Ivn_server(models.Model):
    server_ress = (
        (u'出库', u'出库'),
        (u'入库', u'入库'),
    )
    sn = models.CharField(u'资产SN号',max_length=128,blank=True, null=True)
    brand = models.CharField(u'品牌',max_length=20,blank=True,null=True)
    types = models.CharField(u'典配类型',max_length=20,blank=True,null=True)
    contract = models.ForeignKey('Contract', verbose_name=u'合同', null=True, blank=True)
    change_time = models.DateTimeField(u'出/入库时间', null=True, blank=True)
    change_stat = models.CharField(u'出/入库记录', choices=server_ress, max_length=32, blank=True, null=True)
    rec_person = models.CharField(u'记录人',max_length=64, blank=True,null=True)
    change_num = models.IntegerField(u'出/入数量', blank=True, null=True)
#    ivn_num = models.IntegerField(u'库存数量', blank=True, null=True)
    remarks = models.CharField(u'备注',max_length=200, blank=True, null=True, default='None')
    class Meta:
        verbose_name = '服务器出入库记录'
        verbose_name_plural = '服务器出入库记录'

    def __unicode__(self):
        return self.types

class Inventory(models.Model):
    sn = models.CharField(u'资产SN号',max_length=128,blank=True, null=True)
    brand = models.CharField(u'品牌',max_length=20,blank=True,null=True)
    types = models.CharField(u'典配类型',max_length=20,blank=True,null=True)
    contract = models.ForeignKey('Contract', verbose_name=u'合同', null=True, blank=True)
#    ivn_num = models.IntegerField(u'库存数量', blank=True, null=True)
    remarks = models.CharField(u'备注',max_length=200, blank=True, null=True, default='None')
    class Meta:
        verbose_name = '服务器库存'
        verbose_name_plural = '服务器库存'

    def __unicode__(self):
        return self.types


class Server(models.Model):
    contracts=(
        (u'合同A', u'合同A'),
        (u'合同B', u'合同B'),
        (u'合同C', u'合同C'),
        (u'合同D', u'合同D'),
    )
#    business_lines = [
#        ('A', u'新飞凡'),
#        ('B', u'公共平台'),
#        ('C', u'大数据'),
#        ('D', u'征信平台'),
#        ('E', u'院线'),
#        ('F', u'块钱'),
#        ('G', u'其他'),
#    ]
    statuss = (
        ( u'使用中', u'使用中'),
        ( u'下架', u'下架'),
    )
    physical = (
        (u'物理机', u'物理机'),
        (u'虚拟机',  u'虚拟机'),
    )
    cabinet_lists = (
        ('A', 'A'),
        ('B', 'B'),
        ('C', 'C'),
        ('D', 'D'),
        ('E', 'E'),
        ('F', 'F'),
    )
    model_numbers = (
        ('Mod1', 'Mod1'),
        ('Mod2', 'Mod2'),
        ('Mod3', 'Mod3'),
        ('Mod4', 'Mod4'),
        ('Ecc', u'Ecc'),
    )
    os_types = (
        ('Windows', 'Windows'),
        ('CentOS', 'CentOS'),
        ('RedHat', 'RedHat'),
        ('Esxi', 'Esxi'),
        ('Others', 'Others'),
    )

    cabinet_numbers = (
         ('1', '1'),
         ('2', '2'),
         ('3', '3'),
         ('4', '4'),
    )

    sn = models.CharField(u'资产SN号',max_length=128,blank=True, null=True)
    types = models.CharField(u'典配类型',max_length=64,blank=True, null=True)
    product = models.CharField(u'生产厂商', max_length=20,blank=True)
    contract = models.ForeignKey('Contract', verbose_name=u'合同', null=True, blank=True)
    manager_ip = models.GenericIPAddressField(u'带外管理',max_length=20,blank=True,null=True)
    idc_mod = models.CharField(u'模块机房',max_length=10, choices=model_numbers, blank=True, null=True)
    cabinet_list = models.CharField(u'机柜列',max_length=32, choices=cabinet_lists, default='A',null=True,blank=True)
    cabinet_number = models.CharField(u'机柜号',max_length=10, blank=True, null=True)
    cabinet_begin = models.CharField(u'起始U位',max_length=32, blank=True, null=True)
#    password = models.CharField(u'密码',max_length=64,null=True,blank=True)
    hostname = models.CharField(u'主机名',max_length=30, null=True,blank=True)
    check = models.BooleanField(u'是否监控',default=False)
#    health = models.BooleanField(u'健康状态',default=True)
#    cabinet_end = models.CharField(u'结束U位',max_length=2, blank=True, null=True)
    ip = models.GenericIPAddressField(max_length=20, null=True,blank=True)
#    ip_2 = models.GenericIPAddressField(max_length=20, null=True,blank=True)
#    status = models.CharField(u'服务器状态',max_length=64, choices=statuss, default='enable', blank=True, null=True)
#    os = models.CharField(u'操作系统',max_length=30,choices=os_types, blank=True, null=True)
#    release = models.CharField(u'版本号',max_length=20, blank=True, null=True)
    owner  = models.CharField(u'接口人',max_length=128, blank=True, null=True)
#    onsale = models.DateField(("Date"), default=date.today)
#    create_date = models.DateField(u'上架时间', default=date.today, blank=True, null=True)
#    update_date = models.DateTimeField(u'检查时间',blank=True, auto_now=True, null=True)
#    machine_type = models.CharField(u'机器类型',max_length=20, choices=physical, default='physical', blank=True, null=True)
    department = models.CharField(u'部门',max_length=128, blank=True, null=True)
    business = models.CharField(u'业务',max_length=50, blank=True, null=True, default='None')
    remarks = models.CharField(u'备注',max_length=200, blank=True, null=True, default='None')
    class Meta:
        verbose_name = '服务器'
        verbose_name_plural = '服务器'
    def __unicode__(self):
        return self.sn

class Contract(models.Model):
    cname = models.CharField(u'合同名称', max_length=256, blank=True, null=True)
    csn = models.CharField(u'合同号', max_length=128,blank=True, null=True)
    jiafang = models.CharField(u'甲方', max_length=128, blank=True, null=True)
    yifang = models.CharField(u'乙方', max_length=128, blank=True, null=True)
    producer = models.CharField(u'厂商', max_length=128, blank=True, null=True)
    conf = models.CharField(u'典配单', max_length=128, blank=True, null=True)
#    gongfang = models.CharField(u'供方', max_length=64, blank=True, null=True)
    price = models.FloatField(u'合同金额', blank=True, null=True)
    detail = models.TextField(u'合同详细',blank=True, null=True)
    file = models.FileField(u'附件',null=True, blank=True, upload_to='upload/contract')
    contract_begin_date = models.DateField(u'合同生效日期', blank=True, null=True)
    contract_end_date = models.DateField(u'合同结束日期', blank=True, null=True)
    begin_date = models.DateField(u'保修开始日期', blank=True, null=True)
    end_date = models.DateField(u'保修结束日期', blank=True, null=True)

    class Meta:
        verbose_name = '合同'
        verbose_name_plural = "合同"
    def __unicode__(self):
        return self.cname


class HostGroup(models.Model):
    name = models.CharField(max_length=30)
    members = models.ManyToManyField(Server)
    class Meta:
        verbose_name = '服务器分组'
        verbose_name_plural = '服务器分组'
    def __unicode__(self):
        return self.name

#class Choice(models.Model):
#    question = models.ForeignKey(Server)
#    choice_text = models.CharField(max_length=200)
#    votes = models.IntegerField(default=0)
#    def __unicode__(self):
#        return self.choice_text

class Record(models.Model):
    statuss = (
        ('A', u'已报修，等待厂商派单'),
        ('G', u'已派单，缺配件'),
        ('B', u'确认交付人'),
        ('C', u'确认停机维护时间'),
        ('D', u'暂时不能停机'),
        ('E', u'维修后，故障依然存在'),
        ('F', u'完成，故障解除'),
    )
    fault_types = (
        (u'硬盘', u'硬盘'),
        (u'内存', u'内存'),
        (u'阵列卡', u'阵列卡'),
        (u'主板', u'主板'),
        (u'电源', u'电源'),
        (u'其他', u'其他'),
    )
    reports = (
        (u'苏建', u'苏建'),
        (u'陈桥', u'陈桥'),
        (u'徐松', u'徐松'),
        (u'吴磊', u'吴磊'),
        (u'沈阳', u'沈阳'),
        (u'李君', u'李君'),
        (u'吴祖兵', u'吴祖兵'),
    )
    ress = (
        (u'成功', u'成功'),
        (u'失败', u'失败'),
    )
    server = models.ForeignKey(Server)
#    fault_descrip = models.CharField(u'故障描述',max_length=120, blank=True, null=True,)
    fault_type = models.CharField(u'故障类型',max_length=64, choices=fault_types, blank=True, null=True, default='')
    state = models.CharField(u'处理状态',max_length=64, choices=statuss, blank=True, null=True, default='')
    discover_time = models.DateTimeField(u'发现故障时间', blank=True,null=True)
    report_time = models.DateTimeField(u'报修时间',blank=True,null=True)
    report_person = models.CharField(u'报修人',max_length=64, choices=reports, blank=True, null=True)
    end_time = models.DateTimeField(u'处理故障时间',blank=True,null=True)
    repair_person = models.CharField(u'处理人',max_length=64, choices=reports, blank=True, null=True)
    res = models.CharField(u'处理结果', choices=ress, max_length=6, blank=True, null=True)
    memo = models.CharField(u'结果备注',max_length=120, blank=True, null=True)
    class Meta:
        verbose_name = '维修记录'
        verbose_name_plural = '维修记录'
    def __unicode__(self):
        return self.state

###########
class Disk_rec(models.Model):
    recs = (
        (u'苏建', u'苏建'),
        (u'陈桥', u'陈桥'),
        (u'徐松', u'徐松'),
        (u'吴磊', u'吴磊'),
        (u'沈阳', u'沈阳'),
        (u'李君', u'李君'),
        (u'吴祖兵', u'吴祖兵'),
    )
    disk_ress = (
        (u'出库', u'出库'),
        (u'入库', u'入库'),
    )
    server = models.ForeignKey(Disk)
    change_time = models.DateTimeField(u'出/入库时间', blank=True,null=True)
    change_stat = models.CharField(u'出/入库记录', choices=disk_ress, max_length=32, blank=True, null=True)
    related_servers = models.CharField(u'关联设备(多台请用","隔开)',max_length = 300, blank=True, null=True)
    rec_person = models.CharField(u'记录人',max_length=64, choices=recs, blank=True, null=True)
    disk_change = models.IntegerField(u'出/入数量', blank=True, null=True)
    disk_num = models.IntegerField(u'现有库存', blank=True, null=True)
    memo = models.CharField(u'结果备注',max_length=120, blank=True, null=True)
    class Meta:
        verbose_name = '硬盘库存记录'
        verbose_name_plural = '硬盘库存记录'
    def __unicode__(self):
        return self.disk_num

###########
class Memery_rec(models.Model):
    recs = (
        (u'苏建', u'苏建'),
        (u'陈桥', u'陈桥'),
        (u'徐松', u'徐松'),
        (u'吴磊', u'吴磊'),
        (u'沈阳', u'沈阳'),
        (u'李君', u'李君'),
        (u'吴祖兵', u'吴祖兵'),
    )
    memrecs = (
        (u'出库', u'出库'),
        (u'入库', u'入库'),
    )
    server = models.ForeignKey(Memery)
    change_time = models.DateTimeField(u'出/入库时间', blank=True,null=True)
    change_stat = models.CharField(u'出/入库记录', choices=memrecs, max_length=32, blank=True, null=True)
    related_servers = models.CharField(u'关联设备(多台请用","隔开)',max_length = 300, blank=True, null=True)
    rec_person = models.CharField(u'记录人',max_length=64, choices=recs, blank=True, null=True)
    memery_change = models.IntegerField(u'出/入数量', blank=True, null=True)
    memery_num = models.IntegerField(u'现有库存', blank=True, null=True)
    memo = models.CharField(u'结果备注',max_length=120, blank=True, null=True)
    class Meta:
        verbose_name = '内存库存记录'
        verbose_name_plural = '内存库存记录'
    def __unicode__(self):
        return self.memery_num

###########
class Nic_rec(models.Model):
    recs = (
        (u'苏建', u'苏建'),
        (u'陈桥', u'陈桥'),
        (u'徐松', u'徐松'),
        (u'吴磊', u'吴磊'),
        (u'沈阳', u'沈阳'),
        (u'李君', u'李君'),
        (u'吴祖兵', u'吴祖兵'),
    )
    nic_ress = (
        (u'出库', u'出库'),
        (u'入库', u'入库'),
    )
    server = models.ForeignKey(Nic)
#    fault_descrip = models.CharField(u'故障描述',max_length=120, blank=True, null=True,)
    change_time = models.DateTimeField(u'出/入库时间', blank=True,null=True)
    change_stat = models.CharField(u'出/入库记录', choices=nic_ress, max_length=32, blank=True, null=True)
    related_servers = models.CharField(u'关联设备(多台请用","隔开)',max_length = 300, blank=True, null=True)
    rec_person = models.CharField(u'记录人',max_length=64, choices=recs, blank=True, null=True)
    nic_change = models.IntegerField(u'出/入数量', blank=True, null=True)
    nic_num = models.IntegerField(u'现有库存', blank=True, null=True)
    memo = models.CharField(u'备注',max_length=120, blank=True, null=True)
    class Meta:
        verbose_name = '网卡库存记录'
        verbose_name_plural = '网卡库存记录'
    def __unicode__(self):
        return unicode(self.nic_num)


#class Connect(models.Model):
#    server = models.ForeignKey(Server, null=True)
#    memo = models.TextField(u'备注', blank=True, null=True)
