---
jupyter:
  jupytext:
    formats: ipynb,md,py
    text_representation:
      extension: .md
      format_name: markdown
      format_version: '1.2'
      jupytext_version: 1.4.1
  kernelspec:
    display_name: Python 3
    language: python
    name: python3
---

<!-- #region slideshow={"slide_type": "slide"} -->
# Lab 5 - Why have biologists still not developed an HIV vaccine?
## Hidden Markov Models
Material and embedded lab.

Motivation and some exercises are variations on those available in Bioinformatics Algorithms: An Active-Learning Approach by Phillip Compeau & Pavel Pevzner.
<!-- #endregion -->

```python slideshow={"slide_type": "skip"}
debug = True # Set this to False before pushing to be graded
```

<!-- #region slideshow={"slide_type": "slide"} -->
# Classifying the HIV Phenotype

* Today there are over 35 million people living with the disease
* 1984 - US Health and Human Services Secretary Margaret Heckler states we will have an HIV vaccine in two years
* 1997 - Bill Clinton established a new research center with the goal of developing HIV vaccine
* 2005 - Merck beins clinical trials of an HIV vaccine, but discontinued two years later because there is some evidence this actual *increased* the risk of infection
* Antiretroviral therapy is available - a drug cocktail that stabilizes the symptoms
<!-- #endregion -->

<!-- #region slideshow={"slide_type": "subslide"} -->
## Vaccines

* Classical vaccines against viruses are made from surface proteins of the virus
* HIV viral envelope proteins are extremely variable
* HIV strains taken from different patients represent diverged subtypes and therefore a vaccine must be broad enough to account for this variability
* HIV has just nine genes... I mean... come on... Why can't we do this? 
* One of my favorite thing to say is biology is complicated and this is one of the hardest things for a computer scientist who is used to 1's and 0's to internalize.
<!-- #endregion -->

<!-- #region slideshow={"slide_type": "subslide"} -->
## A biological problem becomes an algorithm problem
* Multiple sequence alignments tell us a lot about a protein
* HIV proteins are extreme cases where a change at a single position can affect the HIV phenotype (and thus the drug treatment)
    * We would need a different scoring matrix across different locations in the sequence which is not part of our original formulation of the biological problem
* Constructing a multiple sequence alignment from highly diverged sequences is difficult and especially difficult for our previous approaches
* We need a new formulation and a new algorithm!
<!-- #endregion -->

<!-- #region slideshow={"slide_type": "slide"} -->
## Gambling with Yakuza
Enter a simple game of heads or tails. A fair coin would have:
$$
Pr_F(H)=1/2
\hspace{0.5in}
Pr_F(T)=1/2
$$
A biased coin might have:
$$
Pr_F(H)=3/4
\hspace{0.5in}
Pr_F(T)=1/4
$$
<!-- #endregion -->

<!-- #region slideshow={"slide_type": "subslide"} -->
**What is the probability that you will see a sequence that consists of 4 heads and 6 tails given that you know it's a fair coin?**
<!-- #endregion -->

<!-- #region slideshow={"slide_type": "fragment"} -->
$$
Pr(\mbox{HHHHTTTTTT}|F)=(1/2)^4*(1/2)^6=(1/2)^{10}
$$
<!-- #endregion -->

<!-- #region slideshow={"slide_type": "fragment"} -->
**What is the probability that you will see a sequence that consists of 4 heads and 6 tails given that you know it's a biased coin?**
<!-- #endregion -->

<!-- #region slideshow={"slide_type": "fragment"} -->
$$
Pr(\mbox{HHHHTTTTTT}|F)=(3/4)^4*(1/4)^6
$$
<!-- #endregion -->

<!-- #region slideshow={"slide_type": "subslide"} -->
Given a sequence of heads and tails $x=x_1x_2...x_n$ with $k$ occurances of heads:
$$
Pr(x|F)=(1/2)^n
\\
Pr(x|B)=(1/4)^{n-k}*(3/4)^k=3^k/4^n
$$
<!-- #endregion -->

<!-- #region slideshow={"slide_type": "fragment"} -->
Was the dealer using a fair or biased coin?
$$
Pr(x|F)>Pr(x|B)?
$$
<!-- #endregion -->

