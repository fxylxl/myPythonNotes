

# 定义一个空类
class Student():
    # 一个空类，pass代表直接跳过
    # 此处pass必须有
    pass

# 定义一个对象
zhanggsan = Student()


# 再定义一个类，用来描述听python的学生
class PythonStudent():
    # 用None给不确定的值赋值

    name = None
    age = 18
    course = "Python"

    # 需要注意：
    # 1. 缩进层级
    # 2. 系统默认一个self参数
    def doHomework(self):
        print("I am doing my homework")

        # 推荐在函数末尾使用return语句
        return None


# 实例化一个叫lisi的学生，是一个具体的人
lisi = PythonStudent()

print(lisi.age)
print(lisi.name)

# 注意成员函数的调用没有传入参数
lisi.doHomework()