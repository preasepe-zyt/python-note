insulin="GIVEQCCTSICSLYQLENYCNFVNQHLCGSHLVEALYLVCGERGFFYTPKT"#胰岛素序列
for amino_acid in "ACDEFGHIKLMNPQRSTVWY":#氨基酸
  number=insulin.count(amino_acid)#计算每一个氨基酸在insulin中的数量
print(amino_acid,number)
#例2.1 创建随机序列
#从'AGCT'中抽取10个字符
import random
alphabet="AGCT"
sequence="序列"
for i in range(10):#0~9，差一索引
   index=random.randint(0,3)
   sequence=sequence+alphabet[index]
print(sequence)
print(index)
#每一次打印出来的结果应该都不一样
#另一种方法
#可重复抽取alphabet中字符
sequence=""
a=sequence.join([random.choice(alphabet) for i in range(10)])
print(a)#用join函数使之返回字符串类型
#不重复抽取alphabet中字符
b = random.sample(alphabet,4)
print(b)#b为list
