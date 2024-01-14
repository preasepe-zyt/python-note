#数据类型
#str int float
#组合字符串
a = "Taco "
b = "time"
c = a + b
print(c)

#循环
[i for i in t if i > 2] #获得一个列表
#example 1
weather_conditions = ['rain', 'sleet', 'snow', 'freezing fog', 'sunny', 'cloudy', 'ice pellets']
for weather in weather_conditions:
    print(weather)
#example 2
help(range)
odd_numbers = [1, 3, 5, 7, 9]
even_numbers = [10, 4, 6, 8, 2]
for i in range(len(odd_numbers)):
    print(odd_numbers[i] + even_numbers[i])
#条件语句
#简单条件
temperature = 17

if temperature > 25:
    print('it is hot')
else:
    print('it is not hot')
#elif
temperature = -3
if temperature > 0:
     print(temperature, 'is above freezing')
elif temperature == 0:
     print(temperature, 'is freezing')
else:
     print(temperature, 'is below freezing')
#组合条件
if (1 > 0) and (-1 > 0):
     print('Both parts are true')
else:
     print('At least one part is not true')

if (1 < 0) or (-1 < 0):
    print('At least one test is true')
#循环和条件
temperatures = [0, 12, 17, 28, 30]
for temperature in temperatures:
    if temperature > 25:
        print(temperature, 'celsius degrees is hot')
    else:
        print(temperature, 'is not hot')
#嵌套的if
season = "Winter"
temperature = 10
if season == "Winter":

     if temperature > 7:
         print("No need for winter jacket!")

     else:
         print("It might be cold! Wear a proper jacket!")

elif season == "Summer":

     if temperature > 20:
         print("It's warm! Time to wear shorts!")

     else:
         print("Well this is Finland, better wear long trousers!")
else:
     print("Check the weather forecast!")
#函数
#定义函数
def celsius_to_fahr(temp):
    return 9/5 * temp + 32
#调用
freezing_point =  celsius_to_fahr(0)
print('The freezing point of water in Fahrenheit is:', freezing_point)
#子母函数
#定义
def hello(name, age):
    return 'Hello, my name is ' + name + '. I am ' + str(age) + ' years old.'
#调用
output = hello(name='Dave', age=39)
print(output)
"""
将函数保存在脚本文件中
基本上，我们刚刚了解了如何将一些函数保存到脚本文件中。现在让我们将我们一直在使用的其他函数添加到脚本中。只需将下面的文本复制并粘贴到您的文件中，在每个函数之间留下一个空白行。temp_converter.py
"""
#检查当前路径
ls
#设置工作路径
cd
#同时导入多个函数
from my_script import func1, func2, func3
#从脚本导入所有函数
import temp_converter as tc
#“模块”、“包”和“库”这两个词通常可以互换使用。
#导入包和模块
import math
math.sqrt(81)
#重命名导入的模块
import math as m
m.sqrt(49)
type(m)
#导入单个函数
from math import sqrt
sqrt(16)
#导入子模块
import matplotlib.pyplot as plt
plt.figure()
#使用模块函数
print(dir(math))
#导入以后查询函数
help(math.sin)
#对数值进行计算
my_list = ['car', 'bus', 'bike', 'car', 'car', 'bike']
car_count = my_list.count('car')
print("There are", car_count, "cars in my list!")
#pandas来读数据
import pandas as pd
fp = "C:/Users/79403/Desktop/白术抗ad/差异分析部分/ids_exprs.txt"
# Read data using varying amount of spaces as separator and specifying * characters as NoData values
data = pd.read_csv(fp, delim_whitespace=True, na_values=['*', '**', '***', '****', '*****', '******'])
data.head() #显示前面几个
data.columns #显示列
data.rows()
#python读取文件
data = pd.read_csv(fp, delim_whitespace=True, usecols=['USAF','YR--MODAHRMN', 'DIR', 'SPD', 'GUS','TEMP', 'MAX', 'MIN'], na_values=['*', '**', '***', '****', '*****', '******'])
data.head()
#选择列
#usecols= xxx
#第二种方法
#with open(文件名, 模式) as 文件对象:
with open('test.txt', 'r') as f:

#修改列的名称
new_names = {'GSM119615':"a", 'GSM119616':"b", 'GSM119617':"c", 'GSM119618':"d", 'GSM119619':"e",
       'GSM119620':"f", 'GSM119621':"g", 'GSM119622':"h", 'GSM119623':"j", 'GSM119624':"k"}

# Rename the columns
data = data.rename(columns=new_names)
#查看矩阵的维度等于dim
data.shape
#列数据的类型
data.dtypes
#描述统计
data.describe()
#数据框增加某一列$根据需求
def fahr_to_celsius(temp_fahrenheit):
    converted_temp = (temp_fahrenheit - 32) / 1.8
    return converted_temp
data["TEMP_C"] = fahr_to_celsius(data["a"])
data.head()
#循环访问行
# Iterate over the rows
for idx, row in data.iterrows():
    # Print the index value
    print('Index:', idx)
    # Print the row
    print('Temp F:', row["TEMP_F"], "\n")
#
# Create an empty column for the DataFrame where the values will be stored
new_column = "TEMP_C"
data[new_column] = None
# Iterate over the rows
for idx, row in data.iterrows():
    # Convert the Fahrenheit to Celsius
    celsius = fahr_to_celsius(row['TEMP_C'])
    # Update the value of 'Celsius' column with the converted value
    data.at[idx, new_column] = celsius
"""
Pandas DataFrames和Series也有一个专用的方法，用于在列（或行！）上应用函数。使用 时，我们将函数名称（不带括号！）作为参数传递：.apply().apply()
"""
data["new"] = data["a"].apply(fahr_to_celsius)
data.head()
#解析某个列
data["b"].dtypes()
data["a"].head()
#数字切片
date = "201910012350"
date[0:6]
#转换格式+切片
# Convert to string
data['a_STR'] = data['a'].astype(str)#括号里面输入其他的可以切换其他数据类型
data['YEAR_MONTH'] = data['a_STR'].str.slice(start=0, stop=2)
#转换成日期时间
pd.to_datetime(data["TIME_STR"], format='%Y%m', exact=False)
"""
如果需要，您可以使用该参数根据 strftime（format） 方法定义输出日期时间格式。与 一起，例如这样：formatexact=False
在此示例中，删除天、小时和分钟，因为它们未包含在指定的格式中。exact=False
"""
#根据日期时间列提取不同的时间单位
data['DATE'].dt.year
#时间和其他函数连用
data['DATE'].dt.year.nunique()
#创建加提取
data['YEAR'] = data['DATE'].dt.year
data['MONTH'] = data['DATE'].dt.month
#根据固定的来分组
data.groupby(["YEAR", "MONTH"])
#从组中获得固定的值
month = (2019, 4)
grouped.get_group(month)
#计算固定列的均值
# Specify the columns that will be part of the calculation
mean_cols = ['DIR', 'SPEED', 'GUST', 'TEMP_F', 'TEMP_C', 'MONTH']
# Calculate the mean values all at one go
mean_values = group1[mean_cols].mean()
#创建数据框
# Create an empty DataFrame for the aggregated values
monthly_data = pd.DataFrame()
# The columns that we want to aggregate
mean_cols = ['DIR', 'SPEED', 'GUST', 'TEMP_F', 'TEMP_C', "MONTH"]
# Iterate over the groups
for key, group in grouped:
   # Calculate mean
   mean_values = group[mean_cols].mean()
   # Add the ´key´ (i.e. the date+time information) into the aggregated values
   mean_values['YEAR_MONTH'] = key
   # Append the aggregated values into the DataFrame
   monthly_data = monthly_data.append(mean_values, ignore_index=True)
#条件判断和r语言差不多
aprils = data[data["MONTH"]==4]
#取固定列 子集
aprils = aprils[['STATION_NUMBER','TEMP_F', 'TEMP_C','YEAR', 'MONTH']]
#选择某一列进行排列
grouped = aprils.groupby(by=["YEAR", "MONTH"])
#根据某一列进行排序
data.sort_values(by="a", ascending=False).head(10)
"""
请注意，我们使用 * 字符作为通配符，因此任何以 开头和结尾的文件都将添加到我们将迭代的文件列表中。我们专门使用文件名的起始部分，以避免将我们的元数据文件包含在列表中！data/0txtdata/0
"""
import glob
file_list = glob.glob(r'data/0*txt')
#批量读取多个文本
# Repeat the analysis steps for each input file:
#cd current file
import glob
file_list = glob.glob(r'data/0*txt')
for fp in file_list:
    # Read selected columns of  data using varying amount of spaces as separator and specifying * characters as NoData values
    data = pd.read_csv(fp, delim_whitespace=True, usecols=['USAF','YR--MODAHRMN', 'DIR', 'SPD', 'GUS','TEMP', 'MAX', 'MIN'], na_values=['*', '**', '***', '****', '*****', '******'])
"""
1 读取固定宽度的文本文件
本周的数据文件不是用逗号分隔，而是在值之间有可变数量的空格。 以前，我们使用 Pandas 函数的选项读取逗号分隔的值。 对于可变数量的空格，我们可以使用 或 ; 或将起作用，但不能两者兼而有之。 在这种情况下，我们建议使用 .sep=','read_csv()sepdelim_whitespace parametersep='\s+delim_whitespace=Truedelim_whitespace
2 跳过文件的第二行
Pandas 函数的选项是一种在读取文件时跳过文件前 n 行的简单方法。 如果我们想跳过数据文件的前两行，我们可以使用 . 但是，的值不必是单个值，也可以以列表的形式给出。 这样，可以使用带有第二行索引值的列表跳过读取文件的第二行。 换句话说，您可以使用 .skiprows=n read_csv() skiprows=2 n skiprows=[1]
3 两个数据框合并
join1 = data1.merge(data2, on='Time')
4 两个数据框合并希望全部的数据合并进来
join1 = data1.merge(data2, on='Time',how='outer')
"""

