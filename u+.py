import json
from wsgiref import headers
import requests
from requests import request
import json
import re

def text(html,n,pattern,p,p2):
    for i in html:
        header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36 Edg/105.0.1343.50","Accept": "application/json, text/plain, */*","Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6","Accept-Encoding": "gzip, deflate","Connection": "keep-alive","Referer": "http://ee-c.lcu.edu.cn/workAnswer/29206131b3a2440184c5150a8b2347fa/fe4f3e67550f45359e431ab29fea0188/false?isPiYue=noPiYue","Host": "ee-c.lcu.edu.cn","Authentication": "eyJhbGciOiJIUzUxMiJ9.eyJyZnQiOmZhbHNlLCJqdGkiOiJhY2VhOTI3MGE2MWY0NjcxYjZlZDQwNDQyOGQ3MDFiMiIsImlzcyI6InVyYW51cyIsInN1YiI6IjhhYjVhZDcxZjE1MTRlNmZiMWY3NWQ5MDI3OWEyNzNlIiwiYXVkIjpbIioiXSwiaWF0IjoxNjY0MDcyMTkyLCJuYmYiOjE2NjQwNzIxOTIsImV4cCI6MTY2NDI0NDk5MiwiYWV4IjowLCJwbXMiOnsiZXhhbSI6NDYsImNvdXJzZSI6Njg3MTk1NzAzNTgsImF0dGFjaG1lbnQiOjQ2MTE2ODYwMTg0MjczODc5MDYsImdyYWQiOjE1MzgsImJhc2UiOjY2OTQ4MDIyfSwibWFuIjp7ImFjY291bnRJZCI6IjhhYjVhZDcxZjE1MTRlNmZiMWY3NWQ5MDI3OWEyNzNlIiwiYWNjb3VudCI6IkxDVTIwMjAyMDU0NDQiLCJlbWFpbCI6IjIzOTQ1NTk2NTlAcXEuY29tIiwibW9iaWxlIjoiMTM3OTEwMjEwNjEiLCJjYWxsaW5nQ29kZSI6Ijg2IiwicGFzc3dvcmRDb3JyZWN0ZWQiOnRydWUsImVtYWlsVmVyaWZpZWQiOmZhbHNlLCJtb2JpbGVWZXJpZmllZCI6ZmFsc2UsIm1lbWJlcklkIjoiMzllZGRlMWQwNWU1MTFlYmE4ZTEyMDA0MGZmMWZmNjQiLCJuYW1lIjoi546L6JCMIiwidHlwZSI6IlN0dWRlbnQifSwib3JnIjp7InNjaG9vbElkIjoiZjRhY2FmNmM2MzBkMTFlOWIwNjIyMDA0MGZmMWZmNjQiLCJzY2hvb2xDb2RlIjoiTENVIiwic2Nob29sTmFtZSI6IuiBiuWfjuWkp-WtpiIsImNvbGxlZ2VJZCI6IjU2MmJmNTNkNjMwZTExZTliMDYyMjAwNDBmZjFmZjY0IiwiY29sbGVnZUNvZGUiOiJMQ1UtQzAwMSIsImNvbGxlZ2VOYW1lIjoi6K6h566X5py65a2m6ZmiIiwibWFqb3JJZCI6IjA2ZWQ1ZWM2NjMwZjExZTliMDYyMjAwNDBmZjFmZjY0IiwibWFqb3JDb2RlIjoiTENVLUMwMDEtUzAwNCIsIm1ham9yTmFtZSI6Iui9r-S7tuW3peeoiyIsImNsYXNzcmFkZUlkIjoiMDg4MGUwMjIwNWU0MTFlYmE4ZTEyMDA0MGZmMWZmNjQiLCJjbGFzc3JhZGVDb2RlIjoiTENVLUMwMDEtUzAwNC0yMDIwLTUiLCJjbGFzc3JhZGVOYW1lIjoiMjAyMOe6p-i9r-S7tuW3peeoizXnj60ifX0.skEmKaUH1cftxUp-fXAAUNyUDPv62EIpqHMPTSxNu6lAFdJoek8idh2HWyuoexRq5hWRYwUVXuNLi9SI7infcA"}
        response = requests.get(i,headers = header)
        result = response.content.decode("utf-8")
        text = json.loads(result)
        fanhui1 = str(n) + "、" + text["data"]["titleText"]
        fanhui2 = text["data"]["userAnswer"]
        fh1 = pattern.sub("",fanhui1)
        fh2 = pattern.sub("",fanhui2)
        fh1 = p.sub("",fh1)
        fh2 = p.sub("",fh2)
        fh1 = p2.sub(">",fh1)
        fh2 = p2.sub(">",fh2)
        with open('answer.txt','a',encoding='utf-8') as file1:
            print(fh1,file = file1)
            print(fh2,file = file1)
        n += 1

cnt = 1
html = ["http://ee-c.lcu.edu.cn/api/course/homeworkQuestions/7d49288180524aaeacd24d1031b54f09/student/detail",\
        "http://ee-c.lcu.edu.cn/api/course/homeworkQuestions/db9da391360a4574bbb075c025bd819d/student/detail",\
        "http://ee-c.lcu.edu.cn/api/course/homeworkQuestions/6eb50a71c8d04cadba36f7e045e71bf2/student/detail",\
        "http://ee-c.lcu.edu.cn/api/course/homeworkQuestions/1e32a0e7bd5e4b329e8b73bef412326d/student/detail",\
        "http://ee-c.lcu.edu.cn/api/course/homeworkQuestions/421767b427144e2cba0d8a8356a2d39e/student/detail",\
        "http://ee-c.lcu.edu.cn/api/course/homeworkQuestions/455687e800eb421fba87c799ae0eac65/student/detail",\
        "http://ee-c.lcu.edu.cn/api/course/homeworkQuestions/fde6769bb5404f94b04d36d32adb585f/student/detail",\
        "http://ee-c.lcu.edu.cn/api/course/homeworkQuestions/845b74a123064490948584cbee59c804/student/detail",\
        "http://ee-c.lcu.edu.cn/api/course/homeworkQuestions/72c5f1cdf85540ea8ff4ce4ab2ee9a6a/student/detail",\
        "http://ee-c.lcu.edu.cn/api/course/homeworkQuestions/05287094a60d49a28ceacfdd4ff915ad/student/detail",\
        "http://ee-c.lcu.edu.cn/api/course/homeworkQuestions/a83b7dec194c45788ce5d510aa745f01/student/detail",\
        "http://ee-c.lcu.edu.cn/api/course/homeworkQuestions/ae6606d2365241beb8b6f08af33af043/student/detail",\
        "http://ee-c.lcu.edu.cn/api/course/homeworkQuestions/3f441827e8af4c3d8f04327aa59fe4bd/student/detail"]
pattern = re.compile("<[^>]+>")
p = re.compile("&nbsp;")
p2 = re.compile("&gt;")
text(html,cnt,pattern,p,p2)

#pyload = {}
