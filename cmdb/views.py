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
from cmdb.serializers import ServerSerializer
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from cmdb.models import Server
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
from rest_framework import generics
from rest_framework import viewsets
import django_filters.rest_framework
from django_filters.rest_framework import DjangoFilterBackend
###
from cmdb.ansible_api import ANSRunner
from .forms import AnsibleForm

@csrf_exempt
def form(request):
    if request.method == 'POST':
        form = AnsibleForm(request.POST)
        print form
        if form.is_valid():
            ip_list = []
            model_name = form.cleaned_data['model_name'].encode("utf-8")
            command = form.cleaned_data['command'].encode("utf-8")
            Host_List = form.cleaned_data['Host_List']
            for i in  Host_List.split('\r\n'):
                ip_list.append(i)
            rbt = ANSRunner('[{"hostname":"172.16.186.130"},{"hostname":"172.16.186.129"}]')
            print ip_list
            rbt.run_model(host_list=ip_list, module_name=model_name,module_args=command)
            Runmod_Output = rbt.get_model_result()
            # Runmod_Output = json.dumps(Runmod_Output, content_type='application/json')
            Runmod_output_json = json.dumps(Runmod_Output)

            print Runmod_Output
            # print 'Runmod_Output  ==========>  '+Runmod_Output
            # now = datetime.datetime.now()
            return render(request, 'cmdb/Runmod_output_result.html', {'Runmod_output_json': Runmod_output_json})
        # return HttpResponse('ok')
    else:
        form = AnsibleForm()
        return render(request, 'cmdb/form_ansible.html', {'form': form})

def Servers(request):

    return render(request, 'cmdb/Servers.html')

def dataget(request):
    list_chose = request.GET.get('list')
    print list_chose
    return render(request, 'cmdb/Servers.html', {'list_chose':list_chose})

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
        request = request.body
        # print 'request  ==========>  '+request
        init_request = json.loads(request)
        ip_list=[]
        rbt = ANSRunner(init_request["hosts"])
        for host in init_request["hosts"]:
            for k,v in host.items():
                ip_list.append(v)
        print ip_list
        rbt.run_model(host_list=ip_list, module_name=init_request["module_name"], module_args=init_request["module_args"])
        Runmod_Output = rbt.get_model_result()
        print type(Runmod_Output)
        Runmod_Output = json.dumps(Runmod_Output, content_type = 'application/json')
        # print 'Runmod_Output  ==========>  '+Runmod_Output
        # now = datetime.datetime.now()
        return HttpResponse(Runmod_Output)
        # return render(request, 'AnsibleAPI.html')

@csrf_exempt
def playbookAPI(request):
    if request.method == "POST":
#'''request =   {"module_name":"shell","hosts":[{"hostname":"172.16.186.130"},{"hostname":"group1"}],"module_args":"touch /tmp/qianshiwangbadan! ","extra_vars":{"hostslist":"all","ansible_ssh_user":"root"}}'''
        request = request.body
        dict_request = json.loads(request)
        extra_vars = dict_request['extra_vars']
        rbt = ANSRunner(resource='all')
        rbt.run_playbook(playbook_path='/Users/vct/opt/ansible/yml/useradd.yml',extra_vars=extra_vars)
        Playbook_Output = rbt.get_playbook_result()
        Playbook_Output.pop('ok')
        Json_Playbook_Output = json.dumps(Playbook_Output)
        # print Json_Playbook_Output
        return HttpResponse(Json_Playbook_Output, content_type = 'application/json')
    # return render(request, 'AnsibleAPI.html')



        # now = datetime.datetime.now()
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
@api_view(['GET', 'POST'])
def server_list(request,format=None):
    # """
    # 列出所有的代码片段（snippets），或者创建一个代码片段（snippet）
    # """
    if request.method == 'GET':
        list_chose = request.GET.get('list')

        if list_chose == None or list_chose == 'None':
            servers = Server.objects.all()
        else:
            servers = Server.objects.filter(cabinet_list = list_chose)
        serializer = ServerSerializer(servers, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ServerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def server_detail(request, pk,format=None):
    # """
    # 读取, 更新 或 删除 一个代码片段实例（snippet instance）。
    # """
    try:
        server = Server.objects.get(sn=pk)
    except Server.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ServerSerializer(server)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = ServerSerializer(server, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        server.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)