<!-- #region slideshow={"slide_type": "subslide"} -->
You can easily compute these probabilities, so let's assume the dealer switches back and forth between the fair and biased coins with $Pr(switch)=0.1$. They do this after each flip of the coin. Now how do you determine when the dealer flipped the coin, so you can maximize your winnings?
<!-- #endregion -->

<!-- #region slideshow={"slide_type": "fragment"} -->
What about a sliding window? 
* What size sliding window?
* Can you think of any other problems?
<!-- #endregion -->

<!-- #region slideshow={"slide_type": "slide"} -->
## What does this have to do with biology? Consider finding CG-islands

We've spoken before about how not all nucleotides occur at the same frequency in the genome. For example, the human genome's GC-content is approximately 42%. This would mean that the probability of CG occuring in the human genome would be $0.21*0.21=4.41\%$

But it's approximately $1\%$!!! 

This is because methylation is the most common DNA modification that adds a methyl group to the cystosine nucleotide. The resulting methylated cytosine has a tendency to deaminate into thymine (i.e., mutate). This is bad... so this CG is the least common dinucleotide.
<!-- #endregion -->

<!-- #region slideshow={"slide_type": "subslide"} -->
## CG-islands
Methylation is often suppresed around genes in areas called CG-islands where CG appears relatelively frequently

A great biological quesiton is where are the CG-islands in the human genome?

Well... the genome is a sequence of characters similar to a sequence of coin flip results. Within that sequence we don't know if we are in a CG-island or not in a CG-island. This IS our coin flip problem with more symbols.
<!-- #endregion -->

<!-- #region slideshow={"slide_type": "subslide"} -->
<img src="https://2.bp.blogspot.com/-Lgf7NJe-MkY/TeK1zpDQ97I/AAAAAAAAADA/egoF0eM_UvQ/s1600/fairbet.png">
<!-- #endregion -->

<!-- #region slideshow={"slide_type": "subslide"} -->
<img src="https://i.imgflip.com/4052le.jpg" width=400>
<!-- #endregion -->

<!-- #region slideshow={"slide_type": "subslide"} -->
* $States$ - Hidden Markov Models have hidden states (e.g., $States=\{F,B\}$)
* $\pi$ - Path through the hidden states (e.g., $\pi = FFFBBFB$)
* $\Sigma$ - Emission symbols
* $Emission$ - emission probabilities (e.g., $Pr(H|F)=1/2$)
* $Transitions$ - transition probabilities from one hidden state to another (e.g., $Pr(F|B)=0.1$)
<!-- #endregion -->

<!-- #region slideshow={"slide_type": "subslide"} -->
**Exercise 1** Probability of a Hidden Path Problem

Input: A hidden path $\pi$ in an HMM ($\Sigma$, $States$, $Transition$, $Emission$).

Output: The probaiblity of the path, $Pr(\pi)$.
<!-- #endregion -->

```python slideshow={"slide_type": "subslide"}
def prob_path(pi,hmm):
    sigma,states,transition,emission=hmm
    prob = 1/len(states) # probability from initial state pi_0 to pi_1 (assume uniform)
    # YOUR SOLUTION HERE
    return prob
```

```python slideshow={"slide_type": "subslide"}
import pandas as pd
pi = "FFFFBBBBFBFBBB"
sigma = ["H","T"]
states = ["F","B"]
transition = pd.DataFrame([[0.9,0.1],[0.1,0.9]],index=states,columns=states)
emission = pd.DataFrame([[0.5,0.5],[0.75,0.25]],index=states,columns=sigma)
coin_hmm = (sigma,states,transition,emission) # I'm just packing these together


prob_path(pi,coin_hmm)
```

<!-- #region slideshow={"slide_type": "subslide"} -->
But what are the inputs?
<!-- #endregion -->

```python slideshow={"slide_type": "fragment"}
transition
```

```python slideshow={"slide_type": "fragment"}
emission
```

<!-- #region slideshow={"slide_type": "subslide"} -->
## Pandas refresher
While I love Pandas, I know that viewpoint isn't always shared. Let's answer the following question again:

What if I hate Pandas so much that I want to stop using it? For the most part this is totally fine. If you get your code to work, I'm happy. To get a list:
<!-- #endregion -->

```python slideshow={"slide_type": "fragment"}
#Moving from pandas to numpy to pure python
df=pd.DataFrame([[1,2],[3,4]])
arry = df.values
arry.tolist()
```