# jupyter notebook  启动

#遇到装的包全是required st
pip install --target=c:\users\79403\.conda\envs\omicverse\lib\site-packages singlet
if __name__ == '__main__': #作为脚本都会运行，作为模块import输入后面的不会运行
#查看帮助
help()
xxx？  #函数
L.insert?  #object和函数
xx？ #object本身
xxx?#自定义函数
square?? #可以访问源码 = r中的body
#tab  可以补全 对象都有与之关联的各种属性和方法。
#对象后加.可以显示所有对象
#_下划线是私有方法
#tab 补充导入的库也有用
** #等于开平方
str.*find*? #通过通配符来寻找方法
%paste %cpaste #可以粘贴代码
%run #运行外部代码
%timeit #可以决定后面函数的执行时间
%magic %lsmagic ?#魔术函数的帮助文档
%prun

""""
numpy 模块
"""
#python 是动态语言 c和java这种静态语言需要声明变量
import numpy
numpy.__version__ #看版本
L = list(range(10))
type(L)
[str(c) for c in L]
L3 = [True, "2", 3.0, 4]
[type(item) for item in L3]
#数组
array.array('i', L)
array.array('i', L) #相同类型的数组
np.array([range(i, i + 3) for i in [2, 4, 6]]) #多维数组
#创造数组
# Create a length-10 integer array filled with zeros
np.zeros(10, dtype=int)
# Create a 3x5 floating-point array filled with ones
np.ones((3, 5), dtype=float)
# Create a 3x5 array filled with 3.14
np.full((3, 5), 3.14)
# Create an array filled with a linear sequence
# Starting at 0, ending at 20, stepping by 2
# (this is similar to the built-in range() function)
np.arange(0, 20, 2)
# Create an array of five values evenly spaced between 0 and 1
np.linspace(0, 1, 5)
# Create a 3x3 array of uniformly distributed
# random values between 0 and 1
np.random.random((3, 3))
# Create a 3x3 array of normally distributed random values
# with mean 0 and standard deviation 1
np.random.normal(0, 1, (3, 3))
# Create a 3x3 array of random integers in the interval [0, 10)
np.random.randint(0, 10, (3, 3))
# Create a 3x3 identity matrix
np.eye(3)
# Create an uninitialized array of three integers
# The values will be whatever happens to already exist at that memory location
np.empty(3)

"""
数据类型	描述
bool_	布尔值（真或假）存储为字节
int_	默认整数类型（与 C 相同;通常为或longint64int32)
intc	与 C 相同（通常或intint32int64)
intp	用于索引的整数（与 C 相同;通常为 或ssize_tint32int64)
int8	字节（-128 到 127）
int16	整数（-32768 到 32767）
int32	整数（-2147483648 到 2147483647）
int64	整数（-9223372036854775808 到 9223372036854775807）
uint8	无符号整数（0 到 255）
uint16	无符号整数（0 到 65535）
uint32	无符号整数（0 到 4294967295）
uint64	无符号整数（0 到 18446744073709551615）
float_	的简写。float64
float16	半精度浮点数：符号位、5 位指数、10 位尾数
float32	单精度浮点数：符号位，8位指数，23位尾数
float64	双精度浮点数：符号位，11位指数，52位尾数
complex_	的简写。complex128
complex64	复数，由两个 32 位浮点数表示
complex128	复数，由两个 64 位浮点数表示
"""

#数组的属性
ndim shape size dtype
np.random.randint(10, size=(3, 4, 5))
#访问单个元素
x2[2, 0]
#切片
#一维数组
x = np.arange(10)
x[start:stop:step]
#多维数组
x2[:3, ::2]  # all rows, every other column
x2[:2, :3]  # two rows, # three columns
#修改 创建数组
x2_sub_copy = x2[:2, :2].copy() #数组的副本
#重塑
grid = np.arange(1, 10).reshape((3, 3))
#连接2个及其以上的数组
np.concatenate([x, y, z])
#也可用于二维
# concatenate along the second axis (zero-indexed)
np.concatenate([grid, grid], axis=1)
#混合维度的堆积
# vertically stack the arrays
np.vstack([x, grid])
# horizontally stack the arrays
y = np.array([[99],
              [99]])
np.hstack([grid, y])
#数组的拆分
np.spli tnp.hsplit np.vsplit
#数组算数

"""
算子	等效的 ufunc	描述
+	np.add	加法（例如，1 + 1 = 2)
-	np.subtract	减法（例如，3 - 2 = 1)
-	np.negative	一元否定（例如，-2)
*	np.multiply	乘法（例如，2 * 3 = 6)
/	np.divide	部门（例如，3 / 2 = 1.5)
//	np.floor_divide	楼层划分（例如，3 // 2 = 1)
**	np.power	幂（例如，2 ** 3 = 8)
%	np.mod	模量/余数（例如，9 % 4 = 1)
"""

#指数和对数
当非常小时，这些函数给出的值比原始或要使用的值更精确。x np.log  np.exp
#三角函数
theta = np.linspace(0, np.pi, 3)
#所有相加
np.add.reduce(x)
#所有的乘积
np.multiply.reduce(x)
#如果我们想存储计算的所有中间结果，我们可以改用：accumulate 代码同上

#字母连接数字 r语言中的paste(xxx, xxx) = "xx"+pd["sss"]

#r语言中的getwd() = os.getcwd(） 后面是查看文件的目录 os.path.dirname(os.path.abspath(__file__))
"""
Function Name	NaN-safe Version	Description
np.sum	np.nansum	Compute sum of elements
np.prod	np.nanprod	Compute product of elements
np.mean	np.nanmean	Compute mean of elements
np.std	np.nanstd	Compute standard deviation
np.var	np.nanvar	Compute variance
np.min	np.nanmin	Find minimum value
np.max	np.nanmax	Find maximum value
np.argmin	np.nanargmin	Find index of minimum value
np.argmax	np.nanargmax	Find index of maximum value
np.median	np.nanmedian	Compute median of elements
np.percentile	np.nanpercentile	Compute rank-based statistics of elements
np.any	N/A	Evaluate whether any elements are true
np.all	N/A	Evaluate whether all elements are true
We will see these aggregates often throughout the rest of the book.
"""
#broadcasting

"""
广播允许在不同大小的数组上执行这些类型的二进制操作 - 例如，我们可以轻松地将标量（将其视为零维数组）添加到数组中：
我们可以将其视为将值拉伸或复制到数组中的操作，并将结果相加。 NumPy广播的优势在于，这种价值观的重复实际上并没有发生，但是当我们考虑广播时，它是一个有用的心理模型。5[5, 5, 5]
"""

#逻辑和函数的等价
Operator	Equivalent ufunc	Operator	Equivalent ufunc
==	np.equal		!=	np.not_equal
<	np.less		<=	np.less_equal
>	np.greater		>=	np.greater_equal

#是否包含某些
np.all(x < 10)
np.any(x < 10)

#逻辑和函数的一致
Operator	Equivalent ufunc		Operator	Equivalent ufunc
&	np.bitwise_and		|	np.bitwise_or
^	np.bitwise_xor		~	np.bitwise_not

#布尔作为掩码
x[x < 5]
#返回符合条件的

#一些逻辑符号 and or & |
#花式索引
ind = [3, 7, 4]
x[ind]
row = np.array([0, 1, 2])
col = np.array([2, 1, 3])
X[row, col]
X[:,range(4)]

#组合索引
X[2, [2, 0, 1]]
X[1:, [2, 0, 1]]
mask = np.array([1, 0, 1, 0], dtype=bool)
X[row[:, np.newaxis], mask]

#索引修改值
x = np.arange(10)
i = np.array([2, 1, 8, 4])
x[i] = 99
print(x)

x[i] -= 10

x = np.zeros(10)
x[[0, 0]] = [4, 6]

i = [2, 3, 3, 4, 4, 4]
x[i] += 1

np.add.at(x, i, 1)#根据i次来执行1

排序
x.sort
# sort each column of X
np.sort(X, axis=0)
# sort each row of X
np.sort(X, axis=1)
#返回排序的索引
x = np.array([2, 1, 4, 3, 5])
i = np.argsort(x)
#取一个数组和一个数字 K;结果是一个新数组，其中最小的 K 值位于分区的左侧，其余值位于右侧，顺序为任意顺序
np.partition
#多维数组
np.partition(X, 2, axis=1)
#简单排序算法
import numpy as np

def selection_sort(x):
    for i in range(len(x)):
        swap = i + np.argmin(x[i:])
        (x[i], x[swap]) = (x[swap], x[i])
    return x
#bogsort
def bogosort(x):
    while np.any(x[:-1] > x[1:]):
        np.random.shuffle(x)
    return x

#创造结构化数组
np.dtype({'names':('name', 'age', 'weight'),
          'formats':('U10', 'i4', 'f8')})
#复合型定义元组
np.dtype([('name', 'S10'), ('age', 'i4'), ('weight', 'f8')])

