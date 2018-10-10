from rest_framework import serializers
from cmdb.models import Server,Ticket
from django.contrib.auth.models import User




# class ServerSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Server
#         fields = "__all__"
#
# class TicketSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Ticket
#         fields = "__all__"


class ServerSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Server
        fields = ('id','ip','manager_ip','owner','sn','cabinet_list','cabinet_number','cabinet_begin','department','business')


# class UserSerializer(serializers.HyperlinkedModelSerializer):
#     snippets = serializers.HyperlinkedRelatedField(many=True, view_name='server-detail', read_only=True)
#
#     class Meta:
#         model = User
#         fields = ('url', 'id', 'username', 'servers')