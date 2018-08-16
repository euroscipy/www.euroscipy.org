Title:Parselmouth: an efficient Python interface to the Praat phonetics software package
URL:2018/descriptions/Parselmouth: an efficient Python interface to the Praat phonetics software package.html
save_as: 2018/descriptions/Parselmouth: an efficient Python interface to the Praat phonetics software package.html



# Parselmouth: an efficient Python interface to the Praat phonetics software package
[Praat](http://www.fon.hum.uva.nl/praat/) is a widely used software package in phonetics and other speech sciences. It contains a wide range of algorithms related to the acoustic analysis, manipulation, and synthesis of speech signals. However, being an independent application with its own scripting language, the integration with other scientific software and a general-purpose programming language is not as straightforward or efficient as an experienced Python user would want or expect.

We have developed [Parselmouth](https://github.com/YannickJadoul/Parselmouth) as a Python interface to Praat. Rather than offering a thin interface to the Praat commands and scripting language, our goal is to provide a full-fledged Python library that integrates well with common Python idioms and other scientific libraries such as NumPy. Yet, at the same time we want the library to access Praat's C/C++ algorithm implementations and data structures rather than reimplementing them. The [pybind11](https://github.com/pybind/pybind11) library allows us to achieve this desired trade-off and wrap the existing Praat codebase into a Python extension module without incurring an enormous performance penalty.

After primarily focussing on introducing Parselmouth to the target audience of academic Praat users, we now want to present this project to the Python scientific community. On the one hand, Parselmouth can become an additional tool for scientific research in Python. On the other hand, we hope the technical solution and development might inspire similar projects to interface existing scientific software with Python.