"""
Character	Description	Example
'b'	Byte	np.dtype('b')
'i'	Signed integer	np.dtype('i4') == np.int32
'u'	Unsigned integer	np.dtype('u1') == np.uint8
'f'	Floating point	np.dtype('f8') == np.int64
'c'	Complex floating point	np.dtype('c16') == np.complex128
'S', 'a'	String	np.dtype('S5')
'U'	Unicode string	np.dtype('U') == np.str_
'V'	Raw data (void)	np.dtype('V') == np.void
"""

#数组和列表的区别  数组都是一种类型的 列表都是不同类型的

#pandas
data = pd.Series([0.25, 0.5, 0.75, 1.0])
Series values index values
# [1:3] 切片和索引都可以访问

data = pd.Series([0.25, 0.5, 0.75, 1.0],
                 index=['a', 'b', 'c', 'd'])

population_dict = {'California': 38332521,
                   'Texas': 26448193,
                   'New York': 19651127,
                   'Florida': 19552860,
                   'Illinois': 12882135}
population = pd.Series(population_dict)
pd.Series(data, index=index)
#取交集等
indA & indB  # intersection
indA | indB  # union
indA ^ indB  # symmetric difference
#判断是否在里面
'a' in data
#首先，该属性允许始终引用显式索引的索引和切片：loc 行
#该属性允许索引和切片始终引用隐式 Python 样式索引：iloc 行
#建立数据框
area = pd.Series({'California': 423967, 'Texas': 695662,
                  'New York': 141297, 'Florida': 170312,
                  'Illinois': 149995})
pop = pd.Series({'California': 38332521, 'Texas': 26448193,
                 'New York': 19651127, 'Florida': 19552860,
                 'Illinois': 12882135})
data = pd.DataFrame({'area':area, 'pop':pop})
#一种方法
data.area = data['area']
#并集
area.index | population.index
#增加没有的部分
A.add(B, fill_value=0)os.listdir(file_PATH)  os.listdir(file_PATH)  os.listdir(file_PATH)  
#列相加
A + B
#
"""

python运算符	pandas
+	add()
-	sub(),subtract()
*	mul(),multiply()
/	truediv(), ,div()divide()
//	floordiv()
%	mod()
**	pow()
"""
#建立数据框
pd.DataFrame(np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]),
                    columns=list("abc"))
df.subtract(df['R'], axis=0) #列
df.subtract(df['R'], axis=1) #行

#选择列
df[['A', 'B']]
df.loc[:, 'B']
#行的切片然后到2
df.iloc[0, ::2]
"""
Typeclass	Conversion When Storing NAs	NA Sentinel Value
floating	No change	np.nan
object	No change	None or np.nan
integer	Cast to float64	np.nan
boolean	Cast to object	None or np.nan"
"""
"""
isnull()：生成指示缺失值的布尔掩码
notnull()： 与 相反isnull()
dropna()：返回数据的过滤版本
fillna()：返回填充或插补缺失值的数据副本
"""
#删除缺失值
df.dropna(axis='columns', how='all')
df.dropna(axis='rows', thresh=3)
#填充缺失值
# forward-fill
data.fillna(method='ffill')
# back-fill
data.fillna(method='bfill')
df.fillna(method='ffill', axis=1)
#直接引索
#使用此索引方案，您可以根据以下多个索引直接对序列进行索引或切片：
pop[('California', 2010):('Texas', 2000)]
#写判断语句 series
pop[[i for i in pop.index if i[1] == 2010]]
#多引索
index = pd.MultiIndex.from_tuples(index)
pop.reindex(index)
MultiIndex
#现在要访问第二个索引为 2010 的所有数据，我们可以简单地使用 Pandas 切片符号：
pop[:, 2010]
#等于melt
#Series unstack() DataFrame stack()
#创造多素引的办法
df = pd.DataFrame(np.random.rand(4, 2),
                  index=[['a', 'a', 'b', 'b'], [1, 2, 1, 2]],
                  columns=['data1', 'data2'])
#构造索引
pd.MultiIndex.from_arrays([['a', 'a', 'b', 'b'], [1, 2, 1, 2]])
#您可以从元组列表构造它，给出每个点的多个索引值
pd.MultiIndex.from_tuples([('a', 1), ('a', 2), ('b', 1), ('b', 2)])
pd.MultiIndex.from_product([['a', 'b'], [1, 2]])
#设置索引名字
pop.index.names = ['state', 'year']
#索引切片
pop[index1, index2]
pop.loc['California':'New York']
pop[:, 2000]
pop[pop > 22000000]
#数据框索引
#locilocix
health_data.iloc[:2, :2]
health_data.loc[:, ('Bob', 'HR')]
#重新排序多索引
MultiIndexsort_index()
sortlevel()
DataFramesort_index()
#数据框消融
pop.unstack(level=0)
pop.unstack(level=1)
pop.unstack().stack()

#索引设置和重置
pop_flat = pop.reset_index(name='population')
pop_flat.set_index(['state', 'year'])

#数据融合
health_data.mean(level='year')
#通过进一步利用关键字，我们也可以取列上级别之间的平均值：axis
data_mean.mean(axis=1, level='type')

#series 合并
np.concatenate([x, y, z])
np.concatenate([x, x], axis=1)#行
np.concatenate([x, x], axis=0)#列
#pandas的合并
pd.concat([ser1, ser2]) #合并行
pd.concat([df3, df4], axis='col')#合并列
#忽略重复索引
pd.concat([x, y], verify_integrity=True)

pd.concat([x, y],ignore_index=True)
#添加多索引
display('x', 'y', "pd.concat([x, y], keys=['x', 'y'])")
#合并行
pd.concat([df5, df6])
df1.append（df2）
#合并行留下列的交集
pd.concat([df5, df6], join='inner')
pd.concat([df5, df6], join_axes=[df5.columns])
#合并多的列 可以一对多 也可以多对多
pd.merge(df1, df2)
#基于某列进行合并
pd.merge（df1， df2， on='employee'）
#致使两个列名来合并
pd.merge（df1， df3， left_on=“employee”， right_on=“name”）
#根据两列合并以后删除某列
pd.merge(df1, df3, left_on="employee", right_on="name").drop('name', axis=1)
#增加列，根据两个一致的索引
pd.merge（df1a， df2a， left_index=True， right_index=True）
df1a.join(df2a)
pd.merge（df1a， df3， left_index=True， right_on='name'）
#合并列的交集
pd.merge(df6, df7, how='inner')
#合并列的所有
pd.merge(df6, df7, how='outer')
#左右位置的设定
pd.merge（df6， df7， how='left'）
#处理列名一致的情况
pd.merge（df8， df9， on=“name”， suffixes=[“_L”， “_R”]）
#检查是否有空值
.isnull().any()
#每一行的值
df.mean(axis='columns')
#每一列的
df.mean()
#删除极端值后的描述
planets.dropna().describe()
"""
The following table summarizes some other built-in Pandas aggregations:

Aggregation	Description
count()	Total number of items
first(), last()	First and last item
mean(), median()	Mean and median
min(), max()	Minimum and maximum
std(), var()	Standard deviation and variance
mad()	Mean absolute deviation
prod()	Product of all items
sum()	Sum of all items
"""
#根据组来用方法
df.groupby('key').x
#累加的计算结果
df.groupby('key').aggregate(['min', np.median, max])
#数据透视表
titanic.pivot_table('survived', index='sex', columns='class')
#多层数据透视表
age = pd.cut(titanic['age'], [0, 18, 80])
titanic.pivot_table('survived', ['sex', age], 'class')
#pandas 字符串的方法
"""
len()	lower()	translate()	islower()
ljust()	upper()	startswith()	isupper()
rjust()	find()	endswith()	isnumeric()
center()	rfind()	isalnum()	isdecimal()
zfill()	index()	isalpha()	split()
strip()	rindex()	isdigit()	rsplit()
rstrip()	capitalize()	isspace()	partition()
lstrip()	swapcase()	istitle()	rpartition()
"""
monte.str.lower()
monte.str.len()
monte.str.startswith('T')
monte.str.split()

"""
此外，还有几种方法接受正则表达式来检查每个字符串元素的内容，并遵循 Python 内置模块的一些 API 约定：re
方法	描述
match()	调用每个元素，返回一个布尔值。re.match()
extract()	调用每个元素，以字符串形式返回匹配的组。re.match()
findall()	调用每个元素re.findall()
replace()	用其他字符串替换出现的模式
contains()	调用每个元素，返回一个布尔值re.search()
count()	计算模式的出现次数
split()	等效于 ，但接受正则表达式str.split()
rsplit()	等效于 ，但接受正则表达式str.rsplit()
"""

"""
最后，还有一些杂项方法可以实现其他方便的操作：
方法	描述
get()	为每个元素编制索引
slice()	对每个元素进行切片
slice_replace()	将每个元素中的切片替换为传递的值
cat()	连接字符串
repeat()	重复值
normalize()	返回字符串的 Unicode 形式
pad()	在字符串的左侧、右侧或两侧添加空格
wrap()	将长字符串拆分为长度小于给定宽度的行
join()	使用传递的分隔符联接系列的每个元素中的字符串
get_dummies()	将虚拟变量提取为数据帧
"""

#def 才有 return
"""
1返回函数值
2结束函数
"""

#匹配
str.startswith()、str.endswith()、str.contains()或正则表达式等

#在 Python 的 Pandas 库中，Series 和 DataFrame 是两种不同的数据结构，用于处理和分析数据。
#Series: 定义： Series 是一维标签化数组，可以包含任何数据类型。它由两个主要部分组成：索引（index）和数据（data）。\
#创建： 可以通过将列表、数组或字典转换为 Series 来创建。索引默认是从 0 开始的整数。
#特点： Series 只有一列，类似于一维数组或列表。可以通过索引访问数据。
import pandas as pd
# 创建一个 Series
s = pd.Series([1, 2, 3, 4])

