text = str(100)#处理浮点数时会降低可读性
type(text)
#集合是唯一元件的无序组合，不含重复元素
data_a = set([1,2,3,4,5,6])
#等价于data_a ={1,2,3,4,5,6}
#注意：创建一个空集合必须用set()而不是{}，因为{}是用来创建一个空字典。
#也等价于data_a = set([1, 1, 2, 3, 4, 5, 6]) 
data_b = set([1,5,7,8,9])
#list类型数据需先set()转换成set类型才能进行下述代码
a_and_b = data_a.intersection(data_b)#交集
a_not_b = data_a.difference(data_b)#差：取出data_a独有的元素
b_not_a = data_b.difference(data_a)#取出data_b独有的元素
a_or_b = data_a.union(data_b)#并集
a_xor_b = data_a.symmetric_difference(data_b)#对称差：取出不同时存在于二者的元素
print(a_and_b)
print(a_not_b)
print(b_not_a)
print(a_or_b)
print(a_xor_b)

import functools as f#reduce()函数已转移至该模块中(Python3.X)
a ={1,2,3,4,5}
b ={2,4,6,7,1}
c ={1,4,5,9}
triple_set =[a,b,c]
common=f.reduce(set.intersection,triple_set)
#用传给 reduce 中的函数 intersection 先对triple_set中的、b进行操作，
#得到的结果再与c用 intersection 函数运算，最后得到一个结果。
print(common)