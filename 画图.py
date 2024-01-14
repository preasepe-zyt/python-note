#我找到了一个感觉比较好的画图包：plotly
#运行下面的代码需要先用pip安装plotly和plotly-express
#找了一个plotly画图的例子：
import plotly_express as px#这个包里有很多数据可以用来画图
gap = px.data.gapminder().query("year == 2002")
fig = px.scatter(gap
                 ,x="year"
                 ,y="gdpPercap"
                 ,color="continent"
                 ,size="pop"
                 ,size_max=60)
fig.show()
#画出了一张交互式的图。

#Bio.PDB包可用来从网络上检索大分子结构，读写PDB文件，计算原子间的距离和角度，叠加结构。
from Bio import PDB
from Bio.PDB import PDBIO

pdbl = PDB.PDBList()
pdbl.retrieve_pdb_file("2DN1")#下载pdb结构

parser = PDB.PDBParser()#解析pdb结构
structure = parser.get_structure("2DN1","dn/pdb2dn1.ent")
#Structure对象是一个容器，存储PDB数据项中的结构信息，
#这个层次结构可以被简写为SMCRA（Structure→Model（s）→Chain（s）→Residues→Atoms）。

#parser = MMCIFParser() #解析mmCIF文件
#structure = parser.get structure("2DN1","2DN1.cif")

for model in structure:
for chain in model:
print (chain)#打印链
print (residue.resname,residue.id[1])#打印残基及其序列标识
for atom in residue:
print(atom.name,atom.coord)#打印原子及其坐标

# write pdb file
io = PDBIO()
io.set_structure(structure)
io.save('my_structure.pdb')#将structure对象保存到文件