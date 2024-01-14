# 简单的定义一个类
class my_class:
    name = None  # 预定义name变量，并预设值为None

    def my_function(self, date):  # 在类中定义方法时，必须加上一个self参数,用于调用类内部的变量
        print(f"I am {self.name}, Today is {date}.")


# 简单操作一下刚才定义的类的变量
my_new = my_class()  # 创建类对象
print(my_new.name)  # 查看类中name的初始值

# 使用刚才定义的类中的方法
my_new.name = "Biomamba"
my_new.my_function(date = "Friday")
# 可以看到类中包含方法的print函数内容被成功输出

"""
二、构造方法
Python类可以使用:init()方法，成为构造方法。这样构建的方法会在创建类对象的时候会利用传入参数自动传递给__init__()自动执行。
"""
# 定义包含构造方法的类：
class my_class:
    # 定义变量的过程可以省略
    def __init__(self, name, date):
        print(f"I am {name}, Today is {date}.")

my_newclass = my_class(name="Biomamba", date="Friday")
# 可以看到由于构造方法的存在，省去了一些变量的定义过程，并且在生成类对象时同事执行构造方法

# 简单定义一个类并调用其中的方法：
class my_class:
    def my_print(self,my_content):
        print(my_content)
my_new = my_class()
my_new.my_print("Biomamba")
# 可以看出这个类中方法的作用就是打印出输入的内容：
"""
三、类内置方法(魔术方法)
例如一部分中的__init__构造方法是Python的类内置方法，类中还有数十种其它各自具有特殊功能的类内置方法，又称为魔术方法。本文只介绍其中常见的几种。
16.3.1 字符串方法
"""
# 那么这时就可以通过__str__来对类进行改造
class my_class:
    def my_print(self, my_content):
        print(my_content)

    def __str__(self):
        return "我是魔术方法返回的字符串"


my_new = my_class()
"""
16.3.2 大小比较符方法
通过__lt__即可定义。由于两个对象不可直接进行比较，因此比较魔术方法可以指定比较的变量，让对象带上比较的功能。
注：__lt__只能用于>和<这两种比较，<=、>=这类比较运算符需要通过__le__实现。==需要通过__eq__来实现，定义方法与__lt__逻辑相同。
"""
# 改造一下这个类定义
# 定义包含构造方法的类：
class my_class:
   # 定义变量的过程可以省略
    def __init__(self,name,oclock):
        print(f"I am {name}, Now is {oclock} oclock.")
        self.oclock = oclock

    def __lt__(self,other): # self表示当前类，other代表其它用于比较的类
        return self.oclock < other.oclock

my_newclass_1 = my_class(name="Biomamba",oclock= 1)
my_newclass_2 = my_class(name="Biomamba",oclock= 5)

"""
四、封装
封装是指将数据（属性）和行为（方法）包装到类对象中。在方法內部对属性进行操作，在类对象的外部调用方法。这一操作能够提高程序的安全性。
私有成员:
在类的定义中，可以设置私有成员对象和私有成员方法，这些私有成员不可被用户调用，不对外开放。
"""
# 定义一个包含私有成员的类
class my_class:
    __my_var = "我是一个私有变量"
    def __my_function(self):
        print("我是一个私有成员方法")


# 私有成员存在的意义是供类中的其它成员调用：

#  调用私有变量
class my_class:
    __my_var = "我是一个私有变量"
    def my_function(self):
        print(self.__my_var)
my_new = my_class()
my_new.my_function()
# 可以看到私有变量__my_var被成功打印

# 调用私有方法
class my_class:
    def __my_function(self):
        print("我是一个私有成员方法")

    def open_function(self):
        self.__my_function()

my_new = my_class()
my_new.open_function()
# 可以看到私有方法被成功调用
"""
五、继承

继承，顾名思义，可以让新的类继承原有类的变量与方法，语法为:
class 新类名(原有类名)
即:
class 类名(父类)
"""
#单类继承
# 定义原有类
class old_class:
    def old_function(self):
        print("这是初始版本的类")

my_oldclass =  old_class()
my_oldclass.old_function()

# 定义一个新得类，并继承原有类的功能：
class new_class(old_class):
    def new_function(self):
        print("这是最新版本的类")

my_newclass =  new_class()
my_newclass.old_function()
my_newclass.new_function()


#多继承指一个子类继承多个父类，语法也很简单：

class 新类名(父类1, 父类2, 父类3...)


# 定义父类1
class old_class_1:
    def old_function_1(self):
        print("这是父类1的功能")


# 定义父类2
class old_class_2:
    def old_function_2(self):
        print("这是父类2的功能")


# 定义父类3
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# 定义一个新得类，并继承原有类的功能：
class new_class(old_class_1, old_class_2, old_class_3):
    def new_function(self):
        print("这是最新版本的类")
my_newclass = new_class()

my_newclass.old_function_1()
## 这是父类1的功能
my_newclass.old_function_2()
## 这是父类2的功

my_newclass.old_function_3()
## 这是父类3的功能
my_newclass.new_function()
# 可以发现所有父类的功能均可以被调用：
## 这是最新版本的类

