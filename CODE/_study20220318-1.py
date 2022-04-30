'''
while(True):
    input1 = input('> ')
    if input1 =='help':
        print('에코를 해주는 프로그램입니다!!')
    elif input1 == 'quit':
        input2 = input('정말로 종료하시겠습니까? (Y/N) ')
        if input2 == 'Y':
            break
    else:
        input1 = input1 + ' '
        print(input1 * 3)
'''

'''
f = open('_myPY.txt','w')
f.write('안녕하세요!!')
f.close()

with open('_myPY.txt','r') as f:
    data = f.read()
print(data)
'''

'''
import turtle as t

for i in range(4):
    t.forward(100)
    t.left(90)
    print(t.position())

t.up()
t.goto(200,0)
t.down()

for i in range(2):
    t.forward(120)
    t.left(120)
    t.forward(80)
    t.left(60)

t.up()
t.goto(-300,0)
t.down()

for i in range(5):
    t.forward(100)
    t.left(360*2//5)

t.up()
t.goto(0,0)
t.down()
'''

import turtle as t

t.goto(-400,0)
t.color('red','yellow')
t.begin_fill()
while(True):
    t.forward(800)
    t.left(172)
    print(t.position())
    print(abs(t.pos()))
    if abs(t.pos()) < 1:
        print(t.pos())
        print(abs(t.pos()))
        break
t.end_fill()
t.done()
