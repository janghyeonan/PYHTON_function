# 파이썬 내 자체 그래픽스를 이용한 그리기 각도 변경, 거북이 숨기기
import turtle as t

t.shape("turtle")

angle = 89
t.bgcolor("black")
t.color("green")
t.speed(0)
for x in range(200):
    t.forward(x)     # x 만큼 앞으로 이동 (실행을 반복하면서 선이 길어짐)
    t.left(angle)    # 왼쪽으로 89도 회전

t.hideturtle();      # 화면에 보이지 않도록 숨김.
