<!DOCTYPE html>
<html>
{% for ticket in ticket_list %}
   {% for k,v in ticket.items %}
   <br> {{v}} </br>
   {% endfor %}
{% endfor %}
{% for number in server_sum %}
    {% for x,y in number.items %}
        <br> {{y}} </br>
    {% endfor %}
{% endfor %}
<head>
    <meta charset="utf-8">
    <title>ECharts</title>
    <!-- 引入 echarts.js -->
    <script src="/static/js/echarts.min.js"></script>
</head>
<body>
    <div id="main" style="width: 600px;height:400px;"></div>
    <script type="text/javascript">
        // 基于准备好的dom，初始化echarts实例
        var myChart = echarts.init(document.getElementById('main'));

        // 指定图表的配置项和数据
    option = {
        title : {
            text: '运基地IT组工单分类情况',
            subtext: '系统组',
            x:'center'
        },
        tooltip : {
            trigger: 'item',
            formatter: "{a} <br/>{b} : {c} ({d}%)"
        },
        legend: {
            orient: 'vertical',
            left: 'left',
            data: ['定时巡检','设备报修','设备迁移','设备上架','设备下架','协助处理','系统安装','增加备件','移除备件','变更处理','问题咨询']
        },
        series : [
            {
                name: '访问来源',
                type: 'pie',
                radius : '55%',
                center: ['50%', '60%'],
                data:[
                    {name:'定时巡检', value:{{count_dsxj}}},
                    {name:'设备报修', value:{{count_sbbx}}},
                    {name:'设备迁移', value:{{count_sbqy}}},
                    {name:'设备上架', value:{{count_sbsj}}},
                    {name:'设备下架', value:{{count_sbxj}}},
                    {name:'协助处理', value:{{count_xzcl}}},
                    {name:'系统安装', value:{{count_xtaz}}},
                    {name:'增加备件', value:{{count_zjbj}}},
                    {name:'移除备件', value:{{count_ycbj}}},
                    {name:'变更处理', value:{{count_bgcl}}},
                    {name:'问题咨询', value:{{count_wtzx}}},
                ],
                itemStyle: {
                    emphasis: {
                        shadowBlur: 10,
                        shadowOffsetX: 0,
                        shadowColor: 'rgba(0, 0, 0, 0.5)'
                    }
                }
            }
        ]
    };


        myChart.setOption(option);
    </script>
</body>
</html>

