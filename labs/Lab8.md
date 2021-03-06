---
jupyter:
  jupytext:
    encoding: '# -*- coding: utf-8 -*-'
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

<!-- #region slideshow={"slide_type": "slide"} -->
# Lab 8 - Are there fragile regions in the human genome?

## Clustering Algorithms - Chapter 8
Material and embedded lab.

Motivation and some exercises are variations on those available in Bioinformatics Algorithms: An Active-Learning Approach by Phillip Compeau & Pavel Pevzner.
<!-- #endregion -->

<!-- #region slideshow={"slide_type": "subslide"} -->
## Assignments for week
* Labs and keep on making progress on the project (keep up the good work)!

## Other announcements
* Slides from Monday. Questions?
* Extension labs are coming Week 10, so don't cut corners on these strength building labs

## Plans for today
We are going to walk through this together. Unlike other labs where we wrote algorithms from scratch, we are going to use implementations today.
<!-- #endregion -->

<!-- #region slideshow={"slide_type": "subslide"} -->
## Slack ice breaker
Best meal you've ever eaten?
<!-- #endregion -->

<!-- #region slideshow={"slide_type": "slide"} -->
## Biology from a biologist

<a href="https://calpoly.zoom.us/rec/share/l5hfMH_OtdbAo4-ow76eOgR2F4Lh92mG9YHkEPh6CSElixfS2awWOKcEW34XxrbT.mZKbQHX4hni3U4IO?startTime=1604435224000">Transcriptomics perspective</a>

Watch the first 3 minutes and then answer in your group: "What is the transcriptome?" We'll discuss together about 5 minutes is up.
<!-- #endregion -->

<!-- #region slideshow={"slide_type": "slide"} -->
## Clustering
Clustering or partitioning data into sets is not specific to bioinformatics. Let's first talk about clustering in a generic sense.

<a href="http://anderson-data-science.com/csc_448_2020_fall/clustering.pptx">http://anderson-data-science.com/csc_448_2020_fall/clustering.pptx</a>
<!-- #endregion -->

<!-- #region slideshow={"slide_type": "slide"} -->
## What's all this about yeast and wine?
<!-- #endregion -->

<!-- #region slideshow={"slide_type": "subslide"} -->
The species of yeast that we will consider in this chapter is Saccharomyces cerevisiae, which **can brew wine because it converts the glucose found in fruit into ethanol**. We will therefore begin with a simple question: if S. cerevisiae often lives on grapevines, **why must crushed grapes be stored in tightly sealed barrels in order to make wine?**

Once its supply of glucose runs out, S. cerevisiae must do something to survive. It therefore inverts its metabolism, with the ethanol that it just produced becoming its new food supply. This metabolic inversion, called the diauxic shift, can only occur in the presence of oxygen. Without oxygen, S. cerevisiae hibernates until either glucose or oxygen becomes available. In other words, if winemakers don’t seal their barrels, then the yeast in the barrel will metabolize the ethanol that it just produced, ruining the wine.

The diauxic shift is a complex process that affects the expression of many genes. 
<!-- #endregion -->

<!-- #region slideshow={"slide_type": "slide"} -->
## Our data
>In 1997, Joseph DeRisi conducted the first massive gene expression experiment by sampling an S. cerevisiae culture every two hours for the six hours before and after the diauxic shift. Since there are approximately 6,400 genes in S. cerevisiae, and there were seven time points, this experiment resulted in a 6,400 × 7 gene expression matrix. 
<!-- #endregion -->

```python slideshow={"slide_type": "subslide"}
import pandas as pd
df=pd.read_csv('http://bioinformaticsalgorithms.com/data/realdatasets/Clustering/diauxic_raw_ratios_RG.txt',sep='\t')
df
```

<!-- #region slideshow={"slide_type": "subslide"} -->
Values above 1 in expression vectors correspond to increased expression, while values below 1 correspond to decreased expression.
<!-- #endregion -->

```python slideshow={"slide_type": "subslide"}
import altair as alt
plot_df = df.set_index('ORF').drop('Name',axis=1).loc[['YPR055W','YLR258W','YPL012W']]
plot_df.columns.name = 'Sample Point'
plot_df = plot_df.stack().to_frame()
plot_df.columns=["Ratio"]
plot_df = plot_df.reset_index()
alt.Chart(plot_df).mark_line().encode(
    x='Sample Point:N',
    y='Ratio',
    color='ORF'
)
```

<!-- #region slideshow={"slide_type": "subslide"} -->
**Exercise 1.** What is the interpretation of this plot?

Take 5 minutes in a breakout room, and then let's come back together.
<!-- #endregion -->

