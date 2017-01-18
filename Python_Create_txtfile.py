#파이썬으로 텍스트 파일 만들기

import os

with open(r"C:\Programs\Python\Python35\testfile.txt", "wt") as f:
    f.write("Hello, World\n")
