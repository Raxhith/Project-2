from django.shortcuts import render
from django.http import HttpResponse

import datetime

def server_time(request):
	data = datetime.datetime.now()
	msg = '<h1>Server Time: '+str(data)+'</h1>'
	return HttpResponse(msg)