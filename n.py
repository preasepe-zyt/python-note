#https://pandas.pydata.org/pandas-docs/stable/user_guide/reshaping.html#exploding-a-list-like-column 文档
# 进行删除多列的操作，此处删除Score1和Score2两列
df = df.drop(['Score1','Score2'], axis=1)
# 进行删除重复值的操作，此处以Sex列为准则进行操作
df = df.drop_duplicates(['Sex'])
# 进行删除空值的操作
df = df.dropna()
import pandas as pd
import glob
import numpy as np
final = pd.concat(objs=[paa, pa2], axis=0, join="outer")
file_list = glob.glob(r'.\order\*xls')
for fp in file_list:
    # Read selected columns of  data using varying amount of spaces as separator and specifying * characters as NoData values
    data = pd.read_csv(fp, sep="/t")
final = final[final['gene_name'] != "-"] #删除为"-"的行
ss = np.intersect1d(pa2['gene_name'], paa['gene_name'])
ss[1:len(ss)]
# 转换数据框
ss1 = pd.DataFrame(ss)
#数据框选择行
ss1.iloc[1] #跟r语言一样
ss1.loc[2]
#转换
np.array(ss)
final_d = final.drop_duplicates(['gene_name'])
a = pd.DataFrame()
for i in ss:
    df = final_d[final_d['gene_name'] == i]
    a = pd.concat([df, a])
col = ["log2FoldChange", "gene_name"]
sort_col = sort_list[col]
fl = abs(sort_col["log2FoldChange"])
sort_list = sort_col.assign(fl=abs(sort_col["log2FoldChange"]))
sort_list = sort_list.sort_values("fl", ascending=True)
sort_col.to_excel('sample_data.xlsx', sheet_name='sheet1', index=False)
