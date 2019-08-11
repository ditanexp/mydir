from django.db import models
from django_fsm import FSMField, transition

TicketLevel = {
    1: 'P1',
    2: 'P2',
    3: 'P3',
    4: 'P4',
    5: 'P5',
}


class TicketRecord(models.Model):
    # 创建工单
    state = FSMField(u'状态', default='new', help_text="工单状态")
    sn = models.CharField(u'流水号', unique=True, max_length=12, help_text="工单的流水号")
    title = models.CharField(u'标题', max_length=50, blank=False, default='', help_text="工单的标题")
    content = models.TextField(u'工单内容', max_length=200, blank=False, default='', help_text="工单内容描述")
    level = models.CharField(max_length=3, choices=tuple(TicketLevel.items()), default=2, verbose_name=u'工单等级')
    creator = models.CharField(u'创建者', max_length=12, blank=False, help_text="工单创建人")
    contact_man = models.CharField(u'告障人', max_length=12, blank=False, help_text="告障或委托人姓名")
    contact_number = models.CharField(u'联系电话', max_length=11, blank=False, help_text="告障或委托人手机号码")
    contact_org = models.CharField(u'告障单位', max_length=50, blank=False, help_text="告障或委托单位")
    gmt_created = models.DateTimeField(u'创建时间', auto_now_add=True)
    # 工单分派，默认为机器人
    assigner = models.CharField(u'调度人', max_length=12, default='ROBOT', help_text="工单分派与调度")
    gmt_assigned = models.DateTimeField(u'指派时间', null=True, auto_now=False)
    # 接受工单
    executor = models.CharField(u'处理人', max_length=12, blank=True, default='', help_text="工单处理人")
    gmt_accepted = models.DateTimeField(u'接受时间', null=True, auto_now=False)
    is_closed = models.BooleanField('已关闭', default=False, help_text='工单是否已关闭')

    #
    def __str__(self):
        return self.sn

    # 处理工单
    class Meta:
        verbose_name = '工单记录'
        verbose_name_plural = '工单记录'

    @transition(field=state, source='new', target='submitted')
    def submit(self):
        """
         提交工单
        """

    @transition(field=state, source='submitted', target='assigned')
    def assign(self):
        """
        分派工单
        """

    @transition(field=state, source='assigned', target='accepted')
    def accept(self):
        """
        确认工单
        """

    @transition(field=state, source='accepted', target='rejected')
    def reject(self):
        """
        拒绝工单
        """

    @transition(field=state, source='accepted', target='finished')
    def finish(self):
        """
        完成工单
        """

    @transition(field=state, source='finished', target='reviewed')
    def review(self):
        """
        完成工单
        """

    @transition(field=state, source='*', target='closed')
    def close(self):
        """
        完成工单
        """



class TicketHandle(models.Model):
    sn = models.ForeignKey(TicketRecord, on_delete=models.SET_NULL, null=True, blank=False, verbose_name=u'工单编号')
    describe = models.TextField(u'需求描述', max_length=50, blank=False, help_text="故障或需求描述")
    reason = models.TextField(u'原因分析', max_length=50, blank=False, help_text="故障或需求原因")
    process = models.TextField(u'处理过程', max_length=200, blank=False, help_text="处理过程")
    advices = models.TextField(u'技术建议', max_length=200, blank=False, help_text="技术优化建议")
    gmt_start = models.DateTimeField(u'开始处理时间', null=False, auto_now=False)
    gmt_done = models.DateTimeField(u'处理完成时间', null=False, auto_now=False)
    gmt_edit = models.DateTimeField(u'最后编辑时间', null=False, auto_now=True)

    class Meta:
        verbose_name = '工单详情'
        verbose_name_plural = '工单详情'

    def __str__(self):
        return self.sn


class TicketReview(models.Model):
    sn = models.ForeignKey(TicketRecord, on_delete=models.SET_NULL, null=True, blank=False, verbose_name=u'工单编号')
    reviewer = models.CharField(u'复核人', max_length=12, blank=True, default='', help_text="工单处理完成后的复核与评价人")
    comments = models.TextField(u'评论', max_length=50, blank=True, default='', help_text="工单复核与评论")
    gmt_edit = models.DateTimeField(u'最后编辑时间', null=False, auto_now=True)

    def __str__(self):
        return self.sn



