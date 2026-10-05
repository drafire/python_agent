def hello():
    print("hello")

def add(a,b):
    return a+b

c=add(3,4)
print(c)

def add_multi(*args):   #可变数量的参数，包括元祖
    sum=0
    for num in args:
        sum+=num
    return sum

print(add_multi(1,2,3,4,5))

def tuple_add(**kwargs):   #这样写是可变的字典
    sum=0
    for num in kwargs:
        sum+=num
    return sum

# print(tuple_add(234,11,2))

c= lambda a, b: a + b  #这个是lambda表达式
print(c(1,2))

d=lambda :print("hello")  #这个也是lambda 表达式，不过是没有参数的
d()
