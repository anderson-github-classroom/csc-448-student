# ---
# jupyter:
#   jupytext:
#     formats: ipynb,md,py
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.4.1
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

# + [markdown] slideshow={"slide_type": "slide"}
# # Lab 2 - Which animal gave us SARS?
# ## Secondary Title: Evolutionary Tree Construction
# Material and embedded lab.
#
# Motivation and some exercises are variations on those available in Bioinformatics Algorithms: An Active-Learning Approach by Phillip Compeau & Pavel Pevzner.

# + slideshow={"slide_type": "skip"}

# + [markdown] slideshow={"slide_type": "slide"}
# # Fastest Outbreak?

# + [markdown] slideshow={"slide_type": "subslide"}
# ## SARS crosses Pacific Ocean within a week
# * Feb 21, 2003 - Chinese doctor Liu Jianlu flys to Hong Kong to attend a wedding
# * Two weeks later Dr. Liu Jianlu dies but tells doctors that he recently treated sick patients in Guangdong Province
# * Feb 23, 2003 - Man staying across the hall from Liu Jianlu travels to Hanoi and dies after infecting 80 people
# * Feb 26, 2003 - Woman traveled home to Toronto bringing the disease and initiating an outbreak there.
#
# * It took 5 years for the Black Death to travel from Constantinople to Kiev
# * It took HIV two decades to circle the global

# + [markdown] slideshow={"slide_type": "subslide"}
# ## Reaction
# The reaction was immense with Chinese officials threatening to execute infected patients who violated quarantine.
#
# If international travel spread the disease then international collaboration would contain it.
#
# Within weeks bioligists identified a virus that caused the epdemic and sequences the genome. The new disease earned the name Severe Acute Respiratory Syndrome or SARS

# + [markdown] slideshow={"slide_type": "subslide"}
# ## Evolution of SARS
# * SARS belongs to a family of viruses called conoraviruses (named after latin word *corona* meaning crown)
# * Before SARS the coronaviruses were thought to only cause minor problems like the common cold
#
# <table>
#     <tr>
#         <td>
#             <img src="http://bioinformaticsalgorithms.com/images/Evolution/coronavirus.png" width=200>
#         </td>
#         <td>
#             <img src="http://bioinformaticsalgorithms.com/images/Evolution/eclipse.png" width=200>
#         </td>
#     </tr>
#     </table>

# + [markdown] slideshow={"slide_type": "subslide"}
# ## Sequencing
# * By fall 2003, researchers sequenced many strains from patients in various contries
# * OK ... so what is sequencing...
# <center>
# <img src="https://www.genengnews.com/wp-content/uploads/2018/10/Aug23_GEN_Baker_NGSChallenges_GettyImages537618080_ktsimage_DNATestSangerSeq2004017011.jpg" width=400>
# </center>
# * We will eventually get back to assembly in bioinformatics, so we'll talk more about sequencing then. But for now, check out this video: https://www.youtube.com/watch?v=jFCD8Q6qSTM

# + [markdown] slideshow={"slide_type": "subslide"}
# ## Questions
# * How did SARS-CoV cross the species barrier to humans? 
# * When and where did it happen? How did SARS spread around the world, and who infected whom?
#
# Each of these questions about SARS is ultimately related to the problem of constructing evolutionary trees (also known as phylogenies). Here is an evolutionary tree for HIV, but what algorithms do we use for this?
#
# <img src="http://bioinformaticsalgorithms.com/images/Evolution/HIV_phylogeny.png" width=200>

# + [markdown] slideshow={"slide_type": "slide"}
# # Distance Matrices to Evolutionary Trees
# * Scientists started sequencing cornonavirus from various species to determine which is most similar to SARS
# * Comparing (multiple alignment) of entire viral genomes is tricky because viral genes are often rearranged, inserted, and deleted
# * Scientists focused on one of six genes in SARS-CoV
# * Gene that encodes Spike protein
#     * Identifies and binds to receptor site on host's cell membrane
#     * Spike protein is 1,255 amino acids long and rather weak similarity with Spike proteins in other coronaviruses
#     * Even subltle similarities turned out to be ssufficient for constructing a multiple alignment (comparison) across coronaviruses

# + [markdown] slideshow={"slide_type": "subslide"}
# ## Amino acids
# <img src="https://www.nature.com/scitable/content/ne0000/ne0000/ne0000/ne0000/7447898/EssGen1-5_Codons-to-AA-V2.jpg">

