import pandas as pd
table =[
[0.16,0.038,0.044,0.040],
[0.33,0.089,0.095,0.091],
[0.66,0.184,0.191,0.191],
[1.00,0.280,0.292,0.283],
[1.32,0.365,0.367,0.365],
[1.66,0.441,0.443,0.444]
]
B = pd.DataFrame(table)

#这个好用，有轮子干嘛不用呢？
import pandas as pd
list1 = [[1,2,3],[4,5,6]]
df = pd.DataFrame(list1)
df.to_csv("test.csv",sep=',',header=False,index=False)

#8.3.6 按长度对字符串排序
data = ['ACCTGGCCA','ACTG','TACGGCAGGAGACG','TTGGATC']
bylength = sorted(data,key=lambda x:len(x))
#lambda函数又称匿名函数，不包括return语句，而是包括一个表达式，
#而且总会返回该表达式的值。
#可以在任何地方定义lambda函数，即便是在未分配名称的另一个函数的参数中。

print(bylength)