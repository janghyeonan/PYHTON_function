#파이썬 날짜 변환 -원하는 출력은 170101 순으로 표기되는것
import glob, os
import time as tt
from datetime import date
from datetime import time
from datetime import datetime
from selenium import webdriver
import datetime
import selenium

#날짜 자릿수변경
today = datetime.date.today()

kk = today.year
mm = today.month
nn = today.day -1
kk = str(kk).replace("201", "1")
if len(str(mm)) < 2 :
    mm = "0" + str(mm)
if len(str(nn)) < 2 :
    nn = "0" + str(nn)

result = str(kk) + str(mm) + str(nn)

print(result)