# + [markdown] slideshow={"slide_type": "subslide"}
# ## Amino acids continued
#
# <img src="https://www.nature.com/scitable/content/ne0000/ne0000/ne0000/ne0000/118090962/amino-acid-table.jpg">

# + [markdown] slideshow={"slide_type": "subslide"}
# ## Amino acids continued
# <img src="https://ib.bioninja.com.au/_Media/amino-acid-structures_med.jpeg" width=500>

# + [markdown] slideshow={"slide_type": "subslide"}
# ## Distance matrix
# Consider the DNA sequences shown below for 4 different species. 
# <img src="http://bioinformaticsalgorithms.com/images/Evolution/mammal_alignment_distance_matrix.png" width=400>
# The above example defined a distance matrix of +1 for every mismatched position. In general, $D$ must satisfy three properties. It must be symmetric (for all $i$ and $j$, $D_{i,j}$ = $D_{j,i}$), non-negative (for all $i$ and $j$, $D_{i,j}$ $\ge$ 0) and satisfy the triangle inequality (for all $i$, $j$, and $k$, $D_{i,j} + D_{j,k} \ge D_{i,k}$ ).

# + [markdown] slideshow={"slide_type": "subslide"}
# <img src="http://bioinformaticsalgorithms.com/images/Evolution/tree_of_life.png" width=400>

# + [markdown] slideshow={"slide_type": "subslide"}
# ## Rooted trees
# <img src="http://bioinformaticsalgorithms.com/images/Evolution/rooted_tree_time.png" width=400>

# + [markdown] slideshow={"slide_type": "subslide"}
# ## What are we aiming for?
# We say that a weighted unooted tree $T$ fits a distance matrix $D$ if $d_{i,j}=D_{i,j}$ for every pair of leaves $i$ and $j$. Example:
#
# <img src="http://bioinformaticsalgorithms.com/images/Evolution/additive_distance_matrix.png" width=300>
#
# <img src="http://bioinformaticsalgorithms.com/images/Evolution/simple_tree_fitting_additive_matrix.png" width=300>

# + [markdown] slideshow={"slide_type": "subslide"}
# ### Technical Detour: networkx
# ``networkx`` is a very useful Python package. It provides a great visualization for many different applications. While there are phylogentic libraries we will use later, for our project.

# + slideshow={"slide_type": "subslide"}
# %matplotlib inline 

import networkx as nx

G = nx.Graph()

G.add_edge('v1', 'v5', weight=11)
G.add_edge('v2', 'v5', weight=2)
G.add_edge('v5', 'v6', weight=4)
G.add_edge('v6', 'v3', weight=6)
G.add_edge('v6', 'v4', weight=7)

# + slideshow={"slide_type": "subslide"}
import copy
import pandas as pd

def show(T):
    T = copy.deepcopy(T)
    labels = nx.get_edge_attributes(T,'weight')
    max_value = 0
    for n1,n2 in T.edges():
        if T[n1][n2]['weight'] > max_value:
            max_value = T[n1][n2]['weight']
    for n1,n2 in T.edges():
        T[n1][n2]['weight']=max_value - T[n1][n2]['weight'] + 3
    pos=nx.spring_layout(T)
    nx.draw(T,pos,with_labels=True)
    nx.draw_networkx_edge_labels(T,pos,edge_labels=labels);
    
def show_adj(T):
    return pd.DataFrame(nx.adjacency_matrix(T).todense(),index=T.nodes(),columns=T.nodes())


# + slideshow={"slide_type": "subslide"}
show(G)

# + slideshow={"slide_type": "subslide"}
show_adj(G)

# + [markdown] slideshow={"slide_type": "subslide"}
# ## Pandas and numpy
# Throughout this course, I will use numpy and Pandas when I find their use worth the complexity of you learning another library. Fortunately, there are some really simple Pandas and numpy features that we can easily discuss. For this lab, our primary use will be the use of a pandas dataframe. If we didn't use pandas, and we wanted to access a 2-dimensional array, then we would have to do the following:

# + slideshow={"slide_type": "fragment"}
D = [[0,13,21,22],[13,0,12,13],[21,12,0,13],[22,13,13,0]]
D

# + [markdown] slideshow={"slide_type": "subslide"}
# This isn't bad, but it gets clunky. 
# * We don't have any names associated with the columns or rows.
# * We don't have an easy way to access a specific column.
# * And much more...

