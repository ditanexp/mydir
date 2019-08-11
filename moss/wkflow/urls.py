from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import WorkTicketViewSet
from django.conf.urls import url

router = DefaultRouter()
router.register('WorkTicket', WorkTicketViewSet, 'WorkTicket')
urlpatterns = [
    url(r'list/', WorkTicketViewSet.as_view({'get':'list'}), name='listTicket'),
    url(r'ticket/', WorkTicketViewSet.as_view({'get':'retrieve','post':'create', 'put':'ticketedit', 'delete':'destroy'}), name='Ticket'),
    url(r'assign/(?P<sn>\d+)', WorkTicketViewSet.as_view({'post':'assgin', 'put':'reassign'}), name='AssignTicket'),
    url(r'accept/(?P<sn>\d+)', WorkTicketViewSet.as_view({'post':'accept'}), name='AcceptTicket'),
    url(r'reject/(?P<sn>\d+)', WorkTicketViewSet.as_view({'post':'reject'}), name='RejectTicket'),
    url(r'handledetail/(?P<sn>\d+)', WorkTicketViewSet.as_view({'get':'handledetail','post':'done','put':'updatedetail'}), name='HandleDetail'),
    url(r'close/(?P<sn>\d+)', WorkTicketViewSet.as_view({'post':'close'}), name='CloseTicket'),
    url(r'review/(?P<sn>\d+)', WorkTicketViewSet.as_view({'post':'review', 'put':'updatereview'}), name='ReviewTicket'),
]

urlpatterns += router.urls