#DataFrame: 定义： DataFrame 是一个二维的表格数据结构，可以看作是由多个 Series 组成的字典。每列可以包含不同的数据类型。
#创建： 可以通过传递字典、二维数组或其他数据结构来创建 DataFrame。DataFrame 有行索引和列索引。
#特点： DataFrame 是一个表格，类似于数据库表或电子表格。可以通过列名和行索引来访问数据。
import pandas as pd
# 创建一个 DataFrame
data = {'Column1': [1, 2, 3, 4],
        'Column2': ['A', 'B', 'C', 'D']}
df = pd.DataFrame(data)




#matplotlib
#pre_request
import matplotlib
matplotlib.use('Agg') ## TkAgg、QtAgg

#General Matplotlib part
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
plt.style.use('classic')
x = np.linspace(0, 10, 100)
plt.plot(x, np.sin(x))
plt.plot(x, np.cos(x))
plt.show()
#不同线条的
import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(0, 10, 100)
fig = plt.figure()
plt.plot(x, np.sin(x), '-')
plt.plot(x, np.cos(x), '--');

fig.savefig('my_figure.png')#保存图片

from IPython.display import Image
Image('my_figure.png')

fig.canvas.get_supported_filetypes()#查看支持的文件格式
#创建两个图层
plt.figure()  # create a plot figure
# create the first of two panels and set current axis
plt.subplot(2, 1, 1) # (rows, columns, panel number)
plt.plot(x, np.sin(x))
# create the second panel and set current axis
plt.subplot(2, 1, 2)
plt.plot(x, np.cos(x));

#上一个图层的镜像
# First create a grid of plots
# ax will be an array of two Axes objects
fig, ax = plt.subplots(2)

# Call plot() method on the appropriate object
ax[0].plot(x, np.sin(x))
ax[1].plot(x, np.cos(x));

#设置风格和fig 和ax
import matplotlib.pyplot as plt
plt.style.use('seaborn-whitegrid')#设置风格
import numpy as np
fig = plt.figure()
ax = plt.axes()
#叠加多个
plt.plot(x, np.sin(x))
plt.plot(x, np.cos(x));
#调整线的颜色
plt.plot(x, np.sin(x - 0), color='blue')        # specify color by name
plt.plot(x, np.sin(x - 1), color='g')           # short color code (rgbcmyk)
plt.plot(x, np.sin(x - 2), color='0.75')        # Grayscale between 0 and 1
plt.plot(x, np.sin(x - 3), color='#FFDD44')     # Hex code (RRGGBB from 00 to FF)
plt.plot(x, np.sin(x - 4), color=(1.0,0.2,0.3)) # RGB tuple, values 0 to 1
plt.plot(x, np.sin(x - 5), color='chartreuse'); # all HTML color names supported
#调整线的style
plt.plot(x, x + 0, linestyle='solid')
plt.plot(x, x + 1, linestyle='dashed')
plt.plot(x, x + 2, linestyle='dashdot')
plt.plot(x, x + 3, linestyle='dotted');
# For short, you can use the following codes:
plt.plot(x, x + 4, linestyle='-')  # solid
plt.plot(x, x + 5, linestyle='--') # dashed
plt.plot(x, x + 6, linestyle='-.') # dashdot
plt.plot(x, x + 7, linestyle=':');  # dotted
#设置坐标轴刻度
plt.xlim(-1, 11)
plt.ylim(-1.5, 1.5);
#[xmin, xmax, ymin, ymax]:
plt.axis([])

#标记label The position, size, and style 可调整supported values are 'normal', 'italic', 'oblique'
plt.plot(x, np.sin(x), '-g', label='sin(x)')
plt.title("A Sine Curve")
plt.xlabel("x")
plt.ylabel("sin(x)");
#坐标轴的缩放
plt.axis('equal');
plt.axis('tight');
#添加legend
plt.plot(x, np.sin(x), '-g', label='sin(x)')
plt.plot(x, np.cos(x), ':b', label='cos(x)')
plt.axis('equal')
plt.legend();
#在面向对象的绘图接口中，使用该方法一次设置所有这些属性通常比单独调用这些函数更方便：ax.set()
pltaxplt.plot()
ax.plot()
plt.legend()
ax.legend()
"""
虽然大多数函数直接转换为方法（例如 → ， → 等），但并非所有命令都是如此。 特别是，设置限制、标签和标题的功能略有修改。 要在 MATLAB 样式函数和面向对象方法之间转换，请进行以下更改
plt.xlabel()→ax.set_xlabel()
plt.ylabel()→ax.set_ylabel()
plt.xlim()→ax.set_xlim()
plt.ylim()→ax.set_ylim()
plt.title()→ax.set_title()
"""
#画图的类型
plt.plot(x, y, 'o', color='black');#
#设置批量注释
rng = np.random.RandomState(0)
for marker in ['o', '.', ',', 'x', '+', 'v', '^', '<', '>', 's', 'd']:
    plt.plot(rng.rand(5), rng.rand(5), marker,
             label="marker='{0}'".format(marker))
plt.legend(numpoints=1)
plt.xlim(0, 1.8);
#点连线
plt.plot(x, y, '-ok');
plt.plot(x, y, '-p', color='gray',
         markersize=15, linewidth=4,
         markerfacecolor='white',
         markeredgecolor='gray',
         markeredgewidth=2)
plt.ylim(-1.2, 1.2);
#其他形式
#This type of flexibility in the function allows for a wide variety of possible visualization options. For a full description of the options available, refer to the documentation.plt.plotplt.plot
#控制颜色大小
#can be individually controlled or mapped to data.plt.scatterplt.plotcan be individually controlled or mapped to data.plt.scatterplt.plot
rng = np.random.RandomState(0)
x = rng.randn(100)
y = rng.randn(100)
colors = rng.rand(100)
sizes = 1000 * rng.rand(100)

plt.scatter(x, y, c=colors, s=sizes, alpha=0.3,
            cmap='viridis')
plt.colorbar();  # show color scale

#画误差棒
%matplotlib inline
import matplotlib.pyplot as plt
plt.style.use('seaborn-whitegrid')
import numpy as np
x = np.linspace(0, 10, 50)
dy = 0.8
y = np.sin(x) + dy * np.random.randn(50)

plt.errorbar(x, y, yerr=dy, fmt='.k');

#改变bar的属性
plt.errorbar(x, y, yerr=dy, fmt='o', color='black',
             ecolor='lightgray', elinewidth=3, capsize=0);

#
import matplotlib.pyplot as plt
plt.style.use('seaborn-white')
import numpy as np
def f(x, y):
    return np.sin(x) ** 10 + np.cos(10 + y * x) * np.cos(x)
x = np.linspace(0, 5, 50)
y = np.linspace(0, 5, 40)

X, Y = np.meshgrid(x, y)
Z = f(X, Y)
plt.contour(X, Y, Z, colors='black');
#改颜色
plt.contour(X, Y, Z, 20, cmap='RdGy');
#改颜色加颜色bar
plt.contourf(X, Y, Z, 20, cmap='RdGy')
plt.colorbar();
#改变不知道
plt.imshow(Z, extent=[0, 5, 0, 5], origin='lower',
           cmap='RdGy')
plt.colorbar()
plt.axis(aspect='image');

"""
There are a few potential gotchas with , however:imshow()
plt.imshow() doesn't accept an x and y grid, so you must manually specify the extent [xmin, xmax, ymin, ymax] of the image on the plot.
plt.imshow() by default follows the standard image array definition where the origin is in the upper left, not in the lower left as in most contour plots. This must be changed when showing gridded data.
plt.imshow() will automatically adjust the axis aspect ratio to match the input data; this can be changed by setting, for example, to make x and y units match.plt.axis(aspect='image')
"""

#透明度和标度
contours = plt.contour(X, Y, Z, 3, colors='black')
plt.clabel(contours, inline=True, fontsize=8)

plt.imshow(Z, extent=[0, 5, 0, 5], origin='lower',
           cmap='RdGy', alpha=0.5)
plt.colorbar();

#柱状图
import numpy as np
import matplotlib.pyplot as plt
plt.style.use('seaborn-white')
data = np.random.randn(1000)
plt.hist(data);
#改变性状
plt.hist(data, bins=30, normed=True, alpha=0.5,
         histtype='stepfilled', color='steelblue',
         edgecolor='none');
#呈现多组
x1 = np.random.normal(0, 0.8, 1000)
x2 = np.random.normal(-2, 1, 1000)
x3 = np.random.normal(3, 2, 1000)

kwargs = dict(histtype='stepfilled', alpha=0.3, normed=True, bins=40)

plt.hist(x1, **kwargs)
plt.hist(x2, **kwargs)
plt.hist(x3, **kwargs);

# Two-dimensional histogram
mean = [0, 0]
cov = [[1, 1], [1, 2]]
x, y = np.random.multivariate_normal(mean, cov, 10000).T

plt.hist2d(x, y, bins=30, cmap='Blues')
cb = plt.colorbar()
cb.set_label('counts in bin')
#bzds sm
from scipy.stats import gaussian_kde

# fit an array of size [Ndim, Nsamples]
data = np.vstack([x, y])
kde = gaussian_kde(data)

