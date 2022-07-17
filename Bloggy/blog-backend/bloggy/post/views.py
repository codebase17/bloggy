import imp
from django.db import connection
from django.shortcuts import render
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import datetime

# Create your views here.
@csrf_exempt
def addPost(request):
    if request.method=='POST':
        data = JSONParser().parse(request)
        post_user_email_id = data["post_user_email_id"]
        post_title=data["post_title"]
        post_content=data["post_content"]
        last_modified_date=datetime.datetime.now()  
        likes=data["likes"]
        cursor = connection.cursor()
        sql = '''insert into post_tbl_blog_post (post_user_email_id_id,post_title,post_content,last_modified_date,likes) values (%s,%s,%s,%s,%s)'''
        cursor.execute(sql,(post_user_email_id,post_title,post_content,last_modified_date,likes))
        print(cursor)
        
        row = cursor.fetchone()
        print(row)
        return JsonResponse("Ok",safe=False)
    
