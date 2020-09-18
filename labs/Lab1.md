---
jupyter:
  jupytext:
    formats: ipynb,md,py
    text_representation:
      extension: .md
      format_name: markdown
      format_version: '1.2'
      jupytext_version: 1.6.0
  kernelspec:
    display_name: Python 3
    language: python
    name: python3
---

<!-- #region slideshow={"slide_type": "slide"} hideCode=false hidePrompt=false -->
# Week 1 and Lab 1 - Where in the Genome Does DNA Replication Begin?
## Secondary Title: Algorithm Warmup
Material and embedded lab.

Motivation and some exercises are variations on those available in Bioinformatics Algorithms: An Active-Learning Approach by Phillip Compeau & Pavel Pevzner.
<!-- #endregion -->

<!-- #region slideshow={"slide_type": "subslide"} hideCode=false hidePrompt=false -->
## Announcements and plans today
I haven't been able to turn hide_code plugin on for all. I've found some instructions, but they haven't worked for us yet. Oh well. You can turn it on yourself using the following commands at the terminal in JupyterHub.
<pre>
jupyter nbextension enable --py hide_code
jupyter serverextension enable --py hide_code
</pre>

Video posting update

Project update - if you haven't filled out the survey yet, please do so. You can always change your answers
<!-- #endregion -->

<!-- #region slideshow={"slide_type": "subslide"} -->
Learning objectives for the week and lab:
1. Build our mental model of biology (two ways)
2. Warm up our algorithm abilities after summer break
3. Gain experience translating a biological problem into a problem we can solve via code
<!-- #endregion -->

