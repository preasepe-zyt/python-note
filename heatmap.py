import matplotlib.pyplot as plt
import numpy as np

import matplotlib
import matplotlib as mpl
import pandas as pd
path = r"C:\Users\79403\Desktop\uin\jiao1.xls"
data = pd.read_excel(path)
data = data.iloc[0:18, :]
data_col = ['gene_name', 'gene_chr', 'gene_start', 'gene_end']
data2 = data[data_col]

gene = data["gene_name"]

exe = np.array(data2[['gene_chr', 'gene_start', 'gene_end']], dtype=np.float_)


fig, ax = plt.subplots(figsize=(12, 8))
im = ax.imshow(exe, cmap='viridis', aspect='auto')

# Show all ticks and label them with the respective list entries
ax.set_xticks(np.arange(len(data_col[1:])), labels=data_col[1:])
ax.set_yticks(np.arange(len(gene)), labels=gene)

# Rotate the tick labels and set their alignment.
plt.setp(ax.get_xticklabels(), rotation=45, ha="right",
         rotation_mode="anchor")

# Loop over data dimensions and create text annotations.
for i in range(len(gene)):
    for j in range(len(data_col[1:])):
        text = ax.text(j, i, exe[i, j],
                       ha="center", va="center", color="w")

ax.set_title("heat_map")
#fig.tight_layout()
plt.show()
