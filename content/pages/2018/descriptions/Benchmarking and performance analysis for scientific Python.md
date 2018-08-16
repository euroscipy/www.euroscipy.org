Title:Benchmarking and performance analysis for scientific Python
URL:2018/descriptions/Benchmarking and performance analysis for scientific Python.html
save_as: 2018/descriptions/Benchmarking and performance analysis for scientific Python.html



# Benchmarking and performance analysis for scientific Python
Benchmarking and profiling is a necessary first step before any code optimization.
This talk will start by reviewing tools available in the scientific Python ecosystem that
could be used for this purpose. In particular, we will discuss different approaches for run time
measurements (as well as associated pitfalls), memory usage evaluation with the
[memory_profiler](https://github.com/pythonprofilers/memory_profiler) and, more generally, useful OS level
metrics available via the [psutil](https://github.com/giampaolo/psutil) package. Evaluation of parallelization
efficiency in scientific Python applications will also be discussed.

Finally, I will introduce the [neurtu](https://github.com/symerio/neurtu) package that aims to facilitate
time and memory complexity estimation as well as to provide a consistent API
for parametric benchmarks with multiple metrics. It also allows to control BLAS multi threading at run-time.