<!-- #region slideshow={"slide_type": "subslide"} hideCode=false hidePrompt=false -->
### Our set list for the week
1. Molecular biology primer (Dr. A)
2. Activity 1 (10-15 min in group and then report back out - you can ask for more time if you are on to something)
3. Molecular biology primer (Dr. Davidson - https://calpoly.zoom.us/rec/share/S7ECHKvkz73q1NKzypxJYOnK6Vyy_dyuDyxV4rnCwgZm-T6pe84YZ-c7enWYPmkc.6vf7SLpmaS8-pLWg?startTime=1600383975000)
4. Methods for finding origin of replication
<!-- #endregion -->

<!-- #region slideshow={"slide_type": "slide"} hideCode=false hidePrompt=false -->
## Molecular biology for bioinformatics
Short introduction into some of the concepts we must familiarize ourselves with in this class. We will add to our biological knowledge a little bit at a time.

Credit for some of this content comes from: http://web.stanford.edu/class/cs173/papers/primer.pdf

<img src="https://www.thoughtco.com/thmb/pTDTZI1GH12gJr-DEyozAcVOGvA=/1500x1039/filters:fill(auto,1)/genes-DNA-573388755f9b58723d5eb4fd.jpg" width=800>
<!-- #endregion -->

<!-- #region slideshow={"slide_type": "subslide"} hideCode=false hidePrompt=false -->
### Goals of Molecular Biology
* Sequencing and comparing full genomes of organisms.
* Identifying the genes and determining the foundations of the proteins they encode.
* Understanding gene expression.
* Understanding genetic diseases.
* Understanding evolution and evolutionary history.
* Understanding proteins, which means predicting the folding of the amino acid
sequence, and characterizing the function of the protein based on this folding.
* Constructing synthetic proteins, which means creating amino acid sequences,
such that the protein produced from these have a desired function.
<!-- #endregion -->

<!-- #region slideshow={"slide_type": "subslide"} hideCode=false hidePrompt=false -->
### Polymers
Three types of polymers will play a roll in this class and in biology: DNA, RNA, and proteins

DNA sequences are the information-containing molecules and are composed of
nucleotides from an alphabet of four letters: A, C, G and T. The DNA of an organism plays a central role in its existence. It is arranged in
the form of chromosomes. These strings may be millions of nucleotides long,
measured in base pairs (bp).

The entire set of genetic information of an organism is called its genome. Genome sizes vary for different species.

<img src="https://ib.bioninja.com.au/_Media/genome-size-table_med.jpeg" widt=300>
<!-- #endregion -->

<!-- #region slideshow={"slide_type": "subslide"} hideCode=false hidePrompt=false -->
Proteins, which are the operational molecules, are composed of chains of amino
acids, called polypeptides, each from an alphabet of 20 letters:
    
<img src="https://qph.fs.quoracdn.net/main-qimg-aaa1523b121f7374bb1bdc294d0107ba">
<!-- #endregion -->

<!-- #region slideshow={"slide_type": "subslide"} hideCode=false hidePrompt=false -->
RNA sequences, which stand between DNA and protein, are composed of nucleotides from an alphabet of four letters: A, C, G, U.

The Central Dogma of Molecular Biology describes the interaction of these polymers:
- DNA acts as a template to replicate itself;
- DNA is also transcribed into RNA; and
- RNA is translated into protein.
<!-- #endregion -->

<!-- #region slideshow={"slide_type": "subslide"} hideCode=false hidePrompt=false -->
<img src="https://ib.bioninja.com.au/_Media/central-dogma_med.jpeg">
<!-- #endregion -->

<!-- #region slideshow={"slide_type": "subslide"} hideCode=false hidePrompt=false -->
1. Replication of DNA.
Each strand in a DNA is a chemical ”mirror image” of the other. If there is
an a on one strand, there will always be a t in the same position on the other
strand, and vice versa; if there is a c on the one strand, its ”partner” on the
other strand will always be a g, and vice versa.
When a cell divides to form daughter cells, DNA is replicated by untwisting the
two strands and using each strand as a template to produce its chemical mirror
image.
2. Transcription of DNA.
DNA also act as a blueprint for RNA, more exactly three main types of RNA:
messenger RNA (mRNA), transfer RNA (tRNA), and ribosomal RNA (rRNA).
They carry information from the genome to the ribosomes, the protein synthesis
apparatus in a cell.
3. Translation of mRNA.
The information in an mRNA will be translated into a sequence of amino acids,
creating a polypeptide molecule.3
<!-- #endregion -->

<!-- #region slideshow={"slide_type": "subslide"} hideCode=false hidePrompt=false -->
#### More on proteins

"Organic chemistry is the chemistry of carbon compounds. Biochemistry is the study of carbon compounds that crawl." - Mike Adam

Example, human insulin is composed by two words (chains of amino acids):

A: gly ile val glu gln cys cys thr ser ile cys ser leu tyr glu leu glu asn tyr cys asn.

B: phe val asn gln his leu cys gly ser his leu val glu ala leu tyr leu val cys gly glu arg
gly phe phe tyr thr pro lys thr.

The function of a protein is a direct consequence of its three-dimensional structure
<!-- #endregion -->

<!-- #region slideshow={"slide_type": "subslide"} hideCode=false hidePrompt=false -->
### More on genes
Historically, the heritable factors which determine much of the physical make up of
organisms are called genes.

Usually there are several different forms one gene can have. These forms are called
alleles.

A combination of alleles describes the make-up of an individual, more exactly:
* The genetic make-up of an individual is its genotype.
* The expression of the genes of an individual is its phenotype.
<!-- #endregion -->

<!-- #region slideshow={"slide_type": "subslide"} hideCode=false hidePrompt=false -->
### In class exercise
In your breakout groups, produce a Google Doc that contains and answers the following. You can use Google. You can put down partial answers. Nothing will be graded for correctness. Each group needs to have one student report out what they found and issues they encountered and questions they had, etc. 
1. Find as many different pictures of human insulin protein
2. Why are there different pictures?
3. Now find the gene sequence of insulin
<!-- #endregion -->

<!-- #region slideshow={"slide_type": "subslide"} hideCode=false hidePrompt=false -->
## Bio and chapter primer from a biologist
Dr. Davidson - https://calpoly.zoom.us/rec/share/S7ECHKvkz73q1NKzypxJYOnK6Vyy_dyuDyxV4rnCwgZm-T6pe84YZ-c7enWYPmkc.6vf7SLpmaS8-pLWg?startTime=1600383975000

Complete the following survey as a group after watching the video: https://forms.gle/8P1KxgEoD6r9hBmb8
<!-- #endregion -->

<!-- #region slideshow={"slide_type": "slide"} hideCode=false hidePrompt=false -->
## Genome Replication
* One of most important tasks carried out in the cell. 
* Must be carried out before cell division
* In 1953, James Watson and Francis Crick ended their paper on DNA double helix with:

"It has not escaped our notice that the specific pairing we have postulated immediately suggests a possible copying mechanism for the genetic material."

<img src="https://images.fineartamerica.com/images/artworkimages/mediumlarge/1/watson-and-crick-a-barrington-brown-and-photo-researchers.jpg" alt="drawing" width="400"/>
<!-- #endregion -->

<!-- #region slideshow={"slide_type": "subslide"} hideCode=false hidePrompt=false -->
## Let's talk some biology
<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/3/37/Difference_DNA_RNA-EN.svg/1200px-Difference_DNA_RNA-EN.svg.png" width="600"/>


<!-- #endregion -->

<!-- #region slideshow={"slide_type": "subslide"} hideCode=false hidePrompt=false -->
## DNA and RNA code
* Not a binary alphabet
* DNA alphabet: AGCT
* RNA alphabet: AGCU
* Nucleotides are complementary (A binds to T and G binds to C)
* Replication begins at replication origin (*ori*)
* **Binary is a base-2 system, what is DNA/RNA?**
<!-- #endregion -->

<!-- #region slideshow={"slide_type": "subslide"} hideCode=false hidePrompt=false -->
## Why should I care?
There are molecular copy machines known as DNA polymerases that start by locating a *ori*. Some gene therapy methods use genetically engineered mini-genomes, which are called **viral vectors** because they are able to penetrate cell walls. Viral vectors carry artificial genes that have been used to engineer frost-resistant tomatoes and pesticide-resistant corn. In 1990, gene therapy was successfully performed on humans when it saved the life of a four year old girl suffered from Severe Combined Immunodeficiency Disorder. To ensure the treatment works, scientists must know the location of *ori* and avoid disrupting this site.
<!-- #endregion -->

<!-- #region slideshow={"slide_type": "subslide"} hideCode=false hidePrompt=false -->
## Looking for *ori*
Verified *ori* of Vibrio cholerae, the bacterium that causes cholera (~500 nucleotides):
<pre>
atcaatgatcaacgtaagcttctaagcatgatcaaggtgctcacacagtttatccacaac
ctgagtggatgacatcaagataggtcgttgtatctccttcctctcgtactctcatgacca
cggaaagatgatcaagagaggatgatttcttggccatatcgcaatgaatacttgtgactt
gtgcttccaattgacatcttcagcgccatattgcgctggccaaggtgacggagcgggatt
acgaaagcatgatcatggctgttgttctgtttatcttgttttgactgagacttgttagga
tagacggtttttcatcactgactagccaaagccttactctgcctgacatcgaccgtaaat
tgataatgaatttacatgcttccgcgacgatttacctcttgatcatcgatccgattgaag
atcttcaattgttaattctcttgcctcgactcatagccatgatgagctcttgatcatgtt
tccttaaccctctattttttacggaagaatgatcaagctgctgctcttgatcatcgtttc
</pre>
<!-- #endregion -->

<!-- #region slideshow={"slide_type": "subslide"} hideCode=false hidePrompt=false -->
## DnaA box
* There is a hidden message in *ori* that orders the cell to begin replication here.
* We know that the initiation of replication is mediated by a protein called **DnaA** that looks for a short segment within *ori*.
* This short segment is known as a *DnaA box*
* Biologists want to find this hidden message, but is that clearly defined enough for us CS/STAT/MATH/EGR folks?
<!-- #endregion -->

<!-- #region slideshow={"slide_type": "subslide"} hideCode=false hidePrompt=false -->
## Counting words
* Turns out that the patterns in our DNA are not random. 
* Some patterns are more common than others. 
* Biologically speaking this helps because certain protins can only bind to DNA if a specific string of nucleotides is present and if that string is more prevelant then we have a greater chance of success (and less likely a mutation will cause problems). 
* We are going to refer to a *k*-mer as a string of length *k*.
<!-- #endregion -->

<!-- #region slideshow={"slide_type": "subslide"} hideCode=false hidePrompt=false -->
### Why? Why? Why?
"Nothing in biology makes sense except in the light of evolution." - Theodosius Dobzhansky
<!-- #endregion -->

<!-- #region slideshow={"slide_type": "subslide"} hideCode=false hidePrompt=false -->
We are looking for surprisingly frequent substrings (contiguous strings appearing within) this *ori*.
<pre>
atcaatgatcaacgtaagcttctaagcatgatcaaggtgctcacacagtttatccacaac
ctgagtggatgacatcaagataggtcgttgtatctccttcctctcgtactctcatgacca
cggaaagatgatcaagagaggatgatttcttggccatatcgcaatgaatacttgtgactt
gtgcttccaattgacatcttcagcgccatattgcgctggccaaggtgacggagcgggatt
acgaaagcatgatcatggctgttgttctgtttatcttgttttgactgagacttgttagga
tagacggtttttcatcactgactagccaaagccttactctgcctgacatcgaccgtaaat
tgataatgaatttacatgcttccgcgacgatttacctcttgatcatcgatccgattgaag
atcttcaattgttaattctcttgcctcgactcatagccatgatgagctcttgatcatgtt
tccttaaccctctattttttacggaagaatgatcaagctgctgctcttgatcatcgtttc
</pre>
Are there any substrings that occur more frequent than others?

Before we go about searching for unknown substrings, we'll write a function that counts the number of occurances of a specific substring.
<!-- #endregion -->

```python slideshow={"slide_type": "skip"} hideCode=false hidePrompt=false
#########################
# DO NOT EDIT
#########################

import os
if os.path.isdir('../src/'):
    src_dir = '../src/'
elif os.path.isdir('../csc-448-student/'):
    src_dir = '../csc-448-student/src/'
    
exec(open('%s/header.py'%src_dir).read()) # instructor repo
# Do not forget to push your solutions.
```

<!-- #region slideshow={"slide_type": "subslide"} hideCode=false hidePrompt=false -->
**Exercise 1.**
A *k*-mer is a string of length ``k``. For this exercise, define a function ``count(text, pattern)`` as the number of times that a k-mer ``pattern`` appears as a substring of ``text``. For example,

For example:
<pre>
count("ACAACTATGCATACTATCGGGAACTATCCT","ACTAT")=3.
</pre>
Please note that count("CGATATATCCATAG", "ATA") is equal to 3 (not 2) since we should account for overlapping occurrences of ``pattern`` in ``text``.
<!-- #endregion -->

```python slideshow={"slide_type": "fragment"} hideCode=false hidePrompt=false
def count(text,pattern):
    count = 0
    # YOUR SOLUTION HERE
    return count
```

```python slideshow={"slide_type": "skip"} hideCode=false hidePrompt=false
count("ACAACTATGCATACTATCGGGAACTATCCT","ACTAT")
```

<!-- #region slideshow={"slide_type": "subslide"} hideCode=false hidePrompt=false -->
### A word about embedded lab questions
In general, I will skip over most lab questions when recording and presenting unless I want them to be used as part of the lecture/discussion.
<!-- #endregion -->

<!-- #region slideshow={"slide_type": "subslide"} hideCode=false hidePrompt=false -->
**Exercise 2.** Find the most frequent *k*-mers in a string.
* Input: A string ``text`` and an integer ``k``.
* Output: All most frequent *k*-mers in ``text`` and their count.
* Requirements: Do not use a dictionary/map
<!-- #endregion -->

```python slideshow={"slide_type": "subslide"} hideCode=false hidePrompt=false
import numpy as np

def frequent_words(text,k):
    frequent_patterns = []
    counts = []
    # YOUR SOLUTION HERE
    return list(np.unique(frequent_patterns)),max_count
```

```python slideshow={"slide_type": "skip"} hideCode=false hidePrompt=false
print(frequent_words("ACAACTATGCATACTATCGGGAACTATCCT",5))
print(frequent_words("ACAACTATGCATACTATCGGGAACTATCCT",4))
```

```python slideshow={"slide_type": "subslide"} hideCode=false hidePrompt=false
try:
    print('Question 1: What is the Big-O of frequent words? Define |text| as the length of text. Assume the unit of measurement is comparing a single charater (i.e., comparing ABC to DEF costs 3 units).')
    manual_answers["question_1"] = widgets.RadioButtons(
                options=[
                    '|text|^2',
                    '|text|^2*k',
                    'k^2'
                ],
                layout={'width': 'max-content'},
                value = None
            )

    display(widgets.Box(
        [
            widgets.Label(value='Answers:'),
            manual_answers["question_1"]
        ]
    ))
except:
    pass
```

<!-- #region slideshow={"slide_type": "subslide"} hideCode=false hidePrompt=false -->
### Now let's look at the *ori* and see what 9-mers appear
<!-- #endregion -->

```python slideshow={"slide_type": "fragment"} hideCode=false hidePrompt=false
text = "atcaatgatcaacgtaagcttctaagcatgatcaaggtgctcacacagtttatccacaacctgagtggatgacatcaagataggtcgttgtatctccttcctctcgtactctcatgaccacggaaagatgatcaagagaggatgatttcttggccatatcgcaatgaatacttgtgacttgtgcttccaattgacatcttcagcgccatattgcgctggccaaggtgacggagcgggattacgaaagcatgatcatggctgttgttctgtttatcttgttttgactgagacttgttaggatagacggtttttcatcactgactagccaaagccttactctgcctgacatcgaccgtaaattgataatgaatttacatgcttccgcgacgatttacctcttgatcatcgatccgattgaagatcttcaattgttaattctcttgcctcgactcatagccatgatgagctcttgatcatgtttccttaaccctctattttttacggaagaatgatcaagctgctgctcttgatcatcgtttc"
frequent_words(text,9)
```

<!-- #region slideshow={"slide_type": "fragment"} hideCode=false hidePrompt=false -->
Notice anything interesting about the sequences?
<!-- #endregion -->

<!-- #region slideshow={"slide_type": "subslide"} hideCode=false hidePrompt=false -->
As previously stated, nucleotides only bind to their complement, so A and T bind and G and C bind. It is also true that DNA is read in specific direction. Very much in the same way we read left to right. DNA is read from what is called the 5' end to the 3' end.

<img src="https://image.slidesharecdn.com/dna-replication-lin-140210083429-phpapp02/95/dna-replicationlin-4-638.jpg?cb=1392021295" width=400/>

So we can now understand and look for something very important called a reverse complement. The definition of which is right there in the name. ACTG is the reverse complement of CAGT. Let's now write a simple funciton to find the reverse complement.
<!-- #endregion -->

<!-- #region slideshow={"slide_type": "subslide"} hideCode=false hidePrompt=false -->
**Exercise 3.** Write a function that find the reverse complement of a DNA sequence.
* Input: A string ``text`` representing DNA.
* Output: The reverse complement of ``text``.
<!-- #endregion -->

```python slideshow={"slide_type": "fragment"} hideCode=false hidePrompt=false
def reverse_complement(text):
    text = text[::-1].lower()
    chars = []
    # YOUR SOLUTION HERE
    return "".join(chars)
```

```python slideshow={"slide_type": "skip"} hideCode=false hidePrompt=false
reverse_complement("cagt")
```

<!-- #region slideshow={"slide_type": "subslide"} hideCode=false hidePrompt=false -->
### Back to our 9-mers
<!-- #endregion -->

```python slideshow={"slide_type": "fragment"} hideCode=false hidePrompt=false
solutions = frequent_words(text,9)
print(solutions)
print("Reverse complement of first 9-mer:",reverse_complement(solutions[0][0]))
```

<!-- #region slideshow={"slide_type": "fragment"} hideCode=false hidePrompt=false -->
What is interesting about the reverse complement of the first 9-mer?
<!-- #endregion -->

<!-- #region slideshow={"slide_type": "subslide"} hideCode=false hidePrompt=false -->
### Writing faster code
**Exercise 4.** Let's now write faster code that produces a frequency map. 
* Input: A string ``text`` representing DNA and integer ``k``.
* Output: a frequency map (Python dictionary) that maps every pattern of size ``k`` to the number of times that pattern occurs.
<!-- #endregion -->

```python slideshow={"slide_type": "fragment"} hideCode=false hidePrompt=false
def frequency_table(text,k):
    freq_map = {}
    n = len(text)
    for i in range(n-k+1):
        # YOUR SOLUTION HERE
        pass
    return freq_map
```

```python slideshow={"slide_type": "skip"} hideCode=false hidePrompt=false
freq_map = frequency_table(text,3)
```

<!-- #region slideshow={"slide_type": "subslide"} -->
## A word about packages
I try to limit the number of Python packages that you need for this class. They are roughly pandas+numpy and networkx.

In your project, you are welcome to use bioinformatics Python and non-Python packages. You are encouraged to do so.
<!-- #endregion -->

```python slideshow={"slide_type": "subslide"} hideCode=false hidePrompt=false
# I'm only using pandas here so the output is reasonable, you can remove it of course and see the full dictionary
import pandas as pd
pd.Series(frequency_table(text,3))
```

<!-- #region slideshow={"slide_type": "subslide"} hideCode=false hidePrompt=false -->
### Write better frequent words
**Exercise 5.** Write a function that finds the frequent patterns using a dictionary/map. 
* Input: A string ``text`` representing DNA and integer ``k``.
* Output: All most frequent *k*-mers in ``text`` and their count.
* Requirements: Use your frequency_table function (i.e., use the dictionary).
<!-- #endregion -->

```python slideshow={"slide_type": "fragment"} hideCode=false hidePrompt=false
def better_frequent_words(text,k):
    frequent_patterns = []
    freq_map = frequency_table(text,k)
    # YOUR SOLUTION HERE
    return frequent_patterns,max_value
```

```python slideshow={"slide_type": "skip"} hideCode=false hidePrompt=false
better_frequent_words(text,9)
```

<!-- #region slideshow={"slide_type": "subslide"} hideCode=false hidePrompt=false -->
### Clump Finding Problem
* Imagine you are trying to find *ori* in a newly sequenced genome
* Old frequent hiddent messages won't be useful
* One solution is to use a sliding window and look for a region where a $k$-mer appears several times in short succession
* For example if TGCA forms a (25,3)-clump then it appears at least 3 times in a window of length 25
<!-- #endregion -->

<!-- #region slideshow={"slide_type": "subslide"} hideCode=false hidePrompt=false -->
Even if we solve the clump finding problem, we still have an issue
* Specifically, for the *E. coli* genome we find hundreds of different 9-mers forming (500,3)-clumps
* This makes it absolutely unclear which of these 9-mers might represent a DnaA box in the bacterium’s *ori* region.
* Please read the next sections entitled "The Simplest Way to Replicate DNA" and "Asymmetry of Replication". Dig into the biology, but the abstract model/representation we are using in this class does not require you to understand that biology in detail. Chat with me in Slack about what you find confusing and interesting. 
<!-- #endregion -->

<!-- #region slideshow={"slide_type": "subslide"} hideCode=false hidePrompt=false -->
### Statistics of the Foward and Reverse Half-Strands
The most important consequence for us from the discussion of DNA replication is that we now have four pieces
    1. Forward half-strand x 2
    2. Reverse half-strand x 2

<img src="http://bioinformaticsalgorithms.com/images/Replication/half_strands.png" width=400>


<!-- #endregion -->

<!-- #region slideshow={"slide_type": "subslide"} hideCode=false hidePrompt=false -->
### Why does this matter?
Consider the genome of *Thermotoga petrophila*. If we count the nucleotides in the forward and reverse half strands, then we get the following:

<img src="http://bioinformaticsalgorithms.com/images/Replication/forward_reverse_nucleotide_counts.png" width=400>

Notice that the number of C's and G's is different in the reverse and forward half-strand. Why is this?
<!-- #endregion -->

<!-- #region slideshow={"slide_type": "subslide"} hideCode=false hidePrompt=false -->
Take a minute to read this and then we will discuss together and then in groups depending on time:

"It turns out that we observe these discrepancies because cytosine (C) has a tendency to mutate into thymine (T) through a process called deamination. Deamination rates rise 100-fold when DNA is single-stranded, which leads to a decrease in cytosine on the forward half-strand. Also, since C-G base pairs eventually change into T-A base pairs, deamination results in the observed decrease in guanine (G) on the reverse half-strand (recall that a forward parent half-strand synthesizes a reverse daughter half-strand, and vice-versa)." - Bioinformatics Algorithms 3rd Edition
<!-- #endregion -->

<!-- #region slideshow={"slide_type": "subslide"} hideCode=false hidePrompt=false -->
### Minimum skew problem
We can use this statistic to find the *ori*.

Our idea is to traverse the genome, keeping a running total of the difference between the counts of G and C. If this difference starts increasing, then we guess we are on the forward half-strand. If this difference starts decreasing, then we guess that we are on the reverse half-strand.


<img src="http://bioinformaticsalgorithms.com/images/Replication/increasing_decreasing_skew.png" width=600>

<!-- #endregion -->

<!-- #region slideshow={"slide_type": "subslide"} hideCode=false hidePrompt=false -->
We define $Skew_i(Genome)$ as the difference between the total number of occurrences of G and the total number of occurrences of C in the first $i$ nucleotides of Genome. 

Note that we can compute $Skew_i(Genome)$ incrementally.  

If the next nucleotide is G, then $Skew_{i+1}(Genome)$ = $Skew_i(Genome)$ + 1

if this nucleotide is C, then $Skew_{i+1}(Genome)$ = $Skew_i(Genome)$ – 1

otherwise, $Skew_{i+1}(Genome)$ = $Skew_i(Genome)$.
<!-- #endregion -->

<!-- #region slideshow={"slide_type": "subslide"} hideCode=false hidePrompt=false -->
**Exercise 6:** Compute the skew at every position of a Genome

Input: A DNA string Genome.

Output: An array that computes the $Skew_i(Genome)$. You can assume $Skew_0(Genome)$=0
<!-- #endregion -->

```python slideshow={"slide_type": "fragment"} hideCode=false hidePrompt=false
def skew(genome):
    skews = [0]
    # YOUR SOLUTION HERE
    return skews
```

<!-- #region slideshow={"slide_type": "subslide"} hideCode=false hidePrompt=false -->
### Reading in the *E coli* genome
I'll do this for you.
<!-- #endregion -->

```python slideshow={"slide_type": "fragment"} hideCode=false hidePrompt=false
import pandas as pd
data = pd.read_table("http://bioinformaticsalgorithms.com/data/realdatasets/Rearrangements/E_coli.txt",header=None)
genome = data.values[0,0]
```

```python slideshow={"slide_type": "skip"} hideCode=false hidePrompt=false
skews = skew(genome)
```

```python slideshow={"slide_type": "skip"} hideCode=false hidePrompt=false
# Again I'm using pandas because the display would be horrible otherwise.
# I will either give you the pandas code or teach you that pandas/numpy code
skews = pd.Series(skew(genome))
skews
```

```python slideshow={"slide_type": "subslide"} hideCode=false hidePrompt=false
%matplotlib inline
skews.plot.line()
```

<!-- #region slideshow={"slide_type": "fragment"} hideCode=false hidePrompt=false -->
Where do you think the *ori* is located?
<!-- #endregion -->

```python slideshow={"slide_type": "fragment"} hideCode=false hidePrompt=false
print('Position:',skews.idxmin()+1)
```

```python slideshow={"slide_type": "skip"} hideCode=false hidePrompt=false
# Don't forget to push!
```

```python hideCode=false hidePrompt=false

```
