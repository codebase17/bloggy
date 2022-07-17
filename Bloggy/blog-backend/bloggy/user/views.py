import imp
import re
from django.db import connection, connections
from django.shortcuts import render
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
@csrf_exempt
def addUser(request):
    if request.method=='POST':
        data = JSONParser().parse(request)
        user_name = data["user_name"]
        user_email_id=data["user_email_id"]
        user_password=data["user_password"]
        cursor = connection.cursor()
        sql = '''insert into user_tbl_user (user_name,user_email_id,user_password) values (%s,%s,%s)'''
        cursor.execute(sql,(user_name,user_email_id,user_password))
        row = cursor.fetchone()
        return JsonResponse("Ok",safe=False)
            
