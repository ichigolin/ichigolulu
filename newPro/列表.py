team=['pikaqiu','xiaohuolong','jienigui','miaowazhongzi','huobaohou']#创建列表将我的宠物小精灵装进来
message=('welcome to my team,victory belongs us')
print(team[0].title()+','+message+'!')
print(team[1].title()+','+message+'!')
print(team[2].title()+','+message+'!')
print(team[3].title()+','+message+'!')
print(team[4].title()+','+message+'!')#对我的每个小精灵打个招呼，说一句话
tmp=team[4]
del team[4]#火爆猴生病了离开了队伍
print(team)
print(tmp)
team.append('daqianxie')#大钳蟹自告奋勇加入了我的队伍
print(team)
message=('welcome to join us')
print(team[4].title()+','+message+'!')#跟大钳蟹说一句话
team.append('chouchouni')#大木博士说他的臭臭泥也想加入队伍
message=('welcome')
print(team[5].title()+','+message+'!')#跟臭臭泥说一句话
team_pop=team.pop(4)
print(team)
print(team_pop)
team.sort()
print(team)
s=team.index('miaowazhongzi')
m=team.index('pikaqiu')
team[s],team[m]=team[m],team[s]
print(team)#按指定位置排序，顺序必须是：臭臭泥、杰尼龟、皮卡丘、妙蛙种子、小火龙
team.reverse()#刚才把顺序给弄反了，于是又把排序给反过来了
print(team)
print(len(team))#确定到底有多少宠物小精灵跟我一起上路
message1=('take care of yourself')
message2=('ganbadie,minasang')
print(tmp.title()+','+message1+'!')
print(team[0].title()+','+team[1].title()+','+team[2].title()+','+team[3].title()+','+team[4].title()+','+message2+'!')

