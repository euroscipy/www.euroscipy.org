Title:Detecting anomalies using statistical distances
URL:2018/descriptions/Detecting anomalies using statistical distances.html
save_as: 2018/descriptions/Detecting anomalies using statistical distances.html



# Detecting anomalies using statistical distances
Statistical distances are distances between distributions or data samples and are used in a variety of machine learning applications. Unlike statistical hypothesis tests such as the well-known Kolmogorov-Smirnov test[1], which answer yes-or-no questions (through whether or not they reject the null hypothesis), statistical distances quantitatively show how similar or how different two distributions or data samples are. As such, they pave the way for robust machine learning algorithms, including anomaly detection algorithms.

Datadog, as a cloud monitoring company, collects system, application and business metrics as time-series, and uses sophisticated algorithms to detect anomalous patterns. On the way to designing such algorithms, we experimented with a few statistical distances and studied their properties. As part of the process, we implemented the Wasserstein distance (a.k.a. the  Earth-Mover's distance) and the Cramér-von Mises distance between one-dimensional distributions. As those distances are not available in any common Python libraries, we decided to contribute our implementations to SciPy[2].

The talk will not assume any prior knowledge on the topic. After a quick reminder of the mathematical notions of distance and distribution, the talk will focus on practical ways to use the statistical distance functions now available in SciPy to study datasets and samples. Using concrete examples, we will first explain the motivation for using such functions rather than more classical statistical tools. Classical methods for comparing data samples sometimes involve comparing their statistics (mean, median, standard deviation, kurtosis, etc.). Based on the specificities of the data and the properties that are deemed relevant to the problem at hand, some sample statistics are usually favored: if the spread is relevant, the standard deviation might be used; in the presence of outliers, the median is a more robust statistic than the arithmetic mean and will be a good choice. However, such methods usually discard information about the whole sample distribution and might miss relevant patterns.

Statistical distances are an interesting alternative to sample statistics when comparing samples. Through visual illustrations, the talk will focus on a few common statistical distances, highlighting their strengths and their weaknesses, explaining when each of them can and should be used (see our blog post[3] for some of these details). Specifically, the Kolmogorov-Smirnov distance (as opposed to the test) is convenient to use in the presence of outliers but proves noisy with small datasets. The Wasserstein distance is less noisy, sensitive to outliers but still suffers some caveats. The Cramér-Von Mises distance shares properties with both former distances and reveals itself robust in most situations.

The talk will end with an overview of the inner workings of our production-ready anomaly detection algorithms that use SciPy's statistical distance functions and a demonstration of how such algorithms perform on real-world data sets.

[1] https://en.wikipedia.org/wiki/Kolmogorov%E2%80%93Smirnov_test
[2] http://github.com/scipy/scipy/pull/7563
[3] https://www.datadoghq.com/blog/engineering/robust-statistical-distances-for-machine-learning/