import sys
import random
# import pygame
# pygame.init()
# size = width,heigth = 320,240
# screen = pygame.display.set_mode(size)
a=0
redball = input("请输入红球个数：")
blueball = input("请输入篮球个数：")
bigred = input("请输入红球最大值：")
xiaored = input("请输入红球最小值：")
bigblue = input("请输入篮球最大值：")
xiaoblue = input("请输入篮球最小值：")
ssqnull = input("请输入购买多少注：")
# print("红球个数为"+redball,"篮球个数为"+blueball)
# print("红球最大值为："+bigred,"最小值为："+xiaored)
# print("篮球最大值为："+bigblue,"篮球最小值为："+xiaoblue)
while a < int(ssqnull) :
    b=random.sample(range(int(xiaored),int(bigred)),int(redball))
    c=random.sample(range(int(xiaoblue),int(bigblue)),int(blueball))
    a+=1
    print("红球为："+str(b),"篮球为:"+str(c))
    # print("红球为："+i)
# while True:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             pygame.quit()
#             sys.exit()