<!-- #region slideshow={"slide_type": "subslide"} -->
But we are used to dealing with things a more complicated in computer science then learning a new api, so my recommendation is to get familiar with two of the main ways to access a data frame: loc and iloc.
<!-- #endregion -->

```python slideshow={"slide_type": "fragment"}
df=pd.DataFrame([[1,2,3],[4,5,6]],index=["One","Two"],columns=["A","B","C"])
if debug:
    display(df.loc["One"])
    display(df.loc["Two","B"])
    display(df.iloc[0,:])
    display(df.iloc[1,2])
```

<!-- #region slideshow={"slide_type": "subslide"} -->
## Our CG-island HMM
<!-- #endregion -->

```python slideshow={"slide_type": "subslide"}
# Just an example at this point
sequence = """
ACTGCTGGATGGTCACCCCCAGCACTGACTGTCTGGAAGCTCCAGGCTCAGCTCTCAGTTTCCTGGAGCA
AGTGGGAGGATGAGGACAAGGAGGAACGAGGGCACTGGCCTCCCAGGAATTGTCCCTGAGCCTCCATCCT
GCTGTCCTGAAGCTGCCCCTGAACCTCCAACTTGCTGTCCCCAGAACTGTCATTGAGCCTACACCATGCT
ATCTCTAGAGCCCGGAAAGCCCAGGGCTGGACAAACCCCACCCCTCACTCCTCCTCTGGCCCCTTCTCCC
AGCCATCAACACTTTGGAACAGCCATCAAGCCCCTTTTAATCTCTAGAAAGGTGCCTCAGTAAGGCACAG
AGAGGTCACACCAGGTGGTCATGGTGCCTTACCTGTGTCCACTGGGCCCAGGCTGGCCCTTTAAGGGTAT
GAGGGCAGAACAGCTGAGAGACCACACCCCACTTCTCAGAGAGGTCAGGGATAAAGAAAAGGGACAATGG
AAGGAAGAACTTGTGGCCAGGATGCTGAGGGTAGAGGCTGCTCCCCACAGGCACTGAGCAGAGGGGTTGA
GGGGGGAGCCTCCAGCCTCCATCCAGACAGGACCTCTGACCGCTGCTAGGGGCCCCTTCTCAGGAGGTTC
AGTCTCAGACAAGGGCTCCAGAAACTTCAGTCCATTTTCCCAAAATGGACATGATGCATCTGGCGAGTCA
GGGACCTAGAATGTCCAGGACCGAGCCTTGCTGAGGACAGAAGGGAGCAACATGCCCTGGAGGTCCTCAT
GCAGCCCAGGCCTCTGGCAGTGACCAGCCAGCACCCAGGCAACTCCTTGCTGGGTCTCCAGGCCCTGATG
GTCACAAGAAAGGCCACAGGCCAGGGCTGGGATGGGCCCAGAGCTCTGTGTGTTTCCTGGGAGGGCTGAG
"""
sequence = "".join(sequence.strip().split("\n"))
```

```python slideshow={"slide_type": "skip"}
states = ["I","N"] # I: CG-island and N: not a CG-island
# Emission frequencies from the book
CG_island_freq = pd.DataFrame([
    [0.053,0.079,0.127,0.036],
    [0.037,0.058,0.058,0.041],
    [0.035,0.075,0.081,0.026],
    [0.024,0.105,0.115,0.05]
],index=["A","C","G","T"],columns=["A","C","G","T"])
not_CG_island_freq = pd.DataFrame([
    [0.087,0.058,0.084,0.061],
    [0.067,0.063,0.017,0.063],
    [0.053,0.053,0.063,0.042],
    [0.051,0.070,0.084,0.084]
],index=["A","C","G","T"],columns=["A","C","G","T"])
emission = []
e = []
for i in CG_island_freq.index:
    for j in CG_island_freq.columns:
        e.append(CG_island_freq.loc[i,j])
emission.append(e)
columns = []
e = []
for i in not_CG_island_freq.index:
    for j in not_CG_island_freq.columns:
        columns.append(i+j)
        e.append(not_CG_island_freq.loc[i,j])
emission.append(e)
emission = pd.DataFrame(emission,columns=columns,index=states)
emission
```

