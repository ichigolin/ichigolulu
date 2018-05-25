for number in range(1,5):
    print(number)
number=list(range(1,6))
print(number)
number=list(range(5,20,5))
print(number)
number=list(range(3,31,3))
print(number)
squares=[]
for value in range(1,11):
    square=value**2
    squares.append(square)
print(squares)
squares=[]
for value in range(1,11):
    squares.append(value**2)
print(squares)
square=[value**2 for value in range(1,11)]
print(square)
print(min(square))
print(max(square))
print(sum(square))
number=list(range(1,21))#创建一个列表，在列表里面生成一组数
print(number)
numbers=[]#用for循环把列表里面每个数的3倍计算出来（要用三种方式）
for value in range(1,21):
    number=value*3
    numbers.append(number)
print(numbers)
numbers=[]
for value in range(1,21):
    numbers.append(value*3)
print(numbers)
number=[value*3 for value in range(1,21)]
print(number)
number=list(range(1,21))
print(number)#计算出你列表的总和，找出你列表里最大和最小的值。
print(min(number))
print(max(number))
print(sum(number))











