Title:Imbalanced-learn: a scikit-learn-contrib to tackle learning from imbalanced data set
URL:2018/descriptions/Imbalanced-learn: a scikit-learn-contrib to tackle learning from imbalanced data set.html
save_as: 2018/descriptions/Imbalanced-learn: a scikit-learn-contrib to tackle learning from imbalanced data set.html



# Imbalanced-learn: a scikit-learn-contrib to tackle learning from imbalanced data set
## The curse of imbalanced data sets

The curse of imbalanced data set refers to data sets in which the number of samples in one class is less than in others. This issue is often encountered in real world data sets such as medical imaging applications (e.g. cancer detection), fraud detection, etc. In such particular condition, machine learning algorithms learn sub-optimal models which will generally favor the class having the largest number of samples.

In this talk, we will present the imbalanced-learn package which implement some of the state-of-the-art algorithms, tackling the class imbalance problem.

## A scikit-learn-contrib project

scikit-learn includes a tremendous set of pre-processing methods (i.e. transformers, standardizers, etc.) to optimally train machine learning algorithms. However, there is currently no estimators to reduce or generate samples. Therefore, the imbalanced-learn provides a new type of estimator, named sampler, aiming at resampling a data set whenever it is desired.

We will give a brief overview of the imbalanced-learn API and its integration with scikit-learn.

## Overview of the propose methods

Regarding the data science aspect of this talk, we will highlight the distinctive characteristics of the different algorithms: (i) over-sampling, (ii) controlled under-sampling, (iii) cleaning under-sampling, (iv) combination of over-sampling and cleaning under-sampling, and (v) ensemble sampler.

## What's new in 0.4

We are going to make a new release at the same time than scikit-learn 0.20 which will incorporate new features:

* Change of API
* Documentation User Guide
* `FunctionSampler` with an application on outlier rejection
* Keras and Tensforflow balanced batch generator