# evaluate on a regular grid
xgrid = np.linspace(-3.5, 3.5, 40)
ygrid = np.linspace(-6, 6, 40)
Xgrid, Ygrid = np.meshgrid(xgrid, ygrid)
Z = kde.evaluate(np.vstack([Xgrid.ravel(), Ygrid.ravel()]))

# Plot the result as an image
plt.imshow(Z.reshape(Xgrid.shape),
           origin='lower', aspect='auto',
           extent=[-3.5, 3.5, -6, 6],
           cmap='Blues')
cb = plt.colorbar()
cb.set_label("density")

#修改legend
import matplotlib.pyplot as plt
plt.style.use('classic')
import numpy as np
x = np.linspace(0, 10, 1000)
fig, ax = plt.subplots()
ax.plot(x, np.sin(x), '-b', label='Sine')
ax.plot(x, np.cos(x), '--r', label='Cosine')
ax.axis('equal')
leg = ax.legend();

#修改legend的位置
ax.legend(loc='upper left', frameon=False)
ax.legend(frameon=False, loc='lower center', ncol=2)
ax.legend(fancybox=True, framealpha=1, shadow=True, borderpad=1) #legend的增加边框

#根据输入的来选择legend
y = np.sin(x[:, np.newaxis] + np.pi * np.arange(0, 2, 0.5))
lines = plt.plot(x, y)

# lines is a list of plt.Line2D instances
plt.legend(lines[:3], ['first', 'second', "third"]);

#第二种方法
plt.plot(x, y[:, 0], label='first')
plt.plot(x, y[:, 1], label='second')
plt.plot(x, y[:, 2:])
plt.legend(framealpha=1, frameon=True);

#增加点的legend
import pandas as pd
cities = pd.read_csv('data/california_cities.csv')

# Extract the data we're interested in
lat, lon = cities['latd'], cities['longd']
population, area = cities['population_total'], cities['area_total_km2']

# Scatter the points, using size and color but no label
plt.scatter(lon, lat, label=None,
            c=np.log10(population), cmap='viridis',
            s=area, linewidth=0, alpha=0.5)
plt.axis(aspect='equal')
plt.xlabel('longitude')
plt.ylabel('latitude')
plt.colorbar(label='log$_{10}$(population)')
plt.clim(3, 7)

# Here we create a legend:
# we'll plot empty lists with the desired size and label
for area in [100, 300, 500]:
    plt.scatter([], [], c='k', alpha=0.3, s=area,
                label=str(area) + ' km$^2$')
plt.legend(scatterpoints=1, frameon=False, labelspacing=1, title='City Area')

plt.title('California Cities: Area and Population');

#Multiple Legends
fig, ax = plt.subplots()

lines = []
styles = ['-', '--', '-.', ':']
x = np.linspace(0, 10, 1000)

for i in range(4):
    lines += ax.plot(x, np.sin(x - i * np.pi / 2),
                     styles[i], color='black')
ax.axis('equal')

# specify the lines and labels of the first legend
ax.legend(lines[:2], ['line A', 'line B'],
          loc='upper right', frameon=False)

# Create the second legend and add the artist manually.
from matplotlib.legend import Legend
leg = Legend(ax, lines[2:], ['line C', 'line D'],
             loc='lower right', frameon=False)
ax.add_artist(leg);

#Customizing Colorbars
import matplotlib.pyplot as plt
plt.style.use('classic')
import numpy as np
x = np.linspace(0, 10, 1000)
I = np.sin(x) * np.cos(x[:, np.newaxis])
plt.imshow(I)
plt.colorbar();

#改颜色
plt.imshow(I, cmap='RdYlGn');
plt.cm.<TAB>#选择颜色

from matplotlib.colors import LinearSegmentedColormap


def grayscale_cmap(cmap):
    """Return a grayscale version of the given colormap"""
    cmap = plt.cm.get_cmap(cmap)
    colors = cmap(np.arange(cmap.N))

    # convert RGBA to perceived grayscale luminance
    # cf. http://alienryderflex.com/hsp.html
    RGB_weight = [0.299, 0.587, 0.114]
    luminance = np.sqrt(np.dot(colors[:, :3] ** 2, RGB_weight))
    colors[:, :3] = luminance[:, np.newaxis]

    return LinearSegmentedColormap.from_list(cmap.name + "_gray", colors, cmap.N)


def view_colormap(cmap):
    """Plot a colormap with its grayscale equivalent"""
    cmap = plt.cm.get_cmap(cmap)
    colors = cmap(np.arange(cmap.N))

    cmap = grayscale_cmap(cmap)
    grayscale = cmap(np.arange(cmap.N))

    fig, ax = plt.subplots(2, figsize=(6, 2),
                           subplot_kw=dict(xticks=[], yticks=[]))
    ax[0].imshow([colors], extent=[0, 10, 0, 1])
    ax[1].imshow([grayscale], extent=[0, 10, 0, 1])
view_colormap('jet')
view_colormap('viridis')
view_colormap('cubehelix')
view_colormap('RdBu')

#缩放旁边的colorbar
# make noise in 1% of the image pixels
speckles = (np.random.random(I.shape) < 0.01)
I[speckles] = np.random.normal(0, 3, np.count_nonzero(speckles))

plt.figure(figsize=(10, 3.5))

plt.subplot(1, 2, 1)
plt.imshow(I, cmap='RdBu')
plt.colorbar()

plt.subplot(1, 2, 2)
plt.imshow(I, cmap='RdBu')
plt.colorbar(extend='both')
plt.clim(-1, 1);

#Discrete Color Bars 区别颜色的bar 把某个颜色区分
plt.imshow(I, cmap=plt.cm.get_cmap('Blues', 6))
plt.colorbar()
plt.clim(-1, 1);

#example
# load images of the digits 0 through 5 and visualize several of them
from sklearn.datasets import load_digits
digits = load_digits(n_class=6)

fig, ax = plt.subplots(8, 8, figsize=(6, 6))
for i, axi in enumerate(ax.flat):
    axi.imshow(digits.images[i], cmap='binary')
    axi.set(xticks=[], yticks=[])

# project the digits into 2 dimensions using IsoMap
from sklearn.manifold import Isomap
iso = Isomap(n_components=2)
projection = iso.fit_transform(digits.data)

# plot the results
plt.scatter(projection[:, 0], projection[:, 1], lw=0.1,
            c=digits.target, cmap=plt.cm.get_cmap('cubehelix', 6))
plt.colorbar(ticks=range(6), label='digit value')
plt.clim(-0.5, 5.5)

#Multiple Subplots
import matplotlib.pyplot as plt
plt.style.use('seaborn-white')
import numpy as np
ax1 = plt.axes()  # standard axes
ax2 = plt.axes([0.65, 0.65, 0.2, 0.2]) #[left, bottom, width, height]

fig = plt.figure()
ax1 = fig.add_axes([0.1, 0.5, 0.8, 0.4],
                   xticklabels=[], ylim=(-1.2, 1.2))
ax2 = fig.add_axes([0.1, 0.1, 0.8, 0.4],
                   ylim=(-1.2, 1.2))
x = np.linspace(0, 10)
ax1.plot(np.sin(x))
ax2.plot(np.cos(x));

#Simple Grids of Subplots
for i in range(1, 7):
    plt.subplot(2, 3, i)
    plt.text(0.5, 0.5, str((2, 3, i)),
             fontsize=18, ha='center')

#创造2*3的网格并打字
fig, ax = plt.subplots(2, 3, sharex='col', sharey='row')
# axes are in a two-dimensional array, indexed by [row, col]
for i in range(2):
    for j in range(3):
        ax[i, j].text(0.5, 0.5, str((i, j)),
                      fontsize=18, ha='center')
fig

#More Complicated Arrangements
#更加复杂的排版
grid = plt.GridSpec(2, 3, wspace=0.4, hspace=0.3)
plt.subplot(grid[0, 0])
plt.subplot(grid[0, 1:])
plt.subplot(grid[1, :2])
plt.subplot(grid[1, 2]);
# Create some normally distributed data
mean = [0, 0]
cov = [[1, 1], [1, 2]]
x, y = np.random.multivariate_normal(mean, cov, 3000).T

# Set up the axes with gridspec
fig = plt.figure(figsize=(6, 6))
grid = plt.GridSpec(4, 4, hspace=0.2, wspace=0.2)
main_ax = fig.add_subplot(grid[:-1, 1:])
y_hist = fig.add_subplot(grid[:-1, 0], xticklabels=[], sharey=main_ax)
x_hist = fig.add_subplot(grid[-1, 1:], yticklabels=[], sharex=main_ax)

# scatter points on the main axes
main_ax.plot(x, y, 'ok', markersize=3, alpha=0.2)

# histogram on the attached axes
x_hist.hist(x, 40, histtype='stepfilled',
            orientation='vertical', color='gray')
x_hist.invert_yaxis()

y_hist.hist(y, 40, histtype='stepfilled',
            orientation='horizontal', color='gray')
y_hist.invert_xaxis()

#Text and Annotation
import matplotlib.pyplot as plt
import matplotlib as mpl
plt.style.use('seaborn-whitegrid')
import numpy as np
import pandas as pd
path = r"C:\Users\79403\Desktop\birth.txt"

births = pd.read_csv(path)

quartiles = np.percentile(births['births'], [25, 50, 75])
mu, sig = quartiles[1], 0.74 * (quartiles[2] - quartiles[0])
births = births.query('(births > @mu - 5 * @sig) & (births < @mu + 5 * @sig)')

births['day'] = births['day'].astype(int)

births.index = pd.to_datetime(10000 * births.year +
                              100 * births.month +
                              births.day, format='%Y%m%d')
