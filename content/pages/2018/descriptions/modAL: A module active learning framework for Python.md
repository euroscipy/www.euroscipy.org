Title:modAL: A module active learning framework for Python
URL:2018/descriptions/modAL: A module active learning framework for Python.html
save_as: 2018/descriptions/modAL: A module active learning framework for Python.html



# modAL: A module active learning framework for Python
With the recent explosion of available data, you have can have millions of unlabelled examples with a high cost to obtain labels. Active learning is a machine learning technique which aims to find the potentially most informative instances in unlabeled datasets, allowing the you to label it and improve the performance of classification.

[modAL](https://cosmic-cortex.github.io/modAL/) is a new active learning framework for Python, designed with modularity, flexibility and extensibility in mind. The key components of any workflow are the machine learning algorithm you choose and the query strategy you apply to request labels for the most informative instances. With [modAL](https://cosmic-cortex.github.io/modAL/), instead of choosing from a small set of built-in components, you have the freedom to seamlessly integrate scikit-learn or Keras models into your algorithm and easily tailor your custom query strategies, allowing the rapid development of active learning workflows with nearly complete freedom.

modAL is fully open source and [hosted on GitHub](https://github.com/cosmic-cortex/modAL/).