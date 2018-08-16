Title:Scikit-learn and tabular data: closing the gap
URL:2018/descriptions/Scikit-learn and tabular data: closing the gap.html
save_as: 2018/descriptions/Scikit-learn and tabular data: closing the gap.html



# Scikit-learn and tabular data: closing the gap
Scikit-learn traditionally centered its data model around numpy arrays (and sparse matrices), for good historical and implementation details. However, in an important subset of scikit-learn's usecases, the original data in the machine learning pipeline is tabular: heterogenously typed and labeled. In the meantime, pandas has become very popular, and is one of the driving foces behind the huge popularity of Python for data science (amongst other libraries!). Pandas DataFrames are increasingly used to represent those tabular data, but scikit-learn does not always play well with it.

Typically you need to preprocess the data (vectorize or featurize) to obtain array data. But until recently, the preprocessing tools of scikit-learn were lacking to deal with heterogenous tabular data (e.g. using different transformations for different columns, dealing with categorical data). Further, the label information of the data (the column names (and row labels)) gets lost.

This talk will give an overview of the challenges and current bottlenecks when working with tabular data and scikit-learn. Then it will show the ungoing developments in sckikit-learn to improve this situation as well as highlight some third-party libraries that try to ease those problems. Finally conclude with some open questions on what further needs to be done in this area.