births_by_date = births.pivot_table('births',
                                    [births.index.month, births.index.day])
births_by_date.index = [pd.datetime(2012, month, day)
                        for (month, day) in births_by_date.index]

fig, ax = plt.subplots(figsize=(12, 4))
births_by_date.plot(ax=ax);

#添加文字 plt.text/ax.text
fig, ax = plt.subplots(figsize=(12, 4))
births_by_date.plot(ax=ax)

# Add labels to the plot
style = dict(size=10, color='gray')

ax.text('2012-1-1', 3950, "New Year's Day", **style)
ax.text('2012-7-4', 4250, "Independence Day", ha='center', **style)
ax.text('2012-9-4', 4850, "Labor Day", ha='center', **style)
ax.text('2012-10-31', 4600, "Halloween", ha='right', **style)
ax.text('2012-11-25', 4450, "Thanksgiving", ha='center', **style)
ax.text('2012-12-25', 3850, "Christmas ", ha='right', **style)

# Label the axes
ax.set(title='USA births by day of year (1969-1988)',
       ylabel='average daily births')

# Format the x axis with centered month labels
ax.xaxis.set_major_locator(mpl.dates.MonthLocator())
ax.xaxis.set_minor_locator(mpl.dates.MonthLocator(bymonthday=15))
ax.xaxis.set_major_formatter(plt.NullFormatter())
ax.xaxis.set_minor_formatter(mpl.dates.DateFormatter('%h'));

#Transforms and Text Position
fig, ax = plt.subplots(facecolor='lightgray')
ax.axis([0, 10, 0, 10])

# transform=ax.transData is the default, but we'll specify it anyway
ax.text(1, 5, ". Data: (1, 5)", transform=ax.transData)
ax.text(0.5, 0.1, ". Axes: (0.5, 0.1)", transform=ax.transAxes)
ax.text(0.2, 0.2, ". Figure: (0.2, 0.2)", transform=fig.transFigure);
#改变坐标轴
ax.set_xlim(0, 2)
ax.set_ylim(-6, 6)
fig

#Arrows and Annotation
fig, ax = plt.subplots()

x = np.linspace(0, 20, 1000)
ax.plot(x, np.cos(x))
ax.axis('equal')

ax.annotate('local maximum', xy=(6.28, 1), xytext=(10, 4),
            arrowprops=dict(facecolor='black', shrink=0.05))

ax.annotate('local minimum', xy=(5 * np.pi, -1), xytext=(2, -6),
            arrowprops=dict(arrowstyle="->",
                            connectionstyle="angle3,angleA=0,angleB=-90"));

#多重标记坐标轴和arrow
fig, ax = plt.subplots(figsize=(12, 4))
births_by_date.plot(ax=ax)

# Add labels to the plot
ax.annotate("New Year's Day", xy=('2012-1-1', 4100),  xycoords='data',
            xytext=(50, -30), textcoords='offset points',
            arrowprops=dict(arrowstyle="->",
                            connectionstyle="arc3,rad=-0.2"))

ax.annotate("Independence Day", xy=('2012-7-4', 4250),  xycoords='data',
            bbox=dict(boxstyle="round", fc="none", ec="gray"),
            xytext=(10, -40), textcoords='offset points', ha='center',
            arrowprops=dict(arrowstyle="->"))

ax.annotate('Labor Day', xy=('2012-9-4', 4850), xycoords='data', ha='center',
            xytext=(0, -20), textcoords='offset points')
ax.annotate('', xy=('2012-9-1', 4850), xytext=('2012-9-7', 4850),
            xycoords='data', textcoords='data',
            arrowprops={'arrowstyle': '|-|,widthA=0.2,widthB=0.2', })

ax.annotate('Halloween', xy=('2012-10-31', 4600),  xycoords='data',
            xytext=(-80, -40), textcoords='offset points',
            arrowprops=dict(arrowstyle="fancy",
                            fc="0.6", ec="none",
                            connectionstyle="angle3,angleA=0,angleB=-90"))

ax.annotate('Thanksgiving', xy=('2012-11-25', 4500),  xycoords='data',
            xytext=(-120, -60), textcoords='offset points',
            bbox=dict(boxstyle="round4,pad=.5", fc="0.9"),
            arrowprops=dict(arrowstyle="->",
                            connectionstyle="angle,angleA=0,angleB=80,rad=20"))


ax.annotate('Christmas', xy=('2012-12-25', 3850),  xycoords='data',
             xytext=(-30, 0), textcoords='offset points',
             size=13, ha='right', va="center",
             bbox=dict(boxstyle="round", alpha=0.1),
             arrowprops=dict(arrowstyle="wedge,tail_width=0.5", alpha=0.1));

# Label the axes
ax.set(title='USA births by day of year (1969-1988)',
       ylabel='average daily births')

# Format the x axis with centered month labels
ax.xaxis.set_major_locator(mpl.dates.MonthLocator())
ax.xaxis.set_minor_locator(mpl.dates.MonthLocator(bymonthday=15))
ax.xaxis.set_major_formatter(plt.NullFormatter())
ax.xaxis.set_minor_formatter(mpl.dates.DateFormatter('%h'));

ax.set_ylim(3600, 5400);

#Major and Minor Ticks
import matplotlib.pyplot as plt
plt.style.use('classic')
import numpy as np
ax = plt.axes(xscale='log', yscale='log')
ax.grid();

#Hiding Ticks or Labels
ax = plt.axes()
ax.plot(np.random.rand(50))
ax.yaxis.set_major_locator(plt.NullLocator())
ax.xaxis.set_major_formatter(plt.NullFormatter())

#把图片罗列在设定的框内
fig, ax = plt.subplots(5, 5, figsize=(5, 5))
fig.subplots_adjust(hspace=0, wspace=0)

# Get some face data from scikit-learn
from sklearn.datasets import fetch_olivetti_faces
faces = fetch_olivetti_faces().images

for i in range(5):
    for j in range(5):
        ax[i, j].xaxis.set_major_locator(plt.NullLocator())
        ax[i, j].yaxis.set_major_locator(plt.NullLocator())
        ax[i, j].imshow(faces[10 * i + j], cmap="bone")


#Reducing or Increasing the Number of Tick
fig, ax = plt.subplots(4, 4, sharex=True, sharey=True)

# For every axis, set the x and y major locator
# We can fix this with the plt.MaxNLocator(), which allows us to specify the maximum number of ticks that will be displayed
for axi in ax.flat:
    axi.xaxis.set_major_locator(plt.MaxNLocator(3))
    axi.yaxis.set_major_locator(plt.MaxNLocator(3))
fig

#Fancy Tick Formats
# Plot a sine and cosine curve
fig, ax = plt.subplots()
x = np.linspace(0, 3 * np.pi, 1000)
ax.plot(x, np.sin(x), lw=3, label='Sine')
ax.plot(x, np.cos(x), lw=3, label='Cosine')

# Set up grid, legend, and limits
ax.grid(True)
ax.legend(frameon=False)
ax.axis('equal')
ax.set_xlim(0, 3 * np.pi);

ax.xaxis.set_major_locator(plt.MultipleLocator(np.pi / 2))
ax.xaxis.set_minor_locator(plt.MultipleLocator(np.pi / 4))
fig

