Title:Python Tools for Climate Science
URL:2018/descriptions/Python Tools for Climate Science.html
save_as: 2018/descriptions/Python Tools for Climate Science.html



# Python Tools for Climate Science
Climate Science has always been a domain of "big data" and scientific programming languages like Fortran to run complex models on high-performance clusters -- but through its extensive set of data tools and scientific libraries Python usage has  increased rapidly. This talk will focus on the "small data" of Climate Science and present a few Simple Climate Models and the datasets needed to use them:

Simple Climate Models are models of reduced complexity which can run within seconds and are widely used to assess climate scenarios and progress in emissions reductions, or to emulate complex climate models and to analyse uncertainties.

Three models are easily usable with Python:

Pymagicc ([Gieseke, Willner, Mengel, 2018](https://doi.org/10.21105/joss.00516)), which wraps the widely used model MAGICC using [Wine](https://www.winehq.org/) to run the Windows-only binary on all platforms.

Pyhector ([Willner, Hartin, Gieseke, 2017](https://doi.org/10.21105/joss.00248)) is a Python interface to the Hector model written in C++ and allows it to drive the model with Pandas DataFrames and Python dictionaries as input instead of CSV files and INI-files.

[FAIR](https://github.com/OMS-NetZero/FAIR) ([Smith et al., 2017, in discussion]( https://doi.org/10.5194/gmd-2017-266)) is another Simple Climate Model written completely in Python and thus the easiest to explore.

To drive and validate these models data like global surface temperatures, greenhouse gas concentrations and emissions in an easily processable format are needed.

Python's data tools are ideally suited to get data out of Excel sheets or custom text formats and turn them into clean CSV files and [Data Packages](https://frictionlessdata.io/) that can easily be used with Python and Pandas and in Jupyter Notebooks.

See [openclimatedata.net](https://openclimatedata.net/) for an overview and example notebooks powered by [Binder](https://mybinder.org/).