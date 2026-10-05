from unittest import case

print(123)

age:str=23   # 这里并不能起到强制类型的效果，只是一个类型说明

print(age)

name="sdist"

print(name[0:3])  #这里的索引竟然是从1 开始的

# content=input("请输入你的内容")
# print(content)

a=10
b=3

print(a/b)   #这里会有小数的，因为结果是会自动转为浮点型
print(a//b)  #这里就是3了

c=6
print(c/b)   #就算这样，本来它能够整除，一样会变成浮点型的

#python是没有++和——的

print(a**b)   #这个是10的3次方，这个是java 没有的

print(a is str)

flag=True

if flag:   #注意这里是有一个冒号的
    print("flag")
else:
    print("not flag")

match flag:
    case 1:   #这里1，也可以hit 中的
        print("flag 1")
    case 2:
        print("flag 2")
    case True:  #这里是True，也可以hit中
        print("flag 3")
    case False:
        print("flag 4")

list1 = [1, 3, True, 3.24, 'str']  #list是关键字来的
print(list1)

print(list1[-1])   #这里是打印最后一个元素，这个和java很不一样。
print(list1[-2])

print(3 in list1)
print(4 in list1)

del list1[-1]
print(list1)

tuple1=(1,2,3,4)  #这个是元祖，但是它不能修改
print(tuple1)

del tuple1
# print(tuple1)   #如果这样写，就会报错

tuple2=4,69,True,'str'
print(tuple2)

t1,t2,t3,t4=tuple2  #这样叫解包
#t1,t2,t3=tuple2  #如果这样写，无法正确解包，下面的这种print 就有问题了
print(t1)

#list，字符串也可以解包的

s={1,3,5}  # 这个是集合
s1={} #这样无法定义空集合，因为空字典也是这样定义的。这样定义的是空字典
print(s1)

d={"name":"tio","age":23}   #这个就是字典，类似于java的map
print(s)
print(d)
print(d["name"])

print(f"d['name']={d['name']}")