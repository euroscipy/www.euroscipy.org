Title:Going full Python for Machine Learning in Biomedical engineering
URL:2018/descriptions/Going full Python for Machine Learning in Biomedical engineering.html
save_as: 2018/descriptions/Going full Python for Machine Learning in Biomedical engineering.html



# Going full Python for Machine Learning in Biomedical engineering
The talk with cover the following reflexions coming from the application:
First we need to address a set of constrains coming from the Biomedical application:
  - Data is expensive but dimensions are many: gathering experimental data on humans is complicated (ethics, recruiting subjects, performing actual measurements…) but then each recording holds  a lot of informations (tens of EMG channels at up to 4kHz, accelerometers, motion capture…) and many features can be extracted from that raw data.
  - Robustness is important to address early as there can be a high variability of the signals recorded between subjects but also for the same subject at different times or in slightly different conditions (for example just misplacing electrodes)
  - Supervision of algorithm can be tricky: specially in absence of objective gold standard, then categorization of subjects is often subjective (type/stage of pathology established only by clinical score or MD appreciation)
  - Accuracy is critical in medical application: Sensitivity and Specificity must be as high as possible as  false negative would mean failing to treat and false positive treating healthy patients.
  - Finally, the whole process has to be fully automated and fast to fit within existing procedures and time frames.

We choose to go full Python for our developments in this project for Python versatility and efficiency:
  - We need to test and prototype many methods to find the most suitable ones: *scipy* and *scikit* learn have already implemented most components we might need. Hence we can focus on application specific aspects.
  - We need to communicate with non developers (experimenters, MD,…) at various stages with plots, graphical interfaces or even dynamics websites: this can be covered easily in Python.
  - We wish for our code to take advantage of currently available hardware: parallel computation and GPU usage can be easily prototyped with *Numba*, *Dask* or *TensorFlow/CAFFE*.
  - Finally, Python enables us to address all these task with a single language, easy to learn for interns/students hired within the project.