def format_func(value, tick_number):
    # find number of multiples of pi/2
    N = int(np.round(2 * value / np.pi))
    if N == 0:
        return "0"
    elif N == 1:
        return r"$\pi/2$"
    elif N == 2:
        return r"$\pi$"
    elif N % 2 > 0:
        return r"${0}\pi/2$".format(N)
    else:
        return r"${0}\pi$".format(N // 2)

ax.xaxis.set_major_formatter(plt.FuncFormatter(format_func))
fig

#Summary of Formatters and Locators
"""
Locator class	Description
NullLocator	No ticks
FixedLocator	Tick locations are fixed
IndexLocator	Locator for index plots (e.g., where x = range(len(y)))
LinearLocator	Evenly spaced ticks from min to max
LogLocator	Logarithmically ticks from min to max
MultipleLocator	Ticks and range are a multiple of base
MaxNLocator	Finds up to a max number of ticks at nice locations
AutoLocator	(Default.) MaxNLocator with simple defaults.
AutoMinorLocator	Locator for minor ticks
Formatter Class	Description
NullFormatter	No labels on the ticks
IndexFormatter	Set the strings from a list of labels
FixedFormatter	Set the strings manually for the labels
FuncFormatter	User-defined function sets the labels
FormatStrFormatter	Use a format string for each value
ScalarFormatter	(Default.) Formatter for scalar values
LogFormatter	Default formatter for log axes
"""


#Plot Customization by Hand 画背景
import matplotlib.pyplot as plt
plt.style.use('classic')
import numpy as np

x = np.random.randn(1000)
plt.hist(x);

# use a gray background 改变背景
ax = plt.axes(axisbg='#E6E6E6')
ax.set_axisbelow(True)

# draw solid white grid lines
plt.grid(color='w', linestyle='solid')

# hide axis spines
for spine in ax.spines.values():
    spine.set_visible(False)

# hide top and right ticks
ax.xaxis.tick_bottom()
ax.yaxis.tick_left()

# lighten ticks and labels
ax.tick_params(colors='gray', direction='out')
for tick in ax.get_xticklabels():
    tick.set_color('gray')
for tick in ax.get_yticklabels():
    tick.set_color('gray')

# control face and edge color of histogram
ax.hist(x, edgecolor='#E6E6E6', color='#EE6666');

#Changing the Defaults:
IPython_default = plt.rcParams.copy()
from matplotlib import cycler
colors = cycler('color',
                ['#EE6666', '#3388BB', '#9988DD',
                 '#EECC55', '#88BB44', '#FFBBBB'])
plt.rc('axes', facecolor='#E6E6E6', edgecolor='none',
       axisbelow=True, grid=True, prop_cycle=colors)
plt.rc('grid', color='w', linestyle='solid')
plt.rc('xtick', direction='out', color='gray')
plt.rc('ytick', direction='out', color='gray')
plt.rc('patch', edgecolor='#E6E6E6')
plt.rc('lines', linewidth=2)
plt.hist(x);
#Let's see what simple line plots look like with these rc parameters:
for i in range(4):
    plt.plot(np.random.rand(10))

#Stylesheets
plt.style.available[:5]
plt.style.use('stylename')
with plt.style.context('stylename'):
    make_a_plot()
def hist_and_lines():
    np.random.seed(0)
    fig, ax = plt.subplots(1, 2, figsize=(11, 4))
    ax[0].hist(np.random.randn(1000))
    for i in range(3):
        ax[1].plot(np.random.rand(10))
    ax[1].legend(['a', 'b', 'c'], loc='lower left')

#Default style
# reset rcParams
plt.rcParams.update(IPython_default);
hist_and_lines()
with plt.style.context('fivethirtyeight'):
    hist_and_lines()
with plt.style.context('ggplot'):
    hist_and_lines()
with plt.style.context('bmh'):
    hist_and_lines()
with plt.style.context('dark_background'):
    hist_and_lines()
with plt.style.context('grayscale'):
    hist_and_lines()
#Seaborn style
import seaborn
hist_and_lines()

#Seaborn Versus Matplotlib
import matplotlib.pyplot as plt
plt.style.use('classic')
import numpy as np
import pandas as pd

# Create some data
rng = np.random.RandomState(0)
x = np.linspace(0, 10, 500)
y = np.cumsum(rng.randn(500, 6), 0)

# Plot the data with Matplotlib defaults
plt.plot(x, y)
plt.legend('ABCDEF', ncol=2, loc='upper left');

import seaborn as sns
sns.set()

# same plotting code as above!
plt.plot(x, y)
plt.legend('ABCDEF', ncol=2, loc='upper left');

#Histograms, KDE, and densities
data = np.random.multivariate_normal([0, 0], [[5, 2], [2, 2]], size=2000)
data = pd.DataFrame(data, columns=['x', 'y'])

for col in 'xy':
    plt.hist(data[col], normed=True, alpha=0.5)
#densities
for col in 'xy':
    sns.kdeplot(data[col], shade=True)
#add Histograms
sns.distplot(data['x'])
sns.distplot(data['y']);

#full two-dimensional dataset to kdeplot
sns.kdeplot(data);

#We can see the joint distribution and the marginal distributions together using sns.jointplot. For this plot, we'll set the style to a white background:
with sns.axes_style('white'):
    sns.jointplot("x", "y", data, kind='kde');

#There are other parameters that can be passed to jointplot—for example, we can use a hexagonally based histogram instead:
with sns.axes_style('white'):
    sns.jointplot("x", "y", data, kind='hex')

#Pair plots
iris = sns.load_dataset("iris")
iris.head()
#Visualizing the multidimensional relationships among the samples is as easy as calling sns.pairplot:
sns.pairplot(iris, hue='species', size=2.5);

#Faceted histograms
tips = sns.load_dataset('tips')
tips.head()

tips['tip_pct'] = 100 * tips['tip'] / tips['total_bill']

grid = sns.FacetGrid(tips, row="sex", col="time", margin_titles=True)
grid.map(plt.hist, "tip_pct", bins=np.linspace(0, 40, 15));

#Factor plots
with sns.axes_style(style='ticks'):
    g = sns.factorplot("day", "total_bill", "sex", data=tips, kind="box")
    g.set_axis_labels("Day", "Total Bill");

#Joint distributions
with sns.axes_style('white'):
    sns.jointplot("total_bill", "tip", data=tips, kind='hex')

#The joint plot can even do some automatic kernel density estimation and regression:
sns.jointplot("total_bill", "tip", data=tips, kind='reg');

#Bar plots
planets = sns.load_dataset('planets')
planets.head()
#sns.factorplot
with sns.axes_style('white'):
    g = sns.factorplot("year", data=planets, aspect=2,
                       kind="count", color='steelblue')
    g.set_xticklabels(step=5)
#We can learn more by looking at the method of discovery of each of these planets:
with sns.axes_style('white'):
    g = sns.factorplot("year", data=planets, aspect=4.0, kind='count',
                       hue='method', order=range(2001, 2015))
    g.set_ylabels('Number of Planets Discovered')

#查看数据类型
data.dtypes

data['split_sec'] = data['split'].astype(int) / 1E9
data['final_sec'] = data['final'].astype(int) / 1E9
data.head()
#To get an idea of what the data looks like, we can plot a jointplot over the data:
with sns.axes_style('white'):
    g = sns.jointplot("split_sec", "final_sec", data, kind='hex')
    g.ax_joint.plot(np.linspace(4000, 16000),
                    np.linspace(8000, 32000), ':k')
data['split_frac'] = 1 - 2 * data['split_sec'] / data['final_sec']
data.head()
#画虚线
sns.distplot(data['split_frac'], kde=False);
plt.axvline(0, color="k", linestyle="--");

sum(data.split_frac < 0)

#draws plots of all these correlations:
g = sns.PairGrid(data, vars=['age', 'split_sec', 'final_sec', 'split_frac'],
                 hue='gender', palette='RdBu_r')
g.map(plt.scatter, alpha=0.8)
g.add_legend();

#density
sns.kdeplot(data.split_frac[data.gender=='M'], label='men', shade=True)
sns.kdeplot(data.split_frac[data.gender=='W'], label='women', shade=True)
plt.xlabel('split_frac');

#violinplot
sns.violinplot("gender", "split_frac", data=data,
               palette=["lightblue", "lightpink"]);

#好看的小提琴图
men = (data.gender == 'M')
women = (data.gender == 'W')

with sns.axes_style(style=None):
    sns.violinplot("age_dec", "split_frac", hue="gender", data=data,
                   split=True, inner="quartile",
                   palette=["lightblue", "lightpink"]);


(data.age > 80).sum()

#散点图和拟合曲线
g = sns.lmplot('final_sec', 'split_frac', col='gender', data=data,
               markers=".", scatter_kws=dict(color='c'))
g.map(plt.axhline, y=0.1, color="k", ls=":");

#machine learning
import seaborn as sns
iris = sns.load_dataset('iris')
iris.head()

import seaborn as sns; sns.set()
sns.pairplot(iris, hue='species', size=1.5);

X_iris = iris.drop('species', axis=1)
X_iris.shape

y_iris = iris['species']
y_iris.shape

#Supervised learning example: Simple linear regression
import matplotlib.pyplot as plt
import numpy as np

rng = np.random.RandomState(42)
x = 10 * rng.rand(50)
y = 2 * x - 1 + rng.randn(50)
plt.scatter(x, y);

#1. Choose a class of model
#2. Choose model hyperparameters
#3. Arrange data into a features matrix and target vector
#4. Fit the model to your data
#5. Predict labels for unknown data

from sklearn.linear_model import LinearRegression
model = LinearRegression(fit_intercept=True)
X = x[:, np.newaxis]
X.shape #等于r的table
model.fit(X, y)
model.coef_
model.intercept_
xfit = np.linspace(-1, 11)

Xfit = xfit[:, np.newaxis]
yfit = model.predict(Xfit)

plt.scatter(x, y)
plt.plot(xfit, yfit);

#Supervised learning example: Iris classification
#Gaussian naive Bayes
#data
from sklearn.model_selection import train_test_split
Xtrain, Xtest, ytrain, ytest = train_test_split(X_iris, y_iris,
                                                random_state=1)
#model
from sklearn.naive_bayes import GaussianNB # 1. choose model class
model = GaussianNB()                       # 2. instantiate model
model.fit(Xtrain, ytrain)                  # 3. fit model to data
y_model = model.predict(Xtest)             # 4. predict on new data

#evaluate
from sklearn.metrics import accuracy_score
accuracy_score(ytest, y_model)

#Unsupervised learning example: Iris dimensionality
from sklearn.decomposition import PCA  # 1. Choose the model class
model = PCA(n_components=2)            # 2. Instantiate the model with hyperparameters
model.fit(X_iris)                      # 3. Fit to data. Notice y is not specified!
X_2D = model.transform(X_iris)         # 4. Transform the data to two dimensions

iris['PCA1'] = X_2D[:, 0]
iris['PCA2'] = X_2D[:, 1]
sns.lmplot("PCA1", "PCA2", hue='species', data=iris, fit_reg=False);

#Loading and visualizing the digits data¶
from sklearn.datasets import load_digits
digits = load_digits()
digits.images.shape

import matplotlib.pyplot as plt

fig, axes = plt.subplots(10, 10, figsize=(8, 8),
                         subplot_kw={'xticks':[], 'yticks':[]},
                         gridspec_kw=dict(hspace=0.1, wspace=0.1))

for i, ax in enumerate(axes.flat):
    ax.imshow(digits.images[i], cmap='binary', interpolation='nearest')
    ax.text(0.05, 0.05, str(digits.target[i]),
            transform=ax.transAxes, color='green')

X = digits.data
X.shape
y = digits.target
y.shape


#Unsupervised learning: Dimensionality reduction
import matplotlib.pyplot as plt
import numpy as np
from sklearn.manifold import Isomap
iso = Isomap(n_components=2)
iso.fit(digits.data)
data_projected = iso.transform(digits.data)
data_projected.shape

plt.scatter(data_projected[:, 0], data_projected[:, 1], c=digits.target,
            edgecolor='none', alpha=0.5,
            cmap=plt.cm.get_cmap('spectral', 10))
plt.colorbar(label='digit label', ticks=range(10))
plt.clim(-0.5, 9.5);

#Classification on digits
Xtrain, Xtest, ytrain, ytest = train_test_split(X, y, random_state=0)
from sklearn.naive_bayes import GaussianNB
model = GaussianNB()
model.fit(Xtrain, ytrain)
y_model = model.predict(Xtest)


from sklearn.metrics import accuracy_score
accuracy_score(ytest, y_model)

from sklearn.metrics import confusion_matrix

mat = confusion_matrix(ytest, y_model)

sns.heatmap(mat, square=True, annot=True, cbar=False)
plt.xlabel('predicted value')
plt.ylabel('true value');


fig, axes = plt.subplots(10, 10, figsize=(8, 8),
                         subplot_kw={'xticks':[], 'yticks':[]},
                         gridspec_kw=dict(hspace=0.1, wspace=0.1))

test_images = Xtest.reshape(-1, 8, 8)

for i, ax in enumerate(axes.flat):
    ax.imshow(test_images[i], cmap='binary', interpolation='nearest')
    ax.text(0.05, 0.05, str(y_model[i]),
            transform=ax.transAxes,
            color='green' if (ytest[i] == y_model[i]) else 'red')


#Model validation the right way: Holdout sets
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
# split the data with 50% in each set
X1, X2, y1, y2 = train_test_split(X, y, random_state=0,
                                  train_size=0.5)

# fit the model on one set of data
model.fit(X1, y1)

# evaluate the model on the second set of data
y2_model = model.predict(X2)
accuracy_score(y2, y2_model)


#Model validation via cross-validation 还有留一法
#the initial set of training data is small
#Holdout sets

y2_model = model.fit(X1, y1).predict(X2)
y1_model = model.fit(X2, y2).predict(X1)
accuracy_score(y1, y1_model), accuracy_score(y2, y2_model)
#cross-validation 5
from sklearn.model_selection import cross_val_score
cross_val_score(model, X, y, cv=5)

#Validation curves in Scikit-Learn
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.pipeline import make_pipeline

def PolynomialRegression(degree=2, **kwargs):
    return make_pipeline(PolynomialFeatures(degree),
                         LinearRegression(**kwargs))

import numpy as np

def make_data(N, err=1.0, rseed=1):
    # randomly sample the data
    rng = np.random.RandomState(rseed)
    X = rng.rand(N, 1) ** 2
    y = 10 - 1. / (X.ravel() + 0.1)
    if err > 0:
        y += err * rng.randn(N)
    return X, y

X, y = make_data(40)

import matplotlib.pyplot as plt
import seaborn; seaborn.set()  # plot formatting

X_test = np.linspace(-0.1, 1.1, 500)[:, None]

plt.scatter(X.ravel(), y, color='black')
axis = plt.axis()
for degree in [1, 3, 5]:
    y_test = PolynomialRegression(degree).fit(X, y).predict(X_test)
    plt.plot(X_test.ravel(), y_test, label='degree={0}'.format(degree))
plt.xlim(-0.1, 1.0)
plt.ylim(-2, 12)
plt.legend(loc='best');

from sklearn.learning_curve import validation_curve
degree = np.arange(0, 21)
train_score, val_score = validation_curve(PolynomialRegression(), X, y,
                                          'polynomialfeatures__degree', degree, cv=7)

plt.plot(degree, np.median(train_score, 1), color='blue', label='training score')
plt.plot(degree, np.median(val_score, 1), color='red', label='validation score')
plt.legend(loc='best')
plt.ylim(0, 1)
plt.xlabel('degree')
plt.ylabel('score');

plt.scatter(X.ravel(), y)
lim = plt.axis()
y_test = PolynomialRegression(3).fit(X, y).predict(X_test)
plt.plot(X_test.ravel(), y_test);
plt.axis(lim);


#Learning curves in Scikit-Learn
from sklearn.learning_curve import learning_curve

fig, ax = plt.subplots(1, 2, figsize=(16, 6))
fig.subplots_adjust(left=0.0625, right=0.95, wspace=0.1)

for i, degree in enumerate([2, 9]):
    N, train_lc, val_lc = learning_curve(PolynomialRegression(degree),
                                         X, y, cv=7,
                                         train_sizes=np.linspace(0.3, 1, 25))

    ax[i].plot(N, np.mean(train_lc, 1), color='blue', label='training score')
    ax[i].plot(N, np.mean(val_lc, 1), color='red', label='validation score')
    ax[i].hlines(np.mean([train_lc[-1], val_lc[-1]]), N[0], N[-1],
                 color='gray', linestyle='dashed')

    ax[i].set_ylim(0, 1)
    ax[i].set_xlim(N[0], N[-1])
    ax[i].set_xlabel('training size')
    ax[i].set_ylabel('score')
    ax[i].set_title('degree = {0}'.format(degree), size=14)
    ax[i].legend(loc='best')

#Validation in Practice: Grid Search
#GridSearchCV
from sklearn.model_selection import GridSearchCV

param_grid = {'polynomialfeatures__degree': np.arange(21),
              'linearregression__fit_intercept': [True, False],
              'linearregression__normalize': [True, False]}

grid = GridSearchCV(PolynomialRegression(), param_grid, cv=7)

grid.fit(X, y);
grid.best_params_

#Finally, if we wish, we can use the best model and show the fit to our data using code from before:
model = grid.best_estimator_
plt.scatter(X.ravel(), y)
lim = plt.axis()
y_test = model.fit(X, y).predict(X_test)
plt.plot(X_test.ravel(), y_test, hold=True);
plt.axis(lim);

#Feature Engineering
#Categorical Features
data = [
    {'price': 850000, 'rooms': 4, 'neighborhood': 'Queen Anne'},
    {'price': 700000, 'rooms': 3, 'neighborhood': 'Fremont'},
    {'price': 650000, 'rooms': 3, 'neighborhood': 'Wallingford'},
    {'price': 600000, 'rooms': 2, 'neighborhood': 'Fremont'}
]

#Text Features
sample = ['problem of evil',
          'evil queen',
          'horizon problem']

from sklearn.feature_extraction.text import CountVectorizer

vec = CountVectorizer()
X = vec.fit_transform(sample)
X

#Bayesian Classification
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns;
sns.set()

from sklearn.datasets import make_blobs
X, y = make_blobs(100, 2, centers=2, random_state=2, cluster_std=1.5)
plt.scatter(X[:, 0], X[:, 1], c=y, s=50, cmap='RdBu');
plt.show()

from sklearn.naive_bayes import GaussianNB
model = GaussianNB()
model.fit(X, y);

rng = np.random.RandomState(0)
Xnew = [-6, -14] + [14, 18] * rng.rand(2000, 2)
ynew = model.predict(Xnew)

plt.scatter(X[:, 0], X[:, 1], c=y, s=50, cmap='RdBu')
lim = plt.axis()
plt.scatter(Xnew[:, 0], Xnew[:, 1], c=ynew, s=20, cmap='RdBu', alpha=0.1)
plt.axis(lim);
plt.show()

yprob = model.predict_proba(Xnew)
yprob[-8:].round(2)

##Multinomial Naive Bayes
from sklearn.datasets import fetch_20newsgroups
data = fetch_20newsgroups()
data.target_names

categories = ['talk.religion.misc', 'soc.religion.christian',
              'sci.space', 'comp.graphics']
train = fetch_20newsgroups(subset='train', categories=categories)
test = fetch_20newsgroups(subset='test', categories=categories)

print(train.data[5])

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline

model = make_pipeline(TfidfVectorizer(), MultinomialNB())

model.fit(train.data, train.target)
labels = model.predict(test.data)

from sklearn.metrics import confusion_matrix
mat = confusion_matrix(test.target, labels)
sns.heatmap(mat.T, square=True, annot=True, fmt='d', cbar=False,
            xticklabels=train.target_names, yticklabels=train.target_names)
plt.xlabel('true label')
plt.ylabel('predicted label');
plt.show

def predict_category(s, train=train, model=model):
    pred = model.predict([s])
    return train.target_names[pred[0]]

predict_category('sending a payload to the ISS')

predict_category('discussing islam vs atheism')

predict_category('determining the screen resolution')

#获得工作目录
import os
os.getcwd()
os.chdir(new_directory) #设置工作目录

data.count() #等于r语言的table

 "{}: {}".format(2, 3) #占位符号，可以输出后面format里面的

#机器学习交叉验证的方法
# 训练-测试拆分  k折交叉验证  分层k折交叉验证   留一交叉验证  留出交叉验证(n个验) 蒙特卡罗交叉验证  时间序列交叉验证
#蒙特卡洛
#拆分迭代的次数也可以作为一个超参数来定义。更多的迭代次数会导致更好的性能，但也增加了计算成本。
# 蒙特卡洛交叉验证的每次迭代中拆分是随机进行的，同一个数据点可以多次出现在测试折叠中。但在k折交叉验证中，这种情况不会发生！
# 在蒙特卡洛交叉验证中，有些数据点永远不会被选为验证折叠！

#导入包
import sys
sys.path.append("/path/to/your/script")