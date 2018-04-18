from turtle import*
n = int(input("Nhap so canh cua da giac ban muon (>=3): "))
angle = 180*(n-2)//n
speed(0)

for i in range(1000):
    forward(i)
    right(180-angle+1)
    # if (i % 7 == 1): color('red')
    # if (i % 7 == 2): color('orange')
    # if (i % 7 == 3): color('yellow')
    # if (i % 7 == 4): color('green')
    # if (i % 7 == 5): color('blue')
    # if (i % 7 == 6): color ('indigo')
    # if (i % 7 == 0): color('purple')
    # em thay de den trang dep hon nhung neu thich anh co the uncomment cho no nhieu mau a =)))

a = input("")