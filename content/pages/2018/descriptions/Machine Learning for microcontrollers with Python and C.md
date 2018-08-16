Title:Machine Learning for microcontrollers with Python and C
URL:2018/descriptions/Machine Learning for microcontrollers with Python and C.html
save_as: 2018/descriptions/Machine Learning for microcontrollers with Python and C.html



# Machine Learning for microcontrollers with Python and C
Machine learning is making its way into many industries and applications,
and for many usecases the Python ecosystem has excellent solutions available, for example scikit-learn. However applications based on embedded systems and microcontrollers have severe memory, CPU and energy constraints which make established Python-based solutions unsuitable.

This talk shows how existing scikit-learn estimators can be combined with classifier implementations in portable C code tailored for running on embedded hardware platforms.
This approach allows to train and validate models using existing Python workflows,
and then run efficiently on low-end microcontrollers.
Currently the project covers classifiers using Decision Tree ensembles (Random Forest and extratrees), and Gaussian Naive Bayes. This is provided by two Python packages,
[emtrees](https://github.com/jonnor/emtrees) and [embayes](https://github.com/jonnor/embayes).

Some aspects might also be of interest when hitting performance bottlenecks in larger computing systems.