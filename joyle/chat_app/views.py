from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
# Create your views here.

@csrf_exempt
@login_required(login_url='/auth/error')
def chat_view(request, chat_id):
	return HttpResponse("chat view")

@csrf_exempt
@login_required(login_url='/auth/error')
def group_view(request, group_id):
	return HttpResponse("group view")

@csrf_exempt
@login_required(login_url='/auth/error')
def message_view(request, message_id):
	return HttpResponse("message view")
