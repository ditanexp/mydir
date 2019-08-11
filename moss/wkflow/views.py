import datetime

from django.core.exceptions import ObjectDoesNotExist
from rest_framework import viewsets
from rest_framework.response import Response
from .models import TicketRecord
from .serializers import WorkTicketSerializer, TicketCreateSerializer, TicketAssignSerializer, TicketHandleSerializer, \
    TicketReviewSerializer


class APIResponse():
    def __init__(self):
        self.status = 100
        self.msg = None

    @property
    def get_dic(self):
        return self.__dict__

class WorkTicketViewSet(viewsets.ModelViewSet):
    authentication_classes = []
    serializer_class = WorkTicketSerializer
    queryset = TicketRecord.objects.all()

    def create(self, request):
        """
        创建工单
        :param request:
        :return:
        """
        response = APIResponse()
        ticket_ser = TicketCreateSerializer(data=request.data)
        if ticket_ser.is_valid():
            ticket_ser.save()
        else:
            print(ticket_ser)
            response.status = 101
            response.msg = ticket_ser.errors

        return Response(response.get_dic)

    def retrieve(self, request, sn):
        """查询指定工单记录"""
        response = APIResponse()
        sn = request.POST.get('sn', '')
        try:
            ticket = TicketRecord.objects.all().filter(sn=sn).first()
            ticket_ser = WorkTicketSerializer(instance=ticket)
            response.ticket = ticket_ser.data
        except ObjectDoesNotExist as  e:
            response.status = 101
            response.msg = 'sn不存在'
        except Exception as e:
            print(e)
            response.status = 201
            response.msg = str(e)
        return Response(response.get_dic)

    def assign(self, request):
        response = APIResponse()
        sn = request.POST.get('sn', '')
        executor = request.POST.get('executor', '')
        try:
            ticket = TicketRecord.objects.all().filter(sn=sn).first()
            ticket_ser = TicketAssignSerializer(instance=ticket, executor=executor, gmt_assigned=datetime.now())
            if not ticket_ser.is_valid():
                raise Exception('数据校验失败')
            ticket_ser.save()
            response.ticket = ticket_ser.data
            response.msg = '修改成功'
        except ObjectDoesNotExist as  e:
            response.status = 101
            response.msg = 'sn不存在么'
        except Exception as e:
            print(e)
            response.status = 201
            response.msg = str(e)
        return Response(response.get_dic)


