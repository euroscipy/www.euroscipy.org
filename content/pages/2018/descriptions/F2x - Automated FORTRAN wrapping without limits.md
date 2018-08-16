Title:F2x - Automated FORTRAN wrapping without limits
URL:2018/descriptions/F2x - Automated FORTRAN wrapping without limits.html
save_as: 2018/descriptions/F2x - Automated FORTRAN wrapping without limits.html



# F2x - Automated FORTRAN wrapping without limits
f2py is still a very important tool for the scientific community. However, even though some efford has been put in upgrading it, it did not overcome it's initial limitations (e.g. no support for derived types). When we ran into some of these limitations, we decided not to extend f2py but to start our own wrapper that could

* work out of the box,
* wrap derived types and complex interfaces,
* use modern FORTRAN features for compiler-neutral wrapping,
* generate wrappers for other high-level languages.

The result is F2x which is already in productive use within the German Aerospace Center. In contrast to f2py it uses a real FORTRAN grammar and template-based code generation. While this slows down the wrapping process, it comes with way more potential for adaptation and extension. Using Cython as wrapping target, we could observe a runtime performance equal to that of f2py.

F2x is available as open source and actively developed under https://github.com/DLR-SC/F2x.