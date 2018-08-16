Title:Pyccel, a Fortran static compiler for scientific High-Performance Computing
URL:2018/descriptions/Pyccel, a Fortran static compiler for scientific High-Performance Computing.html
save_as: 2018/descriptions/Pyccel, a Fortran static compiler for scientific High-Performance Computing.html



# Pyccel, a Fortran static compiler for scientific High-Performance Computing
*Pyccel* is a new **static compiler** for Python that uses **Fortran** as backend language while enabling High-Performance Computing **HPC** capabilities.

Fortran is a computer language for scientific programming that is tailored for efficient run-time execution on a wide variety of processors. Even if the *2003* and *2008* standards added major improvements like *OOP, Coarrays, Submodules, do concurrent*, etc ... they are not covered by all available compilers. Moreover, the Fortran developer still suffers from the lack of **meta-programming** compared to **C++** ones. Therefore, it is more and more difficult for applied mathematicians and computational physicists to write applications at the *state of art* (targeting CPUs, GPUs, MICs) while implementing complicated algorithms or numerical schemes.

Pyccel can be used in two cases:

- accelerate Python code by converting it to Fortran and calling *f2py*,
- generate portable HPC Fortran codes from a DSL using the Python syntax.

In order to achieve the second point, we developed an internal DSL for *types* and *macros*. The later is used to map sentences based on *mpi4py*, *scipy.linalg.blas or lapack* onto the appropriate calls in Fortran. Moreover, two parsers, for *OpenMP* and *OpenACC*, were added too, allowing for explicit parallelism through the use of pragmas.

Last but not least, Pyccel is an extension of **Sympy**. Actually, it converts a Python code to symbolic expressions/trees, from a Full Syntax Tree (*RedBaron*), then annotates the new AST using types or different settings provided by the user.

In this talk, after a brief description of Pyccel, we will show different applications including Finite Elements (1d, 2d, 3d), Kronecker linear solvers and Neural Networks.