# + slideshow={"slide_type": "fragment"}
import pandas as pd
names = ["v1","v2","v3","v4"]
D = pd.DataFrame([[0,13,21,22],[13,0,12,13],[21,12,0,13],[22,13,13,0]],index=names,columns=names)
D

# + [markdown] slideshow={"slide_type": "subslide"}
# **Accessing an element by row and column name**

# + slideshow={"slide_type": "fragment"}
D.loc["v2","v3"] # Pretty cool right?

# + slideshow={"slide_type": "fragment"}
D.iloc[1,2] # You can always go back to regular indices

# + slideshow={"slide_type": "fragment"}
D.columns # You can easily get the column names

# + slideshow={"slide_type": "fragment"}
D.index # You can easily get the row names

# + [markdown] slideshow={"slide_type": "subslide"}
# ## Neighboring leaves
# <center>
# ${\color{red}{d_{k,m}}} = \dfrac{({\color{purple}{d_{i,m}}} + {\color{red}{d_{k,m}}}) + ({\color{blue}{d_{j,m}}} + {\color{red}{d_{k,m}}}) - ({\color{purple}{d_{i,m}}} + {\color{blue}{d_{j,m}}})}{2} = \dfrac{d_{i,k} +d_{j,k} - d_{i,j}}{2}$
#
# <img src="http://bioinformaticsalgorithms.com/images/Evolution/neighboring_leaves_equality.png" width=500>
# </center>

# + [markdown] slideshow={"slide_type": "subslide"}
# **Exercise 1** Compute the distances between leaves in a weighted tree
#
# Input: A weighted tree defined by the package networkx
#
# Output: $n \times n$ matrix ($d_{i,j}$), where $d_{i,j}$ is the length of the path between leaves $i$ and $j$.
#
# Learning objectives:
# 1. Refresh memory of graph traversal (path finding)
# 2. Understand the difference between $d_{i,j}$ and $D_{i,j}$.
# 3. Gain exposure and work with networkx python package.

# + slideshow={"slide_type": "subslide"}
import pandas as pd

def compute_d(G):
    d = {}
    for nodei in G.nodes():
        for nodej in G.nodes():
            d[nodei,nodej] = 0
    # Fill in all adjacent values
    for nodei,nodej,data in G.edges(data=True):
        d[nodei,nodej] = data['weight']
        d[nodej,nodei] = d[nodei,nodej]
    for nodei in G.nodes():
        for nodej in G.nodes():
            if d[nodei,nodej] == 0 and nodei != nodej:
                dij = 0
                ## YOUR SOLUTION HERE
                # networkx has a function to compute simple paths. You can uncomment out the line
                # below in order to see this function working. I'll be reviewing your solutions though
                # and if you don't write this from scratch, then I will consider this an attempt to
                # circumvent the autograder
                #path = list(nx.all_simple_paths(G,nodei,nodej))[0] # get the first simple path
                a = path[0]
                for b in path[1:]:
                    dij += d[a,b]
                    a = b
                d[nodei,nodej] = dij
                d[nodej,nodei] = dij
    d = pd.DataFrame(d.values(),index=d.keys(),columns=['d']).unstack()
    d.columns = [n for l,n in d.columns]
    return d

compute_d(G)

# + [markdown] slideshow={"slide_type": "subslide"}
# ## What if you need to find the graph?
# <img src="http://bioinformaticsalgorithms.com/images/Evolution/additive_phylogeny.png" width=450>

# + [markdown] slideshow={"slide_type": "subslide"}
# **Exercise 2** Implement limb length algorightm described in Chapter 7.
#
# Input: An addititve distance matrix $D$ and a node $j$
#
# Output: The length of the limb connect leaf $j$ to its parent in $Tree(D)$.
#
# Learning outcomes:
# 1. Understanding why this function is needed when we just computed the paths weights previously.
# 2. Understanding the Limb Length Theorem in Chapter 7.

# + slideshow={"slide_type": "subslide"}
import pandas as pd
import numpy as np

def limb(D,j):
    min_length = np.Inf
    nodes = D.drop(j).index
    for ix,i in enumerate(nodes):
        for kx in range(ix+1,len(nodes)):
            k = nodes[kx]
    return min_length

names = ["v1","v2","v3","v4"]
D = pd.DataFrame([[0,13,21,22],[13,0,12,13],[21,12,0,13],[22,13,13,0]],index=names,columns=names)
print(D)
limb(D,"v4")


