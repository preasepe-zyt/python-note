"""
Python中的正则表达式
正则表达式，又称规则表达式，可用单个字符串来描述、匹配某个句法规则的字符串，常被用来检索、替换哪些符合某个模式的文本(不理解匹配规则的同学可以参考：正则表达式)。Python中的正则表达式可通过re模块中的match、search、findall三个方法来实现
- re.match(匹配规则, 被匹配字符串)

匹配成功则返回匹配对象，匹配不成功则返回空。re.match默认从头部匹配，若头部不匹配，则后面的内容不参与匹配

- re.search

检索整个字符串，找出匹配的，匹配一次后即停止检索。

- re.findall

检索整个字符串，并返回所有匹配结果(值的list)

""""""

一、简单演示

# re.match

# 默认从头部匹配，若头部不匹配，则后面的内容不参与匹配
import re
match_res = re.match('Biomamba','I am Biomamba')
print(match_res)
# 可以看出虽然我们后面的话中包含"Biomamba"，但是结果并没有返回。
## None


# 我们把单词的顺序换一下
match_res = re.match('Biomamba','Biomamba is me')
print(match_res)
# 可以看到返回了字符串对应的坐标
## <_sre.SRE_Match object; span=(0, 8), match='Biomamba'>


# match_res中的信息可以被分别取出：
print(match_res.span())
## (0, 8)

print(match_res.start())
## 0

print(match_res.end())
## 8

# re.search 
# 检索整个字符串，找出匹配的，匹配一次后即停止检索
import re
search_res = re.search('Biomamba','I am Biomamba. Biomamba is me.')
print(search_res)
# 可以看出只返回了第一个"Biomamba"的坐标。
## <_sre.SRE_Match object; span=(5, 13), match='Biomamba'>

# re.findall
# 检索整个字符串，并返回所有匹配结果(值的list)
import re
findall_res = re.findall('Biomamba','I am Biomamba. Biomamba is me.')
print(findall_res)
# 可以看出返回了所有值
## ['Biomamba', 'Biomamba']


print(type(findall_res))
# 返回的对象是一个list
## <class 'list'>


二、元字符

元字符指一类具有特定功能，用于匹配特定字符串的字符。
18.2.1 字符匹配
.
匹配任意1个字符，除了换行符\n和.本身\.

[]
匹配[]中列举的字符

br> 匹配数字字符，即0-9


匹配非数字的字符


匹配空白，包括空格、tab键


匹配非空白


匹配单词字符，即a-z、A-Z、0-9、_



# 简单的举几个例子：
import re
my_word = 'I am Biomamba.This year is 2023 . Biomamba is me.'
# 找出这句话中所有的数字
re.findall('[0-9]',my_word) 
# 可见匹配到的所有数字被列出：
## ['2', '0', '2', '3']


# 或者我们换个写法依旧可以匹配到所有的数字
import re
my_word = 'I am Biomamba.This year is 2023 . Biomamba is me.'
# 找出这句话中所有的数字
re.findall('\d',my_word) 
# 可见匹配到的所有数字被列出：
## ['2', '0', '2', '3']


# 找出所有的大写字母
import re
my_word = 'I am Biomamba.This year is 2023 . Biomamba is me.'

re.findall('[A-Z]',my_word) 
# 可见匹配到的所有的大写字母被列出：
## ['I', 'B', 'T', 'B']


# 找出所有字母
import re
my_word = 'I am Biomamba.This year is 2023 . Biomamba is me.'

re.findall('[A-z]',my_word) 
# 可见匹配到的所有字母被列出：
## ['I', 'a', 'm', 'B', 'i', 'o', 'm', 'a', 'm', 'b', 'a', 'T', 'h', 'i', 's', 'y', 'e', 'a', 'r', 'i', 's', 'B', 'i', 'o', 'm', 'a', 'm', 'b', 'a', 'i', 's', 'm', 'e']


# 找出所有空格及其前面的一个字符
my_word = 'I am Biomamba.This year is 2023 . Biomamba is me.'

re.findall('.\s',my_word)
## ['I ', 'm ', 's ', 'r ', 's ', '3 ', '. ', 'a ', 's ']


# 找出所有空格及其前面的一个字符
my_word = 'I am Biomamba.This year is 2023 . Biomamba is me.'

re.findall('.\s',my_word)
## ['I ', 'm ', 's ', 'r ', 's ', '3 ', '. ', 'a ', 's ']


# 匹配任意字符任意次
re.findall('.*',my_word) 
# 可以看到完整的内容被匹配与打出
## ['I am Biomamba.This year is 2023 . Biomamba is me.', '']
18.2.2 数量匹配：
*
匹配前一个规则的字符任意次(0次至无数次)

+
匹配前一个规则的字符1至无数次

?
匹配前一个规则的字符0次或1次

{m}
匹配前一个规则的字符m次

{m,}
匹配前一个字符最少m次

{m,n}
匹配前一个字符m到n次



import re
my_word = 'I am Biomamba.BBBiomamba. iomamba.This year is 2023 . Biomamba is me.'

# 匹配B字符任意次及后接iomamba字符
re.findall('B*iomamba',my_word)
# 可以看出 Biomamba 、iomamba 和 BBBiomamba 均可以被打印出
## ['Biomamba', 'BBBiomamba', 'iomamba', 'Biomamba']


# 匹配B字符一次及后接iomamba字符
re.findall('B+iomamba',my_word)
# 可以看出iomamba无法被打印出
## ['Biomamba', 'BBBiomamba', 'Biomamba']


# 匹配最少三次B后接iomamba
my_word = 'I am Biomamba. BBiomamba.BBBiomamba. BBBBiomamba .iomamba.This year is 2023 . Biomamba is me.'
re.findall('B{3,}iomamba',my_word)
# 可以看到只有三个及以上的B被输出
## ['BBBiomamba', 'BBBBiomamba']


# 匹配二至三次B后接iomamba
re.findall('B{2,3}iomamba',my_word)
## ['BBiomamba', 'BBBiomamba', 'BBBiomamba']
18.2.3 边界匹配
^
匹配字符串开头

$
匹配字符串结尾

br> 匹配一个单词的边界


匹配一个非单词的边界



import re
my_word = 'I am Biomamba.This year is 2023 . Biomamba is me.'

# 匹配字符串开头和之后的一个字符
re.findall('^.',my_word)
## ['I']


# 匹配字符串结尾和之前的两个字符
re.findall('.{2}$',my_word)
## ['e.']


# 匹配字符串中单词非边界前为a的单词
re.findall('a\B',my_word)
## ['a', 'a', 'a', 'a']
其它匹配依次类推，正则表达式在所有平台与语言中几乎都是通用的，详情可见我们的Linux课程生信小白的Linux保姆级教程。