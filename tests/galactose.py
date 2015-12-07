"""
Some test simulations and behavior.
"""


import roadrunner
print roadrunner.__version__
rr = roadrunner.RoadRunner("../models/galactose_28_annotated.xml")
# s = rr.simulate(0, 50, 1000, plot=True)
s = rr.simulate(0, 50, 1000, plot=True, stiff=True, absolute=1E-16, relative=1E-16)


