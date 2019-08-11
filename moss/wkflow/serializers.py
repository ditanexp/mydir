from rest_framework import serializers
from .models import TicketRecord, TicketHandle, TicketReview


class WorkTicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = TicketRecord
        fields = '__all__'


#
# 'state', 'sn', 'title', 'contact_man', 'contact_number', 'contact_org', 'creator', 'assigner', 'executor',
# 'reviewer', 'gmt_created', 'gmt_assigned',
# 'gmt_accepted', 'gmt_finished', 'gmt_closed')
class TicketCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = TicketRecord
        fields = ('state', 'sn', 'title', 'contact_man', 'contact_number', 'contact_org', 'assigner')


class TicketAssignSerializer(serializers.ModelSerializer):
    class Meta:
        model = TicketRecord
        fields = ('sn', 'executor')


class TicketHandleSerializer(serializers.ModelSerializer):
    class Meta:
        model = TicketHandle
        fields = '__all__'


class TicketReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = TicketReview
        fields = '__all__'
