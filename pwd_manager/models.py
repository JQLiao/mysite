from django.db import models
from pwd_manager.fernet_field import AesField

class HostInfo(models.Model):
    __tablename__ = 'host_info'
    ip = models.CharField(max_length=30, verbose_name='IP',default='')
    zone = models.CharField(max_length=30, verbose_name='区域', default='')
    status = models.IntegerField(verbose_name='状态', default='')
    # passwd = models.CharField(max_length=30, default='')
    passwd = AesField(verbose_name='密码')
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['create_time']

    def __str__(self):
        return self.ip