<!-- #region slideshow={"slide_type": "subslide"} -->
### YOUR SOLUTION HERE
<!-- #endregion -->

<!-- #region slideshow={"slide_type": "subslide"} -->
Consider what to do about the other genes?
<!-- #endregion -->

```python slideshow={"slide_type": "fragment"}
df.shape
```

<!-- #region slideshow={"slide_type": "subslide"} -->
**Exercise 2.** Considering the dataset above and what you now know about clustering, what questions could you ask?

Take 5 minutes in a breakout room, and then let's come back together.
<!-- #endregion -->

<!-- #region slideshow={"slide_type": "subslide"} -->
### YOUR SOLUTION HERE
### YOUR SOLUTION HERE
<!-- #endregion -->

<!-- #region slideshow={"slide_type": "subslide"} -->
## Sample of genes
<!-- #endregion -->

```python slideshow={"slide_type": "fragment"}
import altair as alt
plot_df = df.set_index('ORF').drop('Name',axis=1).sample(n=100)
plot_df.columns.name = 'Sample Point'
plot_df = plot_df.stack().to_frame()
plot_df.columns=["Ratio"]
plot_df = plot_df.reset_index()
alt.Chart(plot_df).mark_line().encode(
    x='Sample Point:N',
    y='Ratio',
    color='ORF'
)
```

<!-- #region slideshow={"slide_type": "subslide"} -->
**Exercise 3:** What is a good guess on a good ``k`` value?
<!-- #endregion -->

<!-- #region slideshow={"slide_type": "subslide"} -->
### YOUR SOLUTION HERE
### YOUR SOLUTION HERE
<!-- #endregion -->

<!-- #region slideshow={"slide_type": "subslide"} -->
Let's remove genes that are not of interest. This is done in the textbook by removing genes that don't go up or down by a significant amount. 
<!-- #endregion -->

```python slideshow={"slide_type": "fragment"}
df_subset = pd.read_csv('http://bioinformaticsalgorithms.com/data/realdatasets/Clustering/230genes_log_expression.txt',sep='\t')
df_subset
```

<!-- #region slideshow={"slide_type": "subslide"} -->
### Redo the plot
<!-- #endregion -->

```python slideshow={"slide_type": "fragment"}
plot_df = df_subset.set_index('ORF').drop('Name',axis=1).sample(n=100)
plot_df.columns.name = 'Sample Point'
plot_df = plot_df.stack().to_frame()
plot_df.columns=["Ratio"]
plot_df = plot_df.reset_index()
alt.Chart(plot_df).mark_line().encode(
    x='Sample Point:N',
    y='Ratio',
    color='ORF'
)
```

```python slideshow={"slide_type": "subslide"}
# our standard imports
import numpy as np
import pandas as pd

from sklearn.cluster import KMeans
```

<!-- #region slideshow={"slide_type": "subslide"} -->
**Exercise 4:** Using your k value, cluster the genes using k-means. You may use sklearn's version of kmeans. Color the plot above using your clusters.
<!-- #endregion -->

<!-- #region slideshow={"slide_type": "subslide"} -->
### Note to move to board and explain sklearn
<!-- #endregion -->

```python slideshow={"slide_type": "subslide"}
clusterer = KMeans(n_clusters=3, random_state=10)
df_subset["Cluster"] = clusterer.predict(df_subset.drop(['ORF','Name'],axis=1))
df_subset
```

<!-- #region slideshow={"slide_type": "subslide"} -->
**Exercise 5:** Plot all of the genes with color according to their cluster. 
<!-- #endregion -->

```python slideshow={"slide_type": "subslide"}
### YOUR SOLUTION HERE
### YOUR SOLUTION HERE
```

<!-- #region slideshow={"slide_type": "subslide"} -->
**Exercise 6**: How can you now if you selected the right number of clusters?
<!-- #endregion -->

<!-- #region slideshow={"slide_type": "subslide"} -->
### YOUR SOLUTION HERE
### YOUR SOLUTION HERE
<!-- #endregion -->

```python slideshow={"slide_type": "subslide"}
from sklearn.metrics import silhouette_score

### YOUR SOLUTION HERE
cluster2 = clusterer2.predict(df_subset.drop(['ORF','Name','Cluster'],axis=1))
cluster3 = clusterer3.predict(df_subset.drop(['ORF','Name','Cluster'],axis=1))
print('Score for k=2',silhouette_score(df_subset.drop(['ORF','Name','Cluster'],axis=1), cluster2))
print('Score for k=3',silhouette_score(df_subset.drop(['ORF','Name','Cluster'],axis=1), cluster3))
```

```python

```
