'''
Heroer beta-0.1
strawberry
2018-05-24
'''
print("welcome to the heroes' world!")
print("|you are in the world like this #####,'a' for left,'d' for right |")
HP=100
ATK=200
DEF=300
name=input('please input your username:')
if not name:
    name = 'player 01'
usermsg=[name,HP,ATK,DEF]
print('your name is:',usermsg[0],'HP is:',usermsg[1])
print('please input your phone number：')
a=input()
print('your register number is：',a)
print('please choose your sex：1.male，2.female')
c=input()
if int(c)==1:
    print('your sex is：male')
else:
    print('your sex is：female')
print("and now you are here:*####| 'a'for left,'d' for right|")
userinput = input()
if userinput == 'a':
    print('now you are here:*####')
if userinput == 'd':
    print('now you are here:#*###')































