flowers=['poppy','grandifloum','tulip','mandara','higanbana']
print(flowers)#打印整个列表
print(flowers[0])
print(flowers[-2])#把每个元素打印出来
print(flowers[2].title())
print(flowers[1].upper())
message=('my favorite flower is ')
print(message+flowers[0].upper()+'!')
flowers[1]='flos'
print(flowers)#修改列表中的某个元素
animals=[]
animals.append('rabbit')
animals.append('pig')
animals.append('cat')
animals.append('dog')
animals.append('bird')
print(animals)#建立一个空列表，并依次添加元素进去
idols=[]
idols.append('jay chou')
idols.append('Eason')
idols.append('priest')
idols.insert(2,'jake chen')
print(idols)#建立一个空列表，并按位置添加新元素进去
invitation=['ruhua','siyu','chenyu','luoyan']#给列表里的每个朋友发一份邀请，并且每个人的名字首字母大写
message=('would you like to have dinner with me')
print(invitation[0].title()+','+message+'?')
print(invitation[1].title()+','+message+'?')
print(invitation[2].title()+','+message+'?')
print(invitation[3].title()+','+message+'?')




