:::::::::::::::::::::::::::: SALESKEN.AI ﻿::::::::::::::::::::::::::::

:::::::::::: (MSR-Paraphrase, Microsoft Research Paraphrase Corpus) data set ::::::::::::

The data set contains the following:
------------------------------------
  README.md 		  				this file
  MSRpar.txt		  				tab separated input file with sentence pairs
  MSRpar.train-STSBenchmark.ipynb                       Python script to compare human judgements with USE & BERT


Introduction of data set:
-------------------------
Given two sentences of text, s1 and s2, the systems participating in
this task should compute how similar s1 and s2 are, returning a
similarity score.

The dataset comprises pairs of sentences drawn from the publicly
available datasets:

- MSR-Paraphrase, Microsoft Research Paraphrase Corpus
  http://research.microsoft.com/en-us/downloads/607d14d9-20cd-47e3-85bc-a2f65cd28042/
  750 pairs of sentences.


Data set fields:
----------------
- sentence 1
- sentence 2
- semantic relatedness label (on a 0-5 continuous scale)


Task Definition:
----------------
Given two sentences, you are asked to return a continuous valued similarity score on a scale from 0 to 5, with 0 indicating that the semantics of the sentences are completely independent and 5 signifying semantic equivalence. Compute between machine assigned (USE and BERT) semantic similarity scores and human judgements.


Performance:
------------
Performance is assessed by computing the Pearson correlation between USE & BERT semantic similarity scores and human judgements.


Python script notebook:
-----------------------
- MSRpar.train-STSBenchmark.ipynb


Resources:
----------
- https://www.aclweb.org/anthology/S17-2001
- https://www.researchgate.net/publication/330257597_Cross-		Lingual_Semantic_Textual_Similarity_Modeling_Using_Neural_Networks_14th_China_Workshop_CWMT_2018_Wuyishan_China_October_25-26_2018_Proceedings#pf8

