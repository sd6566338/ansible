from rest_framework import serializers
from cmdb.models import Server,Ticket
from django.contrib.auth.models import User




class ServerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Server
        fields = "__all__"

class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = "__all__"


# class SnippetSerializer(serializers.HyperlinkedModelSerializer):
#     owner = serializers.ReadOnlyField(source='owner.username')
#
#     class Meta:
#         model = Server
#         fields = ('sn','manager_ip','hostname','check','ip','owner','remarks')


# class UserSerializer(serializers.HyperlinkedModelSerializer):
#     snippets = serializers.HyperlinkedRelatedField(many=True, view_name='server-detail', read_only=True)
#
#     class Meta:
#         model = User
#         fields = ('url', 'id', 'username', 'servers')