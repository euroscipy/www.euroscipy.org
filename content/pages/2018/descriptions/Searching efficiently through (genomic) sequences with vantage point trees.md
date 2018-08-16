Title:Searching efficiently through (genomic) sequences with vantage point trees
URL:2018/descriptions/Searching efficiently through (genomic) sequences with vantage point trees.html
save_as: 2018/descriptions/Searching efficiently through (genomic) sequences with vantage point trees.html



# Searching efficiently through (genomic) sequences with vantage point trees
Vantage point trees are data structures that provide a fast lookup mechanism to find the most similar sequence from a set of sequences, given a query sequence. These sequences can be genomic sequences, strings, ... Vantage point trees are similar to kd-trees, but unlike kd-trees they can be defined on spaces that don't have a Euclidean coordinate system, but only a metric distance (in other words, a notion of "similarity").

In this talk I will show how vantage point search outperforms standard (genomic) search implementations, and how the implementation works (both conceptually as well as concretely, using some Numpy and Cython). I will focus in particular on showing how simple scientific Python visualizations can be used to understand this rather mysterious algorithm.