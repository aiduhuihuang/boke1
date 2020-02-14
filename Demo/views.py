from django.http import HttpResponse
# def index(request):
#     """
#     视图：作用
#     :param request:  形参 包含请求信息的请求对象
#     :return:    HttpResponse  响应对象
#     """
#     ## JsonReponse
#     return HttpResponse("hello world")
from django.shortcuts import render_to_response

def index(request):

    return render_to_response("index.html")


def about(request):
    return render_to_response("about.html")

def listpic(request):
    return render_to_response("listpic.html")

def newslistpic(request):
    return render_to_response("newslistpic.html")


def base(request):
    return render_to_response("base.html")





