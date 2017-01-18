import glob, os
import datetime

# 특정폴더에서 파일 찾기


#날짜 6자리 추출
today = datetime.date.today()
kk = today.year
mm = today.month
nn = today.day -1
kk = str(kk).replace("201", "1")
if len(str(nn)) < 2 :
    nn = "0" + str(nn)

result = str(kk) + str(mm) + str(nn)


# 추출된 6자리 날짜로 파일 찾기
target_dir = r'C:/Downloads/'
for file in glob.glob(target_dir + "%s*.xlsx" %result):    
    ff = file    

#확인
print(ff)