```python slideshow={"slide_type": "subslide"}
pi = "IIIINNNNNNNNNNNNNNNNNIIII"
sigma = emission.columns
transition = pd.DataFrame([[0.0001,1-0.0001],[1-0.1,0.1],[0.05,1-0.05]],index=["start"]+states,columns=states)
transition
```

```python slideshow={"slide_type": "subslide"}
CG_island_hmm = (sigma,states,transition,emission)
```

```python slideshow={"slide_type": "fragment"}
prob_path(pi,CG_island_hmm)
```

<!-- #region slideshow={"slide_type": "subslide"} -->
So now we have the probability of a path through the hidden states, but how do we incorporate the sequence itself?

$$
Pr(x,\pi)=???
$$
From the chain rule you get?
<!-- #endregion -->

<!-- #region slideshow={"slide_type": "fragment"} -->
$$
Pr(x,\pi)=Pr(x|\pi)*Pr(\pi)
$$
We've already implemented $Pr(\pi)$ above, so now we need to implement the probability that you emit a sequence given a known sequence of hidden states.
<!-- #endregion -->

<!-- #region slideshow={"slide_type": "subslide"} -->
$$
Pr(x,\pi)=\prod_{i=1}^n emission_{\pi_i}(x_i) * transition(\pi_{i-1}\rightarrow\pi_i)
$$
<!-- #endregion -->

<!-- #region slideshow={"slide_type": "subslide"} -->
**Exercise 2**: Probability of an Outcome Given a Hidden Path Problem

Given: A string $x$, followed by the alphabet $\Sigma$ from which $x$ was constructed, followed by a hidden path $\pi$, followed by the states $States$ and emission matrix $Emission$ of an HMM.

Return: The conditional probability Pr(x|π) that string x will be emitted by the HMM given the hidden path $\pi$.
<!-- #endregion -->

```python slideshow={"slide_type": "subslide"}
def prob_outcome_path(x,pi,hmm):
    sigma,states,transition,emission=hmm
    prob = 1/len(states) # probability from initial state pi_0 to pi_1 (assume uniform)
    # YOUR SOLUTION HERE
    return prob
```

```python slideshow={"slide_type": "subslide"}
x = "HHHHTTHTTTHHHH"
pi = "FFFFBBBBFBFBBB"


prob_outcome_path(x,pi,coin_hmm)
```

<!-- #region slideshow={"slide_type": "slide"} -->
## Onto better questions and Dynamic Programming 
So far none of this is too interesting because we need to pass to much information to our functions and the questions our functions answer aren't very interesting. 

What *IS* interesting if is we known a sequence $x$? One thing that is interesting is finding the optimal/most likely path of hidden states. This is what would help us identify CG-islands. This is called the decoding problem, and it requires dynamic programming to implement efficiently. Luckily, we are good at that :)
<!-- #endregion -->

<!-- #region slideshow={"slide_type": "subslide"} -->
**Exercise 3**: Decoding Problem

Given: A string $x$, and a defined HMM (you know... with all the same variables as before).

Return: A path that maximizes the probability Pr(x, $\pi$) over all possible paths $\pi$.

Notes: You obviously cannot just naively enumerate all possible paths and then just select the max. You must use dynamic programming.
<!-- #endregion -->

<!-- #region slideshow={"slide_type": "subslide"} -->
Some things to help. Let's say that we have solved the problem up to a certain point $i$ in the sequence. We are in one of the hidden states from the set $States$. How we know what the optimal state is at that point? We keep track of the paths costs through a graph that looks like the one on the next slide. For a good example, I've found a great image, but it switches the states to whether you are happy and sad for a slightly different HMM. The concepts are exactly the same.
<!-- #endregion -->

<!-- #region slideshow={"slide_type": "subslide"} -->
<img src="https://miro.medium.com/max/3200/1*JlPYICS3_t8QkKILT3fqgQ.jpeg" width=700>
<!-- #endregion -->

```python slideshow={"slide_type": "subslide"}
import numpy as np
from numpy import log

def decode_path(x,hmm,debug=False,use_log=False):
    sigma,states,transition,emission=hmm
    if type(x) == str:
        x = [c for c in x] # needed for pandas stuff
    path_probs = pd.DataFrame(np.zeros((len(states),len(x))),columns=x,index=states)
    previous_states = pd.DataFrame("?",columns=x,index=states)
    for i in range(path_probs.shape[0]): # Get the number of rows
        if use_log:
            path_probs.iloc[i,0] = log(transition.loc["start",path_probs.index[i]])+log(emission.loc[path_probs.index[i],x[0]])
        else:
            path_probs.iloc[i,0] = transition.loc["start",path_probs.index[i]]*emission.loc[path_probs.index[i],x[0]]
        previous_states.iloc[i,0] = path_probs.index[i]
    if debug:
        display(path_probs)
        display(previous_states)
        
    pi = None
    # YOUR SOLUTION HERE
    return pi
```

