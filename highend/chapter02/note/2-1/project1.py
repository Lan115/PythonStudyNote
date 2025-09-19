#python中一切皆为对象
#1.函数可以是对象
def ask(name="boddy"):
    print(name)
func = ask
func()
print()
#2.类可以是对象
class Person:
    def __init__(self):
        print("boddy")
my_class = Person
my_class()
print()
#3.集合可以是对象,此例中输出有返回值
list = []
list.append(ask)
list.append(Person)
for item in list:
    print(item())
print()
#4.可以当成函数的返回值
def a():
    print("decdec")
    return ask
my_ask = a()
my_ask("aaaaaaaaaaaaa")