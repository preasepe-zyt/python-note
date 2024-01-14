#例如：
import re
seq ='RQSAMGSNKSKPKDASQRRRSLEPAENVHGAGGGAFPASQRPSKPrrsl'
pattern = re.compile('R.[ST][^P]',re.I)
#匹配以'R'开头，后一个字符为任意，接下来的字符为'S'或'T'，最后不以'P'结尾的字符串。
#'re.I'表示不区分大小写
matches = pattern.findall(seq)
#找到seq中相匹配的所有字符串
print(matches)