```python slideshow={"slide_type": "subslide"}
x = "HTHTHTHTHHHHHHHTTTTTT"
sigma = ["H","T"]
states = ["F","B"]
transition = pd.DataFrame([[0.5,0.5],[0.65,0.35],[0.35,0.65]],index=["start"]+states,columns=states)
display(transition)
emission = pd.DataFrame([[0.5,0.5],[0.75,0.25]],index=states,columns=sigma)

coin_hmm2 = (sigma,states,transition,emission) # transition if different because I've added a start state we need

pi = decode_path(x,coin_hmm2,debug=debug)
pi
```

<!-- #region slideshow={"slide_type": "subslide"} -->
**Exercise 4**: Likelihood problem

Given: A string $x$, followed by an HMM.

Return: The probability the $x$ was emitted by the HMM.
<!-- #endregion -->

```python slideshow={"slide_type": "subslide"}
def likelihood_x(x,hmm,debug=False):
    sigma,states,transition,emission=hmm
    if type(x) == str:
        x = [c for c in x] # needed for pandas stuff
    path_probs = pd.DataFrame(np.zeros((len(states),len(x))),columns=x,index=states)
    for i in range(path_probs.shape[0]): # Get the number of rows
        path_probs.iloc[i,0] = transition.loc["start",path_probs.index[i]]*emission.loc[path_probs.index[i],x[0]]
        
    prob = None
    # YOUR SOLUTION HERE
    return prob
```

```python slideshow={"slide_type": "subslide"}
x = "HTHTHTHTHHHHHHHTTTTTT"
prob = likelihood_x(x,coin_hmm2,debug=debug)


prob
```
<!-- #region slideshow={"slide_type": "slide"} -->
## What about our CG-islands?
Let's read a snipit and the human genome.
<!-- #endregion -->

```python slideshow={"slide_type": "subslide"}
import os.path

file = None
locations = ['../data/sample.fa','../csc-448-student/data/sample.fa']
for f in locations:
    if os.path.isfile(f):
        file = f
        break
print('Opening',file)
sequence = ("".join(open(file).read().upper().split("\n")[1:])).strip()[:10000]
print(sequence[:10],"...",sequence[-10:])
print(len(sequence))
```

<!-- #region slideshow={"slide_type": "subslide"} -->
**Exercise 5 (for fun - please comment out before submitting to the autograder)**: Find the CG-islands

Given: A string $x$, followed by an HMM.

Return: A path that maximizes the probability Pr(x, $\pi$) over all possible paths $\pi$.
<!-- #endregion -->

```python slideshow={"slide_type": "subslide"}
x = [sequence[i:i+2] for i in range(0,len(sequence)-1)]
pi_discard = decode_path(x,CG_island_hmm,debug=True,use_log=False)

pi = decode_path(x,CG_island_hmm,debug=True,use_log=True)

len(pi)
```

```python slideshow={"slide_type": "subslide"}
sections = []
for i in range(len(pi)):
    if len(sections) == 0:
        sections.append([pi[i]])
    else:
        if sections[-1][0] == pi[i]:
            sections[-1].append(pi[i])
        else:
            sections.append([pi[i]])
prettypi = " ".join(["%d%s"%(len(section),section[0]) for section in sections])
prettypi
```

<!-- #region slideshow={"slide_type": "slide"} -->
## Profile HMMs and Training
* Profile HMMs for Sequence Alignment
   * Separate HMM for each family
   * Seeded with multiple sequence alignment
   * Trained on a lot of sequences from the same family
   * We can then ask what is the family of a sequence (with unknown family) by checking it against each HMM!
* Training
   * Learning the correct transition and emission rates are not beyond our understanding, but in the interest of time I've left them out of this online version of this class. The book has a good section on this material.
<!-- #endregion -->

```python slideshow={"slide_type": "skip"}
# Don't forget to push!
```