# + [markdown] slideshow={"slide_type": "subslide"}
# ## Building up additive phylogeny
# One piece at a time...
#
# Learning outcomes:
# 1. Using recursion and by extension debugging recursion
# 2. Understand additive versus non-additive $D$
# 3. Constructing our first evolutionary tree

# + [markdown] slideshow={"slide_type": "subslide"}
# **Exercise 3a** Implement a portion of ``AdditivePhylogeny`` algorithm from Chapter 7.
#
# Input: Distance matrix $D$ and node name $n$.
#
# Output: Return the node names $i,k$ that satisfy $D_{i,k} = D_{i,n} + D_{n,k}$.

# + slideshow={"slide_type": "skip"}
Dorig = copy.copy(D)


# + slideshow={"slide_type": "subslide"}
def find(D,n):
    nodes = D.drop(n).index
    for ix,i in enumerate(nodes):
        for kx in range(ix+1,len(nodes)):

D = copy.copy(Dorig)
print(D)
limbLength = limb(D,D.index[-1]) # our algorithm will choose the last node
n = D.index[-1]
Dtrimmed = D.drop(n).drop(n,axis=1)
for j in Dtrimmed.index:
    D.loc[j,n] = D.loc[j,n] - limbLength
    D.loc[n,j] = D.loc[j,n]
find(D,"v4")


# -

# **Exercise 3b** Implement a portion of ``AdditivePhylogeny`` algorithm from Chapter 7.
#
# Input: Distance matrix $D$ of size $2 \times 2$.
#
# Output: Return a networkx graph with the correct weight.

# +
def base_case(D):
    T = nx.Graph()
    ## YOUR SOLUTION HERE
    return T

base_G = base_case(D.iloc[:2,:].iloc[:,:2])
show(base_G)


# + slideshow={"slide_type": "subslide"}
def additive_phylogeny(D,new_number):
    D = D.copy()
    if len(D) == 2:
        return base_case(D) # Implemented correctly above
    n = D.index[-1]
    limbLength = limb(D,n) # our algorithm will choose the last node
    Dtrimmed = D.drop(n).drop(n,axis=1)
    for j in Dtrimmed.index:
        D.loc[j,n] = D.loc[j,n] - limbLength
        D.loc[n,j] = D.loc[j,n]

    Dtrimmed = D.drop(n).drop(n,axis=1)
    T = additive_phylogeny(Dtrimmed,new_number+1)

    i,k = find(D,n) # Implemented correctly above
    #if D.loc[j,n] < D.loc[i,n]:
    #    i,k = k,i
    v = "v%s"%new_number
    ## Your solution here
    # This is definitely the most complicated thing conceptually
    # You'll need to add edges and remove edges (T.add_edge and T.remove_edge)
    return T

D = copy.copy(Dorig)
G2 = additive_phylogeny(D,len(D)+1)
show(G2)

# + [markdown] slideshow={"slide_type": "subslide"}
# **Exercise 4 (extra credit)** Run your new algorithm on SARS data derived from multiple alignment of Spike proteins.
#
# This will show up on the grader as incorrect, but I will make it extra credit when moving the grades into Canvas.

# + slideshow={"slide_type": "subslide"}
D_sars = pd.read_csv('../data/coronavirus_distance_matrix_additive.txt',index_col=0)
D_sars

# + slideshow={"slide_type": "subslide"}
from pylab import rcParams
rcParams['figure.figsize'] = 10, 5

G3 = additive_phylogeny(D_sars,len(D_sars)+1)
show(G3)

# + slideshow={"slide_type": "skip"}
show_adj(G3)


# + [markdown] slideshow={"slide_type": "skip"}
# **Helper function to check things out**

# + slideshow={"slide_type": "skip"}
def compute_path_cost(T,i,k):
    cost = 0
    path = list(nx.all_simple_paths(T,i,k))[0]
    a = path[0]
    cost = 0
    A = show_adj(G3)
    for b in path[1:]:
        cost += A.loc[a,b]
        a = b
    return cost


# + slideshow={"slide_type": "skip"}
compute_path_cost(G3,'Human','Turkey')

# + slideshow={"slide_type": "fragment"}
compute_path_cost(G3,'Human','Turkey') == D_sars.loc['Human','Turkey']

# + slideshow={"slide_type": "skip"}
# Don't forget to push!
# -


