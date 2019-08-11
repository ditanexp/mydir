from django.db import models
from django.contrib.auth.models import AbstractUser



class AbastractModel(models.Model):
    created = models.DateTimeField(u'创建时间', auto_now_add=True)
    modified = models.DateTimeField(u'更新时间', auto_now=True)
    deleted = models.BooleanField(u'己删除', default=False)

    class Meta:
        abstract = True


class ClientUser(AbstractUser):
    username = models.CharField(verbose_name=u'用户名', max_length=100, unique=True)
    email = models.EmailField(verbose_name=u'邮箱', max_length=100)
    phone = models.IntegerField(verbose_name=u'电话', blank=True, null=True)
    dept = models.IntegerField(verbose_name=u'部门', default=0)
    org = models.ForeignKey(ClientOrg, on_delete=models.SET_NULL, null=True, blank=True, related_name='user_org', verbose_name=u'所属组织')
    is_active = models.BooleanField(verbose_name=u'己激活', default=True)
    created = models.DateTimeField(verbose_name=u'创建时间', auto_now_add=True)
    modified = models.DateTimeField(verbose_name=u'更新时间', auto_now=True)
    deleted = models.BooleanField(verbose_name=u'己删除', default=False)
    desc = models.CharField(verbose_name=u'客户信息描述', max_length=100)

    def __str__(self):
        return self.username

