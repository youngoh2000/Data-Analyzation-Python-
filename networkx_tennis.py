
# coding: utf-8

# ## Description
# 
# This scripts illustrates basic properties of [NetworkX](https://networkx.github.io "NetworkX").  NetworkX a Python language software package for the creation, manipulation, and study of the structure, dynamics, and functions of complex networks.
# 
# The script below reads network data from the file 'grandslams.txt', constructs a directed graph, and visualizes it.

# In[2]:

##to remove warning messages
import warnings
warnings.filterwarnings('ignore')
################################

import networkx as nx
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


G=nx.DiGraph()



filename = 'grandslams.txt'
tourn_id = '580'
round_nr = 3


with open(filename) as f:
    content = f.readlines()
    for row in content:
        if row and not "#" in row:
            if row.split('|||')[0] == tourn_id and int(row.split('|||')[2]) > round_nr:
                winner = row.split('|||')[3].split(';')[1].rstrip()
                loser = row.split('|||')[4].split(';')[1].rstrip()
                
                G.add_edge(loser, winner)
                print (loser, '--->', winner, '\n')




                
##create figure object
plt.figure(figsize=(10,10));


##draw the graph
#pos=nx.graphviz_layout(G,prog='dot')

pos=nx.spring_layout(G)
nx.draw(G, pos)
nx.draw_networkx_labels(G, pos)


##show the figure
plt.show()
#plt.savefig('tennis.pdf')


# In[ ]:



