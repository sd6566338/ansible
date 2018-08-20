#coding:utf8
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import datetime
import json
from django.shortcuts import render,render_to_response

# from rest_framework.renderers import JSONRenderer
# from rest_framework.parsers import JSONParser
# from cmdb.models import Server
# from cmdb.serializers import SnippetSerializer
###################
# from rest_framework import status
# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# from cmdb.models import Server
# from cmdb.serializers import SnippetSerializer
##################
# from cmdb.models import Server
# from cmdb.serializers import SnippetSerializer
# from django.http import Http404
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status
# from django.contrib.auth.models import User
from rest_framework import mixins
from cmdb.models import Server,Ticket
from cmdb.serializers import ServerSerializer,TicketSerializer
from rest_framework import generics
from rest_framework import viewsets
import django_filters.rest_framework
from django_filters.rest_framework import DjangoFilterBackend
###
from cmdb.ansible_api import ANSRunner


@csrf_exempt
def Post_test(request):
    if request.method == "POST":
        res = {}
        jobs = request.body
        print jobs
        init_jobs = json.loads(jobs)
        print type(init_jobs)
        # print init_jobs
        taskID = init_jobs[0]['taskID']
        print taskID
        # now = datetime.datetime.now()
        return HttpResponse(jobs)
    return render(request, 'postest.html')

@csrf_exempt
def RunmodAPI(request):
    if request.method == "POST":
        result = {}
        request = request.body
        print 'request  ==========>  '+request
        init_request = json.loads(request)
        ip_list=[]

        rbt = ANSRunner(init_request["hosts"])
        for host in init_request["hosts"]:
            print json.dumps(host)
            for k,v in host.items():
                print 'ip  ============>  '+v
                ip_list.append(v)
        rbt.run_model(host_list=ip_list, module_name=init_request["module_name"], module_args=init_request["module_args"])
        # rbt.run_model(host_list=[], module_name='yum', module_args="name=htop state=present")
        output = rbt.get_model_result()
        output = json.dumps(output)
        print 'output  ==========>  '+output

        # print init_jobs

        # now = datetime.datetime.now()
        return HttpResponse(output)
    # return render(request, 'AnsibleAPI.html',{'output': output})

@csrf_exempt
def playbookAPI(request):
    if request.method == "POST":

        request = request.body
        print 'request  ==========>  '+request
        dict_request = json.loads(request)
        extra_vars = dict_request[u'extra_vars'][0]
        print type(extra_vars)
        rbt = ANSRunner(resource='all')
        rbt.run_playbook(playbook_path='/Users/vct/opt/ansible/yml/useradd.yml',extra_vars=extra_vars)
        output = rbt.get_playbook_result()
        print output

        # print init_jobs
        # now = datetime.datetime.now()
        return HttpResponse('output')
    # return render(request, 'AnsibleAPI.html',{'output': output})

###
class RemarkList(generics.ListAPIView):
    serializer_class = ServerSerializer
    def get_queryset(self):
        queryset = Server.objects.all()
        cmdb_owner = self.request.query_params.get('cmdb_owner', None)
        cmdb_ip = self.request.query_params.get('cmdb_ip', None)
        filer_keys = {}
        if cmdb_owner is not None:
            print cmdb_owner
            # q1 = queryset.filter(owner=cmdb_owner)
            # q2 = q1.filter(ip=cmdb_ip)
            res = queryset.filter(filer_keys)
            print res
        else:
            print 'cmdb_remark is none!'

        return res


###########################



class ServerList(generics.ListCreateAPIView):
    queryset = Server.objects.all()[0:10]
    serializer_class = ServerSerializer


#
# class GetIp(mixins.ListModelMixin, viewsets.GenericViewSet):
#     queryset = Server.objects.all()
#     serializer_class = ServerSerializer
#     # 使用过滤器
#     filter_backends = (DjangoFilterBackend,)
#     # 定义需要使用过滤器的字段
#     filter_fields = ('owner', 'ip')


class ServerDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Server.objects.all()
    serializer_class = ServerSerializer



######

# class ServerList(APIView):
#     """
#     列出所有代码片段(snippets), 或者新建一个代码片段(snippet).
#     """
#     def get(self, request, format=None):
#         servers = Server.objects.all()
#         serializer = SnippetSerializer(servers, many=True)
#         return Response(serializer.data)
#
#     def post(self, request, format=None):
#         serializer = SnippetSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     def perform_create(self, serializer):
#         serializer.save(owner=self.request.user)
#
# class ServerDetail(APIView):
#     """
#     读取, 更新 or 删除一个代码片段(snippet)实例(instance).
#     """
#     def get_object(self, pk):
#         try:
#             return Server.objects.get(sn=pk)
#         except Server.DoesNotExist:
#             raise Http404
#
#     def get(self, request, pk, format=None):
#         server = self.get_object(pk)
#         serializer = SnippetSerializer(server)
#         return Response(serializer.data)
#
#     def put(self, request, pk, format=None):
#         server = self.get_object(pk)
#         serializer = SnippetSerializer(server, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     def delete(self, request, pk, format=None):
#         server = self.get_object(pk)
#         server.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
###########
# class JSONResponse(HttpResponse):
#     """
#     An HttpResponse that renders its content into JSON.
#     """
#     def __init__(self, data, **kwargs):
#         content = JSONRenderer().render(data)
#         kwargs['content_type'] = 'application/json'
#         super(JSONResponse, self).__init__(content, **kwargs)

# @csrf_exempt
# def cmdb_list(request):
#     """
#     List all code snippets, or create a new snippet.
#     """
#     if request.method == 'GET':
#         cmdb = Server.objects.all()
#         serializer = SnippetSerializer(cmdb, many=True)
#         return JSONResponse(serializer.data)
#
#     elif request.method == 'POST':
#         data = JSONParser().parse(request)
#         serializer = SnippetSerializer(data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JSONResponse(serializer.data, status=201)
#         return JSONResponse(serializer.errors, status=400)
#
# @csrf_exempt
# def server_detail(request, pk):
#
#     """
#     Retrieve, update or delete a code snippet.
#     """
#     try:
#         server = Server.objects.get(sn=pk)
#     except Server.DoesNotExist:
#         return HttpResponse(status=404)
#
#     if request.method == 'GET':
#         serializer = SnippetSerializer(server)
#         return JSONResponse(serializer.data)
#
#     elif request.method == 'PUT':
#         data = JSONParser().parse(request)
#         serializer = SnippetSerializer(cmdb, data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JSONResponse(serializer.data)
#         return JSONResponse(serializer.errors, status=400)
#
#     elif request.method == 'DELETE':
#         cmdb.delete()
#         return HttpResponse(status=204)
# @api_view(['GET', 'POST'])
# def server_list(request,format=None):
#     # """
#     # 列出所有的代码片段（snippets），或者创建一个代码片段（snippet）
#     # """
#     if request.method == 'GET':
#         servers = Server.objects.all()
#         serializer = SnippetSerializer(servers, many=True)
#         return Response(serializer.data)
#
#     elif request.method == 'POST':
#         serializer = SnippetSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
# @api_view(['GET', 'PUT', 'DELETE'])
# def server_detail(request, pk,format=None):
#     # """
#     # 读取, 更新 或 删除 一个代码片段实例（snippet instance）。
#     # """
#     try:
#         server = Server.objects.get(sn=pk)
#     except Server.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)
#
#     if request.method == 'GET':
#         serializer = SnippetSerializer(server)
#         return Response(serializer.data)
#
#     elif request.method == 'PUT':
#         serializer = SnippetSerializer(server, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     elif request.method == 'DELETE':
#         server.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)