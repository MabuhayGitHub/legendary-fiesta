from Rectangle import *

def screenLeftClick(x, y):
    rect = Rectangle(x, y)
    rect.drawShape()

if __name__ == "__main__":
    turtle.title("클래스를 이용한 사각형 그리기")
    # 마우스 왼쪽 버튼 클릭 감지
    # 1: 왼쪽 버튼
    # 2: 휠
    # 3: 우측 버튼
    turtle.onscreenclick(screenLeftClick, 1)
    # 그래픽 창 대기
    turtle.done()