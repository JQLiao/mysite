from django.db import models
from mirage import fields

class HostInfo(models.Model):
    __tablename__ = 'host_info'
    ip = models.CharField(max_length=30, verbose_name='IP',default='', unique=True)
    zone = models.CharField(max_length=30, verbose_name='区域', default='')
    status = models.IntegerField(verbose_name='状态', default='')
    # passwd = models.CharField(max_length=30, default='')
    # 加密保存pwd
    passwd = fields.EncryptedCharField()
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['create_time']

    def __str__(self):
        return self.ip