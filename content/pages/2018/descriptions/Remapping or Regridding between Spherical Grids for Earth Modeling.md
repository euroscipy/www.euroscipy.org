Title:Remapping or Regridding between Spherical Grids for Earth Modeling
URL:2018/descriptions/Remapping or Regridding between Spherical Grids for Earth Modeling.html
save_as: 2018/descriptions/Remapping or Regridding between Spherical Grids for Earth Modeling.html



# Remapping or Regridding between Spherical Grids for Earth Modeling
Earth modeling and simulation, including atmosphere, ocean, and land, are actively under study to better understand and predict global environmental systems. A variety of spherical grids such as latlon, tripole, cubed-sphere, icosahedral are used for the earth simulations. Since the various spherical grids are used in combination, the remapping or regridding between the grids is positively necessary. In this talk, I will introduce a novel toolkit for remapping or regridding between general spherical grids. The toolkit supports various remapping methods such as bilinear, conservative, nearest, Lagrange, dominant type. The toolkit is also fast and scalable by using a new efficient search algorithm. The main functions of the toolkit are written in Fortran90, and they are wrapped to python modules using ctypes and Numpy’s ctypeslib.