from django import forms
import datetime
#coding:utf-8


class StatementForm(forms.Form):
##    ticket = forms.CharField(initial='sbbx',label=u'type',help_text='from')
    today = datetime.date.today()
    start_time = forms.DateTimeField(initial=today-datetime.timedelta(days=6),label='begin')
    end_time = forms.DateTimeField(initial=today+datetime.timedelta(days=1),label='end')



#    b = forms.Integer()
#    cmd = forms.EmailField()
#    ipa = forms.GenericIPAddressField()
class GetsnForm(forms.Form):
    ipa = forms.CharField(widget=forms.Textarea)
#    ipa = forms.CharField(label='Server IPAddress')
#    datef = forms.DateTimeField(label='Server datetime')
#    timef = forms.TimeField(label='timefiled')
#    ipaddf = forms.GenericIPAddressField(label='Ip')
#    url = forms.URLField(label='Your Web site', required=False)
#    comment = forms.CharField()
