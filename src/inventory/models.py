from django.db import models

DATA_SPEED = (
    (0, u'Kbps'),
    (1, u'Mbps'),
    (2, u'Gbps'),
    (3, u'Tbps'),
)

DATA_SIZE = (
    (0, u'KB'),
    (1, u'MB'),
    (2, u'GB'),
    (3, u'TB'),
)

SERVICE_GROUP = (
    (0, u'Infra'),
    (1, u'Business'),
)

HARDWARE_LOCAL = (
    (0, u'CPD1'),
    (1, u'CPD2'),
    (2, u'Deposito'),
)

HARDWARE_STATUS = (
    (0, u'Nao instalado'),
    (1, u'Instalado'),
    (2, u'Em uso'),
    (3, u'Desfazimento')
)

SWITCH_GROUP = (
    (0, u'Edge'),
    (1, u'Core'),
    (2, u'Distribution'),
)


class Enterprise(models.Model):
    name = models.CharField(max_length=50)
    contact = models.CharField(max_length=50, null=True)
    phone = models.CharField(max_length=50)
    mail = models.CharField(max_length=50)

    def __unicode__(self):
        return self.name


class Hardware(models.Model):
    manufacturer = models.ForeignKey(Enterprise, related_name='manufactures', null=True)
    model = models.CharField(max_length=50, null=True)
    provider = models.ForeignKey(Enterprise, related_name='providers', null=True)
    buy = models.DateField(null=True)
    warranty = models.DateField(null=True)
    serial_number = models.CharField(max_length=50, null=True)
    patrimonio = models.CharField(max_length=50, null=True)
    status = models.IntegerField(default=2, choices=HARDWARE_STATUS)
    local = models.IntegerField(default=0, choices=HARDWARE_LOCAL)
    info = models.TextField(null=True)

    def __unicode__(self):
        return self.manufacturer + " " + self.model + " - " + self.patrimonio 


class Server(Hardware):
    processor_model = models.CharField(max_length=30, null=True)
    sockets = models.IntegerField(null=True)
    cores = models.IntegerField(null=True)
    memory_size = models.IntegerField(null=True)
    memory_unit = models.IntegerField(choices=DATA_SIZE, default=2)
    hd_size = models.IntegerField(null=True)
    hd_unit = models.IntegerField(choices=DATA_SIZE, default=2)
    hba_speed = models.IntegerField(default=8, null=True) 
    hba_unit = models.IntegerField(choices=DATA_SPEED, default=2, null=True)
    net_speed = models.IntegerField(default=1, null=True) 
    net_unit = models.IntegerField(choices=DATA_SPEED, default=2, null=True)


class Appliance(Hardware):
    usage = models.CharField(max_length=30, null=True)


class SwitchLAN(Hardware):
    poe = models.BooleanField()
    ports = models.IntegerField(default=48, null=True) 
    group = models.IntegerField(choices=SWITCH_GROUP, default=0, null=True)
    switching_capacity = models.IntegerField(null=True) 
    switching_capacity_unit = models.IntegerField(choices=DATA_SPEED, default=2, null=True)


class Router(Hardware):
    routing_capacity = models.IntegerField(null=True) 
    routing_capacity_unit = models.IntegerField(choices=DATA_SPEED, default=2, null=True)


class SwitchSAN(Hardware):
    ports = models.IntegerField(default=48, null=True) 
    ports_licensed = models.IntegerField(null=True) 


class Storage(Hardware):
    capacity = models.IntegerField(null=True)


class Library(Hardware):
    capacity = models.IntegerField(null=True)


class UPS(Hardware):
    capacity = models.IntegerField(null=True)


class Cooling(Hardware):
    capacity = models.IntegerField(null=True)


class Host(models.Model):
    name = models.CharField(max_length=50)
    so = models.CharField(max_length=50)
    hardware = models.ForeignKey(Hardware)


class CI(models.Model): 
    name = models.CharField(max_length=50)
    doclink = models.URLField(max_length=100)


class Software(CI):
    version = models.CharField(max_length=30)
    host = models.ForeignKey(Host)


class Network(CI):
    hardware = models.ForeignKey(Hardware)


class Data(CI):
    lun = models.CharField(max_length=30)
    size = models.IntegerField()
    hardware = models.ForeignKey(Hardware)


class Service(models.Model):
    name = models.CharField(max_length=50)
    group = models.IntegerField(choices=SERVICE_GROUP)
    dns = models.CharField(max_length=100, null=True)
    ip = models.IPAddressField(null=True)
    #ver como fazer a dependencia com CIs e Services
