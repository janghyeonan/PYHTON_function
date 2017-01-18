#-*- coding:utf-8 -*-

#로그 파일 만들기
import glob, os
import time as tt
from datetime import date
from datetime import time
from datetime import datetime
import datetime

#오늘의 날짜 검색 6자리 얻는 함수
def today_6day():
    global result
    today = datetime.date.today()
    kk = today.year
    mm = today.month
    nn = today.day -1

    kk = str(kk).replace("201", "1")
    
    if len(str(nn)) < 2 :
        nn = "0" + str(nn)

    result = str(kk) + str(mm) + str(nn)    


#로그파일 만드는 함수
def save_log(message):
    with open(r"D:/log/"+str(datetime.datetime.now())[:19]+"_log_fileupload.txt", 'a') as f:        
        f.write(str(datetime.datetime.now())[:19]+" - " + message +"\n" )
    print(str(datetime.datetime.now())[:19]+" - " + message)


#로그저장
save_log("작업시작")
