#텍스트 파일 읽은 후 print로 보여주기

f = open(r"C:\폴더경로\테스트파일명.txt", 'r')
while True:
    line = f.readline()
    if not line: break
    if line == '\n':
        print('nonono')
    print(line )
f.close()