"""
合并类上面的新类定义中我们均加入了新的功能，我们也可以通过pass来定义一个空的类，来继承原有的父类:
"""
# 定义父类1
class old_class_1:
    def old_function_1(self):
        print("这是父类1的功能")


# 定义父类2
class old_class_2:
    def old_function_2(self):
        print("这是父类2的功能")


# 定义父类3
class old_class_3:
    def old_function_3(self):
        print("这是父类3的功能")


# 定义一个新得类，并继承原有类的功能：
class new_class(old_class_1, old_class_2, old_class_3):
    pass


my_newclass = new_class()

my_newclass.old_function_1()
## 这是父类1的功能


my_newclass.old_function_2()
## 这是父类2的功能


my_newclass.old_function_3()


# 可以发现所有父类的功能均可以被调用：
## 这是父类3的功能





#继承顺序 当多继承中父类存在相同的变量名与方法名，则优先级为左侧优先:

# 定义父类1
class old_class_1:
    def old_function(self):
        print("这是父类1的功能")


# 定义父类2
class old_class_2:
    def old_function(self):
        print("这是父类2的功能")


# 定义父类3
class old_class_3:
    def old_function(self):
        print("这是父类3的功能")


# 定义一个新得类，并继承原有类的功能：
class new_class(old_class_1, old_class_2, old_class_3):
    pass


my_newclass = new_class()

my_newclass.old_function()
# 只会出现父类1的运行结果
## 这是父类1的功能



#复写父类成员 在子类继承父类的成员属性和方法后，可以通过复写对父类中的成员进行修改。完成方式很简单，重新定义同名成员即可。

# 定义父类
class old_class_1:
    def old_function(self):
        print("这是父类1的功能")

# 继承并复写：
class new_class(old_class_1, old_class_2, old_class_3):
    def old_function(self):
        print("这是复写后的功能")


my_newclass = new_class()

my_newclass.old_function()
# 返回的是复写后的结果
## 这是复写后的功能
#当你复写之后可以通过如下两种方式调用父类中的原有成员：

# 原有父类成员调用方式一：
# 父类名.父类成员

# 定义父类:
class old_class_1:
    def old_function(self):
        print("这是父类1的功能")


# 复写并调用原父类方法：
class new_class(old_class_1, old_class_2, old_class_3):
    def old_function(self):
        myraw = old_class_1()
        myraw.old_function()
        print("这是复写后的功能")


my_newclass = new_class()
my_newclass.old_function()


# 可以看到父类和子类的功能可以被分别调用
## 这是父类1的功能
## 这是复写后的功能


# 原有父类成员调用方式二：
# super().父类成员

# 定义父类:
class old_class_1:
    def old_function(self):
        print("这是父类1的功能")


# 复写并调用原父类方法：
class new_class(old_class_1, old_class_2, old_class_3):
    def old_function(self):
        myraw = super().old_function()
        print("这是复写后的功能")


my_newclass = new_class()
my_newclass.old_function()

"""
六、类型注释
对类型注解后有利于我们调用对应类型的各种方法，方便静态类型检查工具、IDE等第三方工具提供快捷功能。
通常有读变量的类型注解、对函数(方法)形参列表和返回值的类型注解。
变量类型注解
变量类型注解的语法很简单:
方式一：变量: 类型
"""

# 基础变量的注解
my_var1: str = "Biomamba"
type(my_var1)
## <class 'str'>

# 各类数据容器的注解:
# 对于负责数据容器来说，可以支持其中的每一个元素的分别注解
my_list: list[int] = [1, 2, 3]
my_tuple: tuple[str, int, bool] = ["Biomamba", 2023, True]
my_set: set[int] = {1, 2, 3}
my_dict: dict[str, int] = {"Biomamba": 2023}

# 测试一下
print(f"{my_tuple[0]}的类型是{type(my_tuple[0])}")
# 没问题：
## Biomamba的类型是<class 'str'>
#方式二–在注释中操作:
# type 类型
#例如：
var_1 = 15  # type: int
type(var_1)
## <class 'int'>
"""
函数与方法的类型注解
函数和方法中可以对形参与返回值进行类型注解。
"""

# 例如定义函数时对形参my_data进行注解
def my_function(my_data: str):
    return my_data.name


# 对返回值进行注解：
def my_function(my_data) -> list:
    return my_data.name

#Union类型联合注解
# 导包与模块
from typing import Union

# 表示list中的元素既可以是字符串，又可以是整数：
my_list: list[Union[str, int]] = [2023, "Biomamba", "Bioinformatics"]

"""
七、多态
完成某一行为时，使用不同的对象即会得到不同的状态。
例如上面继承的例子:
"""

# 一个父类
class old_class_1:
    def my_function(self):
        pass

# 定义两个子类
class new_class_1(old_class_1):
    def my_function(self):
        print("这是子类1的功能")

class new_class_2(old_class_1):
    def my_function(self):
        print("这是子类2的功能")


# 定义新函数，传入变量为原来定义的类
def print_back(myclass: old_class_1):
    myclass.my_function()

my_new_1 = new_class_1()
my_new_2 = new_class_2()

print_back(my_new_1)
## 这是子类1的功能


print_back(my_new_2)
# 可以看出，对于同样的输入方式，不同的输入对象会执行不同的功能(不同的状态)
## 这是子类2的功能
