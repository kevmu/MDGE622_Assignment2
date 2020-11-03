#!/usr/bin/env python

import matplotlib.pyplot as plt
from matplotlib_venn import venn2_unweighted
 
# 17304HA sample Venn Diagram.
venn = venn2_unweighted(subsets = (23, 9, 234), set_labels = ('X!Tandem Search', 'MS-GF+ Search'))
plt.title("Venn Diagram of 17304HA Sample Proteins \nfor X!Tandem and MS-GF+ Searches",fontsize=18)

for text in venn.set_labels:
    text.set_fontsize(14)
for text in venn.subset_labels:
    text.set_fontsize(16)

plt.savefig('17304HA_venn_diagram.png')
plt.clf()

# 21423HA sample Venn Diagram.
venn = venn2_unweighted(subsets = (24, 70, 66), set_labels = ('X!Tandem Search', 'MS-GF+ Search'))
plt.title("Venn Diagram of 21423HA Sample Proteins \nfor X!Tandem and MS-GF+ Searches",fontsize=18)

for text in venn.set_labels:
    text.set_fontsize(14)
for text in venn.subset_labels:
    text.set_fontsize(16)

plt.savefig('21423HA_venn_diagram.png')
plt.clf()
